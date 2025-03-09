import math
from typing import Tuple, List, Dict, Optional
import time
from dataclasses import dataclass
import numpy as np
import threading
import scipy.special
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':

    import sys
    sys.path.append("..")
    
import data
from communication.maxon_epos_driver import MaxonMotor
from communication.can_commXYF import *

@dataclass
class RobotConfig:
    """Robot configuration parameters"""
    wheel_radius: float  # mm
    wheel_base: float   # mm
    max_rpm: float
    min_velocity: float  # mm/s 
    max_velocity: float  # mm/s
    min_lookahead: float  # mm
    max_lookahead: float  # mm
    k_lookahead: float
    k_curvature: float
    max_acceleration: float  # RPM per control cycle
    control_delay: float  # seconds
    alpha_filter: float  # Low pass filter coefficient
    position_tolerance: float  # mm

class PathGenerator(ABC):
    """Abstract base class for path generation"""
    @abstractmethod
    def generate_path(self, points: np.ndarray) -> np.ndarray:
        pass

class BezierPathGenerator(PathGenerator):
    """Bezier curve path generator"""
    def __init__(self, n_points: int = 500): # 200
        self.n_points = n_points

    def generate_path(self, control_points: np.ndarray) -> np.ndarray:
        """Generate path using Bezier curves"""
        return self.calc_bezier_path(control_points, self.n_points)
    @staticmethod
    def calc_4points_bezier_path(sx, sy, syaw, ex, ey, eyaw, offset):
        """
        Compute control points and path given start and end position.

        :param sx: (float) x-coordinate of the starting point
        :param sy: (float) y-coordinate of the starting point
        :param syaw: (float) yaw angle at start
        :param ex: (float) x-coordinate of the ending point
        :param ey: (float) y-coordinate of the ending point
        :param eyaw: (float) yaw angle at the end
        :param offset: (float)
        :return: (numpy array, numpy array)
        """
        dist = np.hypot(sx - ex, sy - ey) / offset
        control_points = np.array(
            [[sx, sy],
            [sx + dist * np.cos(syaw), sy + dist * np.sin(syaw)],
            [ex - dist * np.cos(eyaw), ey - dist * np.sin(eyaw)],
            [ex, ey]])

        path = BezierPathGenerator.calc_bezier_path(control_points, n_points=200)

        return path, control_points
    
    @staticmethod
    def calc_bezier_path(control_points: np.ndarray, n_points: int) -> np.ndarray:
        return np.array([
            BezierPathGenerator.bezier(t, control_points) 
            for t in np.linspace(0, 1, n_points)
        ])

    @staticmethod
    def bezier(t: float, control_points: np.ndarray) -> np.ndarray:
        n = len(control_points) - 1
        return np.sum([
            BezierPathGenerator.bernstein_poly(n, i, t) * control_points[i] 
            for i in range(n + 1)
        ], axis=0)

    @staticmethod
    def bernstein_poly(n: int, i: int, t: float) -> float:
        return scipy.special.comb(n, i) * t ** i * (1 - t) ** (n - i)

class MotionController:
    """Handles robot motion control calculations"""
    def __init__(self, config: RobotConfig):
        self.config = config
        self.rpm_to_mms = (2.0 * math.pi * config.wheel_radius) / 60.0
        self._prev_left_rpm = 0
        self._prev_right_rpm = 0
        self._filtered_left_rpm = 0
        self._filtered_right_rpm = 0

    def calculate_wheel_speeds(self, 
                             current_pos: np.ndarray, 
                             current_heading: float,
                             target_point: np.ndarray) -> Tuple[int, int]:
        """Calculate required wheel speeds based on current state and target"""
        v_current = (self._prev_left_rpm + self._prev_right_rpm) * self.rpm_to_mms / 2.0
        
        # Calculate angle to target
        alpha = math.atan2(target_point[1] - current_pos[1], 
                          target_point[0] - current_pos[0])
        delta_angle = np.arctan2(np.sin(alpha - current_heading), 
                                np.cos(alpha - current_heading))
        
        # Calculate curvature and velocity
        lookahead = self._calculate_adaptive_lookahead(v_current)
        curvature = 2.0 * math.sin(delta_angle) / lookahead
        velocity = self._calculate_target_velocity(curvature, v_current)


        error = np.linalg.norm(target_point - current_pos)
    
        # Dodajte korekciju greške u brzine točkova
        # !!!!!!!!!!!!!!!!!!!!!!! P GAIN UBACITI GLOBALNO NEGDEEEEE AAAA
        correction = error * 0.5  # P-gain (možete podesiti ovu vrednost)
    
        # Calculate individual wheel velocities
        left_vel = velocity * (1 - (self.config.wheel_base * curvature) / 2.0) - correction
        right_vel = velocity * (1 + (self.config.wheel_base * curvature) / 2.0) + correction
        
        # Convert to RPM and apply smoothing
        target_left = self._velocity_to_rpm(left_vel)
        target_right = self._velocity_to_rpm(right_vel)
        
        return self._smooth_wheel_speeds(target_left, target_right)

    def _calculate_adaptive_lookahead(self, v_current: float) -> float:
        """Calculate adaptive lookahead distance based on current velocity"""
        lookahead = self.config.k_lookahead * v_current
        return np.clip(lookahead, 
                      self.config.min_lookahead, 
                      self.config.max_lookahead)\
                      
    def _calculate_target_velocity(self, 
                                 curvature: float, 
                                 current_v: float) -> float:
        """Calculate target velocity based on curvature"""
        base_velocity = self.config.max_velocity / (1.0 + self.config.k_curvature * abs(curvature))
        target_v = np.clip(base_velocity, 
                          self.config.min_velocity, 
                          self.config.max_velocity)
        
        # Add velocity ramping
        max_v_change = 100  # mm/s per control cycle
        v_change = np.clip(target_v - current_v, 
                          -max_v_change, 
                          max_v_change)
        return current_v + v_change


    def _velocity_to_rpm(self, velocity: float) -> int:
        """Convert linear velocity to RPM"""
        rpm = velocity / self.rpm_to_mms
        deadband = 2  # RPM
        if abs(rpm) < deadband:
            return 0
        return int(round(np.clip(rpm, -self.config.max_rpm, self.config.max_rpm)))

    def _smooth_wheel_speeds(self, 
                           target_left: int, 
                           target_right: int) -> Tuple[int, int]:
        """Apply acceleration limits and smoothing to wheel speeds"""
        # Apply acceleration limits
        delta_left = np.clip(target_left - self._prev_left_rpm,
                            -self.config.max_acceleration,
                            self.config.max_acceleration)
        delta_right = np.clip(target_right - self._prev_right_rpm,
                             -self.config.max_acceleration,
                             self.config.max_acceleration)
        
        new_left = int(round(self._prev_left_rpm + delta_left))
        new_right = int(round(self._prev_right_rpm + delta_right))
        
        # Apply low-pass filter
        self._filtered_left_rpm = (self.config.alpha_filter * new_left + 
                                 (1 - self.config.alpha_filter) * self._filtered_left_rpm)
        self._filtered_right_rpm = (self.config.alpha_filter * new_right + 
                                  (1 - self.config.alpha_filter) * self._filtered_right_rpm)
        
        self._prev_left_rpm = int(round(self._filtered_left_rpm))
        self._prev_right_rpm = int(round(self._filtered_right_rpm))

        left_graph = self._prev_left_rpm
        right_graph = self._prev_right_rpm

        # return new_left, new_right
        return left_graph, right_graph

class RobotController:
    """Main robot controller class"""
    def __init__(self, path: np.ndarray, config: Optional[RobotConfig] = None):
        self.config = config or self._default_config()
        self.path = path
        self.current_path_index = 20 # PROBATI DA TO BUDE TACKA KA KOJOJ ROTIRAMOOOOOOOOO
        self.motion_controller = MotionController(self.config)

        self.history_x = []
        self.history_y = []
        self.history_left_rpm = []
        self.history_right_rpm = []
        
        self._setup_motors()
        self._setup_communication()
        self._setup_threads()

    @staticmethod
    def _default_config() -> RobotConfig:
        """Create default robot configuration"""
        return RobotConfig(
            wheel_radius=data.OdometryData.poluprecnik_tocka,
            wheel_base=data.OdometryData.polurastojanje_ose_tockova * 2,
                                                # trajectory_2025_02_11_20_55_17_PUREPURSUIT.png
            max_rpm=3000,                       # 3000
            min_velocity=1000.0,                # 1000.0
            max_velocity=3000.0,                # 3000.0
            min_lookahead=60.0,                 # 60.0
            max_lookahead=90.0,                 # 90.0
            k_lookahead=0.5,                    # 0.5
            k_curvature=50.0,                   # 50.0
            max_acceleration=100,               # 100
            control_delay=0.001,                # 0.001
            alpha_filter=0.5,                   # 0.5
            position_tolerance=1.0 # mm
        )
    # max_v_change

    def _setup_motors(self):
        """Initialize motor controllers"""
        try:
            self.left_motor = MaxonMotor(1, 100000, 50000)
            self.right_motor = MaxonMotor(2, 100000, 50000)
            self.stop_position = False
            print("Motors initialized successfully")
        except Exception as e:
            print(f"Error initializing motors: {e}")
            raise

    def _setup_communication(self):
        """Initialize CAN communication"""
        self.can_comm = CAN_COMM()
        self.can_comm.start()
        # self.can_comm.pos.start()

    def _setup_threads(self):
        """Set up and start control threads"""
        threads = [
            threading.Thread(target=self._motor_control_loop, args=('left',)),
            threading.Thread(target=self._motor_control_loop, args=('right',)),
            # threading.Thread(target=self._position_update_loop)
        ]
        for thread in threads:
            thread.start()

    def _motor_control_loop(self, side: str):
        """Control loop for motor speed updates"""
        motor = self.left_motor if side == 'left' else self.right_motor
        while data.running.is_set() and not self.stop_position:
            speed = (self.motion_controller._prev_left_rpm if side == 'left' 
                    else -self.motion_controller._prev_right_rpm)
            motor.rotate_with_rpm(speed)
            time.sleep(self.config.control_delay)

    # def _position_update_loop(self):
    #     """Update robot position from encoders"""
    #     while data.running.is_set():
    #         self.can_comm.pos.calculate_position()
    #         time.sleep(self.can_comm.pos.delay)

    def find_lookahead_point(self, current_pos: np.ndarray) -> np.ndarray:
        """Find the next target point on the path"""
        distances = np.linalg.norm(
            self.path[self.current_path_index:] - current_pos, 
            axis=1
        )
        
        valid_points = distances >= self.config.min_lookahead
        if np.any(valid_points):
            valid_indices = np.where(valid_points)[0] + self.current_path_index
            closest_index = valid_indices[np.argmin(distances[valid_points])]
            self.current_path_index = closest_index
            return self.path[closest_index]
        return self.path[-1]

    def is_goal_reached(self, current_pos: np.ndarray) -> bool:
        """Check if robot has reached the goal position"""
        if self.current_path_index >= len(self.path) - 1:
            dist = np.linalg.norm(self.path[-1] - current_pos)
            # print(f"U FJI {dist < self.config.position_tolerance}")
            if dist < self.config.position_tolerance:
                print("STIGAOOO SAAAAAAAMMMMMMM")
                print(f"DATA X CURR : {data.x_current} ; DATA Y CURR : {data.y_current}, DATA F CURR {data.f_current} ")
                self.emergency_stop()
                return True
            # else:
            #     print("STIGAO SAM DO KRAJA PUTANJE NISAM USAO U position_tolerance")
            #     print(f"POZICIJA X CURR : {data.x_current}, POZICIJA y CURR : {data.y_current}")
            #     # ovde NE TREBA OVOO - za sad je tu zbog testiranja
            #     self.emergency_stop()
            #     return True
    
    def emergency_stop(self):
        """Emergency stop all motors"""
        try:
            # self.left_motor.rotate_with_rpm(0)
            # self.right_motor.rotate_with_rpm(0)
            speed = self.motion_controller._prev_left_rpm = 0
            speed = self.motion_controller._prev_right_rpm = 0
            print("Emergency stop executed")
        except Exception as e:
            print(f"Error during emergency stop: {e}")

    def normalize_angle(self, angle):
        if angle > 180:
            angle -= 180 * 2
        if angle < - 180:
            angle += 180 * 2
        return angle

    def rotation(self):
        wheel_radius=data.OdometryData.poluprecnik_tocka
        wheel_base=data.OdometryData.polurastojanje_ose_tockova * 2


        # np.deg2rad(2)
        eps_theta = 1   # deg                                
        Kp_w = 8 # 30
        w = 10000
        phi_error = 10000
        print("USAO SAM U ROTATION")

        # proveriti uslove
        # np.abs(w) >= 0.001
        phi = np.rad2deg(np.arctan2(self.path[50][1] - data.y_current, self.path[50][0] - data.x_current))
        print(f"PATH y{self.path[50][1]}, PATH x{self.path[50][0]}")
        print(f"PHIIIIIIIIIIIII {phi}")

        while np.abs(phi_error) >= eps_theta and np.abs(w) >= 0.01:
            # print(type(w), type(wheel_base), type(wheel_radius))
            phi_error = (phi - data.f_current)

            w = Kp_w * phi_error
            print(f"VRTIM WHILE ROTATION F CURRENT {data.f_current}, ABS PHI ERROR {np.abs(phi_error)},  ABS w {np.abs(w)}")

            w_rot = w * wheel_base / (2*wheel_radius)
            w_rot = w_rot
        
            # w_r = w_rot
            # w_l = - w_rot
            # + pa -
            self.motion_controller._smooth_wheel_speeds(-w_rot, w_rot)
            # self.motion_controller._prev_left_rpm = int(round(w_rot))
            # self.motion_controller._prev_right_rpm = int(round(-w_rot))
            print(f"PREV LEFT {self.motion_controller._prev_left_rpm}, PREV RIGHT {self.motion_controller._prev_right_rpm}")
            time.sleep(0.01)
        self.motion_controller._prev_left_rpm = 0
        self.motion_controller._prev_right_rpm = 0
        print(f"POSLE WHILE ROTATION F CURRENT {data.f_current}, ABS PHI ERROR {np.abs(phi_error)},  ABS w {np.abs(w)}")
        print(f"PHIIIIIIIIIIIII {phi}, DATA F CURRENT {data.f_current}")
        print(f"PREV LEFT {self.motion_controller._prev_left_rpm}, PREV RIGHT {self.motion_controller._prev_right_rpm}")

        time.sleep(0.2)
        print(f"DATA F CURR {data.f_current}")



    def main(self):
        """Main control loop"""

        self.rotation()

        while not self.is_goal_reached(np.array([data.x_current, data.y_current])):
            try:
                current_pos = np.array([data.x_current, data.y_current])
                target = self.find_lookahead_point(current_pos)
                
                left_rpm, right_rpm = self.motion_controller.calculate_wheel_speeds(
                    current_pos,
                    np.radians(data.f_current),
                    target
                )

                # Čuvamo istoriju
                self.history_x.append(data.x_current)
                self.history_y.append(data.y_current)
                self.history_left_rpm.append(left_rpm)
                self.history_right_rpm.append(right_rpm)

                # print(f"Wheel speeds - Left: {left_rpm:.2f} RPM, Right: {right_rpm:.2f} RPM")
                # print(f"Data x_current {data.x_current}, Data y_current {data.y_current} \n")
                # print(f"Next point {target}\n")
                time.sleep(0.005) # 0.01
            except KeyboardInterrupt:
                print("\nTrajectory interrupted by user")
                self.emergency_stop()
                break

        print("\nTrajectory interrupted by self.is_goal_reached")
        self.emergency_stop()
        # time.sleep(0.5)
        # self.emergency_stop()




# save_directory: str = "trajectory_plots"
def plot_trajectory_and_speeds(controller: RobotController, save_directory: str = "PurePursuitPlots"):
    plt.figure(figsize=(12, 8))
    
    # Plotovanje putanje
    plt.subplot(2, 1, 1)
    plt.plot(controller.history_x, controller.history_y, label='Robot Path')
    plt.plot(controller.path[:, 0], controller.path[:, 1], 'r--', label='Planned Path')
    plt.xlabel('X Position (mm)')
    plt.ylabel('Y Position (mm)')
    plt.title('Robot Trajectory')
    plt.legend()
    plt.grid(True)
    
    # Plotovanje brzina
    plt.subplot(2, 1, 2)
    plt.plot(controller.history_left_rpm, label='Left Wheel RPM')
    plt.plot(controller.history_right_rpm, label='Right Wheel RPM')
    plt.xlabel('Time Step')
    plt.ylabel('RPM')
    plt.title('Wheel Speeds')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Provera i kreiranje direktorijuma ako ne postoji
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # Generisanje naziva fajla sa vremenskim pečatom
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S") 
    filename = os.path.join(save_directory, f'trajectory_{timestamp}_PUREPURSUIT.png')
    
    # Čuvanje plota
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()  # Zatvaranje figure radi uštede memorije
    
    # Ispisivanje putanje do sačuvanog fajla
    print(f"Plot je sačuvan u: {filename}")
    


if __name__ == "__main__":
        # can_comm = CAN_COMM()
        # can_comm.start()
        # while True:
        #     print(f"POZICIJAAAAAA  -------> DATA X CURR : {data.x_current} ; DATA Y CURR : {data.y_current} ; DATA F CURR {data.f_current}")
        # points = np.array([[data.x_current, data.y_current],[100,100], [400,400], [600,600], [0,700]])

        points = np.array([[data.x_current, data.y_current], [100, 100], [500, 500], [800, 800], [0, 1200]])
        a = BezierPathGenerator()
        waypoints = a.generate_path(points) # vraca np.array

        # waypoints, _ = a.calc_4points_bezier_path(data.x_current, data.y_current, data.f_current, 1000.0, 1000.0, 0.0, 3.0)
        print(f"WAYPOINTS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA {np.size(waypoints)}\n")
        np.set_printoptions(suppress=True, precision=2)
        print(f"{waypoints}\n")
        
    
        controller = RobotController(waypoints)

        data.f_start = 90 # deg
        controller.main()

        plot_trajectory_and_speeds(controller)

        print(f"DATA X CURR {data.x_current} ; DATA Y CURR {data.y_current} ; DATA F CURR {data.f_current}")
