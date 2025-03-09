import math
from typing import Tuple, List, Dict
import time
from ctypes import *
import numpy as np
import sys
import threading
import matplotlib as plt
import os
import scipy.special

if __name__ == '__main__':

    import sys
    sys.path.append("..")
    
import data
from communication.maxon_epos_driver import MaxonMotor
from communication.can_comm import *


class CurveGenerator:
# SPAJA TACKE za sad...
# region
    @staticmethod
    # prakticno samo spaja tacke
    def generate_curve(points: np.ndarray, tip = 'bezivica') -> Dict:
        # 'bezivica'
        # 'saivicama'
        """Generate curve through multiple points."""
        if len(points) < 2:
            raise ValueError("Need at least 2 points")
        
        trajectory = CurveGenerator.generate_trajectory(points, tip)
        return trajectory
       
    @staticmethod
    def generate_trajectory(points: np.ndarray, tip) -> np.ndarray:
        """Generate smooth curve through multiple points."""
        num_segments = len(points) - 1
        curves = []
        
        for i in range(num_segments):
            P0 = points[i]
            P3 = points[i + 1]
            
            # Calculate control points
            if i == 0:
                heading = P3 - P0
            else:
                heading = points[i] - points[i-1]
            
            if i == num_segments - 1:
                next_heading = P3 - P0
            else:
                next_heading = points[i+2] - points[i+1]
            
            heading = heading / (np.linalg.norm(heading) + 1e-6)
            next_heading = next_heading / (np.linalg.norm(next_heading) + 1e-6)
            

            if tip == 'saivicama':
                d = min(2.0, np.linalg.norm(P3 - P0) / 3)
                P1 = P0 + d * heading
                P2 = P3 - d * next_heading
            elif tip == 'bezivica':
                d = np.linalg.norm(P3 - P0) / 3.0
                P1 = P0 + d * heading
                P2 = P3 - d * next_heading

            segment = CurveGenerator.bezier_curve(P0, P1, P2, P3, num_points=5)
            curves.append(segment)
        
        return np.vstack(curves)
    
    @staticmethod
    def bezier_curve(P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray, 
                     num_points: int = 50) -> np.ndarray:
        """Compute cubic Bezier curve segment."""
        t = np.linspace(0, 1, num_points)[:, np.newaxis]
        return ((1 - t)**3 * P0 + 
                3 * t * (1 - t)**2 * P1 + 
                3 * t**2 * (1 - t) * P2 + 
                t**3 * P3)
# endregion


# GENERISE KRIVU
# Veći offset: Kontrolne tačke će biti bliže početnoj i krajnjoj tački → Kriva postaje oštrija i više lokalizovana.
# Manji offset: Kontrolne tačke će biti dalje → Kriva postaje mekša i duže se "proteže".
# offset = 1.0 # 3.0
# 1 nacin
# path, control_points = calc_4points_bezier_path(
#     start_x, start_y, start_yaw, end_x, end_y, end_yaw, offset)
# 2 nacin
# control_points = np.array([[start_x,start_y], [500,100], [500,500], [end_x,end_y]])
# path = calc_bezier_path(control_points, n_points=100)
# region
    # zapravo generise krivu
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

        path = CurveGenerator.calc_bezier_path(control_points, n_points=100)

        return path, control_points

    @staticmethod
    def calc_bezier_path(control_points, n_points=100):
        """
        Compute bezier path (trajectory) given control points.

        :param control_points: (numpy array)
        :param n_points: (int) number of points in the trajectory
        :return: (numpy array)
        """
        traj = []
        for t in np.linspace(0, 1, n_points):
            traj.append(CurveGenerator.bezier(t, control_points))

        return np.array(traj)
    
    @staticmethod
    def bezier(t, control_points):
        """
        Return one point on the bezier curve.

        :param t: (float) number in [0, 1]
        :param control_points: (numpy array)
        :return: (numpy array) Coordinates of the point
        """
        n = len(control_points) - 1
        return np.sum([CurveGenerator.bernstein_poly(n, i, t) * control_points[i] for i in range(n + 1)], axis=0)

    @staticmethod
    def bernstein_poly(n, i, t):
        """
        Bernstein polynom.

        :param n: (int) polynom degree
        :param i: (int)
        :param t: (float)
        :return: (float)
        """
        return scipy.special.comb(n, i) * t ** i * (1 - t) ** (n - i)

# endregion


class RealRobotController:
    def __init__(self, 
                 wheel_radius=0.1,        # meters
                 wheel_base=0.5,          # meters
                 max_rpm=3000,            # maximum RPM for Maxon motors
                 gear_ratio=16.0,          # motor gear reduction ratio
                 # PID gains
                 Kp_linear=15.0,
                 Ki_linear=5.5,
                 Kd_linear=0.0,
                 Kp_angular=10.0,
                 Ki_angular=0.0,
                 Kd_angular=100.0,
                 # Motion control parameters
                 max_acceleration=3.0,     # m/s²
                 max_deceleration=2.5,     # m/s²
                 max_angular_acceleration=2.0,  # rad/s²
                 max_angular_deceleration=1.0,  # rad/s²
                 goal_tolerance = 0.01,  
                 max_linear_velocity = 1.5,
                 max_angular_velocity = 2.0,
                 velocity_threshold = 0.5,
                 dt=0.01):  
        
        self.wheel_radius = wheel_radius
        self.wheel_base = wheel_base
        self.max_rpm = max_rpm
        self.gear_ratio = gear_ratio
        self.dt = dt
        
        # PID gains
        self.Kp_linear = Kp_linear
        self.Ki_linear = Ki_linear
        self.Kd_linear = Kd_linear
        self.Kp_angular = Kp_angular
        self.Ki_angular = Ki_angular
        self.Kd_angular = Kd_angular
        
        # PID error terms
        self.linear_integral = 0.0
        self.angular_integral = 0.0
        self.linear_prev_error = 0.0
        self.angular_prev_error = 0.0

        self.rpm_right = 0
        self.rpm_left = 0

        self.delay = 0.005

        self.MVL = 0
        self.MVR = 0

        # Ostatak inicijalizacije
        self.POJACAJ = 300
        self.current_linear_velocity = 0.0  # Trenutna linearna brzina
        self.current_angular_velocity = 0.0  # Trenutna uglovna brzina
        self.max_linear_velocity = max_linear_velocity  # Maksimalna linearna brzina
        self.max_angular_velocity = max_angular_velocity  # Maksimalna uglovna brzina
        self.max_acceleration = max_acceleration  # Maksimalna akceleracija
        self.max_deceleration = max_deceleration  # Maksimalna dekoeleracija
        self.max_angular_acceleration = max_angular_acceleration
        self.max_angular_deceleration = max_angular_deceleration


        # Initialize Maxon motors
        try:

            self.maxon_left = MaxonMotor(1, 100000, 50000)
            self.maxon_right = MaxonMotor(2, 100000, 50000)

            self.stop_position = False

            print("position")
            # I2i P1p
            self.can_communication = CAN_COMM()
            speed_thread1 = threading.Thread(target=self.send_vel_left)
            speed_thread1.start()
            speed_thread2 = threading.Thread(target=self.send_vel_right)
            speed_thread2.start()

            print("Motors initialized successfully")
        except Exception as e:
            print(f"Error initializing motors: {e}")
            raise

        #Init encoders
        self.init_odom()



        self.vr_prev = 0 


        """
        Ključni parametri za podešavanje:

        -->Look-ahead parametri:
        look_ahead_min: 100-200mm
        look_ahead_max: 300-500mm
        k_look_ahead: 0.2-0.4


        -->PID parametri:
        kp_angular: 0.6-1.0
        ki_angular: 0.01-0.05
        kd_angular: 0.05-0.15


        -->Brzinski parametri:
        k_velocity: 0.3-0.7
        min_velocity: 50-100mm/s

        -->TOK PODESAVANJA: 
        Prvo podesiti look_ahead parametre
        Zatim PID parametre
        Na kraju brzinske parametr
        """
        self.velocity_change_rate = 0.01

        self.max_linear_velocity = 500  # mm/s
        self.max_angular_velocity = 1.5  # rad/s
        # self.max_acceleration = 200  # mm/s^2
        # self.max_angular_acceleration = 1.0  # rad/s^2
        self.dt = 0.05  # seconds
        
        # Pure Pursuit parametri
        # small look ahead -> osc ;  too big look ahead -> slow poor tracking
        self.old_nearest_point_index = None
        self.look_ahead = 200
        self.look_ahead_min = 100  # 100 mm
        self.look_ahead_max = 200  # 300 mm
        self.k_look_ahead = 0.2  # Faktor za dinamički look_ahead
        
        # PID parametri za ugaono upravljanje
        self.kp_angular = 0.5 # 0.5
        self.ki_angular = 0.05 # 0.05
        self.kd_angular = 0.00 # 0.1
        self.angular_error_sum = 0
        self.last_angular_error = 0
        
        # Parametri brzine
        self.k_velocity = 0.3  # Faktor smanjenja brzine u krivinama
        self.min_velocity = 50  # Minimalna brzina
        self.current_linear_velocity = 0
        self.current_angular_velocity = 0
        
        # Parametri praćenja
        self.waypoint_tolerance = 30 # 20 # mm
        self.curve_sharpness_threshold = math.pi/4  # rad

    def init_odom(self):
        self.can_communication = CAN_COMM()
        self.can_communication.start()
        self.can_communication.pos.start()

        position_thread = threading.Thread(target=self.get_position)
        position_thread.start()

    def get_position(self):

        while data.running.is_set():
            self.can_communication.pos.calculate_position()
            time.sleep(self.can_communication.pos.delay)

    def send_vel_left(self):
        while data.running.is_set():
            if not self.stop_position:
                self.maxon_left.rotate_with_rpm(self.MVL)
                # print(f"Vreme1 VEL LEFT: {time.time()}")
                time.sleep(self.delay)

    def send_vel_right(self):
        while data.running.is_set():
            if not self.stop_position:
                self.maxon_right.rotate_with_rpm(-self.MVR)
                # print(f"Vreme2 VEL RIGHT: {time.time()}")
                time.sleep(self.delay)

    def emergency_stop(self):
        """Immediately stop all motors."""
        try:
            self.maxon_right.rotate_with_rpm(0)
            self.maxon_left.rotate_with_rpm(0)
            print("Emergency stop executed")
        except Exception as e:
            print(f"Error during emergency stop: {e}")




    def is_within_workspace(self, x, y):
        return (0 <= x <= self.max_x) and (0 <= y <= self.max_y)
    
    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    



    # def smooth_velocity_change(self, target_linear_velocity, target_angular_velocity):
    #     """
    #     Postepeno menja brzinu robota kako bi izbegao naglo ubrzanje i kočenje.
    #     """
    #     # Postepeno promeni linearne brzine
    #     linear_velocity_difference = target_linear_velocity - self.current_linear_velocity
    #     if abs(linear_velocity_difference) > self.max_acceleration * self.dt:
    #         linear_velocity_difference = self.max_acceleration * self.dt * np.sign(linear_velocity_difference)
    #     self.current_linear_velocity += linear_velocity_difference

    #     # Postepeno promeni uglovnu brzinu
    #     angular_velocity_difference = target_angular_velocity - self.current_angular_velocity
    #     if abs(angular_velocity_difference) > self.max_angular_acceleration * self.dt:
    #         angular_velocity_difference = self.max_angular_acceleration * self.dt * np.sign(angular_velocity_difference)
    #     self.current_angular_velocity += angular_velocity_difference

    #     # Ograničavanje brzina na maksimalne vrednosti
    #     self.current_linear_velocity = max(min(self.current_linear_velocity, self.max_linear_velocity), -self.max_linear_velocity)
    #     self.current_angular_velocity = max(min(self.current_angular_velocity, self.max_angular_velocity), -self.max_angular_velocity)
    

    
    # def pure_pursuit_control(self, goal_x, goal_y, look_ahead_distance = 200):
    #     """
    #     Pure Pursuit algoritam za navigaciju do cilja
    #     """
    #     dx = goal_x - data.x_current
    #     dy = goal_y - data.y_current
        
    #     distance_to_goal = self.calculate_distance(data.x_current, data.y_current, goal_x, goal_y)
    #     goal_angle = math.atan2(dy, dx)
        
    #     angle_error = goal_angle - data.f_current
    #     angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))
        
    #     linear_speed = min(distance_to_goal, self.max_linear_velocity)  # Maksimalna brzina na osnovu rastojanja
    #     angular_speed = max(min(angle_error, self.max_angular_velocity), -self.max_angular_velocity)  # Maksimalna brzina okretanja

    #     # Postepeno menjaj brzinu
    #     self.smooth_velocity_change(linear_speed, angular_speed)

    #     # Računanje brzine za motore
    #     self.MVL = int(self.current_linear_velocity - self.current_angular_velocity) * self.POJACAJ
    #     self.MVR = int(self.current_linear_velocity + self.current_angular_velocity) * self.POJACAJ

    #     return self.MVL, self.MVR


    # def navigate_waypoints(self, waypoints, look_ahead_distance = 100, tolerance = 20):
    #     """
    #     Navigacija kroz niz tačaka koristeći Pure Pursuit algoritam
    #     """
    #     for goal_x, goal_y in waypoints:

    #         while self.calculate_distance(data.x_current, data.y_current, goal_x, goal_y) > tolerance:
    #             # Koristi Pure Pursuit kontrolu da izračuna brzinu
    #             self.MVL, self.MVR = self.pure_pursuit_control(goal_x, goal_y, look_ahead_distance)
    #             # print(f"MVL: {self.MVL}, MVR: {self.MVR}")
    #             vr = time.time()                    
    #             if vr - self.vr_prev > 0.25:
    #                 self.vr_prev = vr
    #                 print(f"CURR X {data.x_current}, CURR Y {data.y_current}")


    def smooth_velocity_change(self, target_velocity, angular_velocity):
        """Postepena promena brzine kako bi se izbegle nagle promene"""
        velocity_step = self.velocity_change_rate * self.dt
        self.current_linear_velocity += np.clip(target_velocity - self.current_linear_velocity, 
                                                -velocity_step, velocity_step)
        self.current_angular_velocity = angular_velocity
                    
    def adjust_look_ahead(self, curve_sharpness, current_velocity):
        """Dinamički podešava look_ahead distancu na osnovu oštrine krivine i brzine"""
        base_look_ahead = self.look_ahead_min + (self.look_ahead_max - self.look_ahead_min) * \
                         (current_velocity / self.max_linear_velocity)
        curve_factor = math.exp(-self.k_look_ahead * abs(curve_sharpness))
        return base_look_ahead * curve_factor
    
    def calculate_curve_sharpness(self, current_point, next_point, future_point):
        """Računa oštrinu krivine na osnovu tri tačke"""
        # # if not all([current_point, next_point, future_point]):
        # #     return 0
        # if current_point is None or next_point is None or future_point is None:
        #     return 0
       
        # angle1 = math.atan2(next_point[1] - current_point[1], 
        #                    next_point[0] - current_point[0])
        # angle2 = math.atan2(future_point[1] - next_point[1], 
        #                    future_point[0] - next_point[0])
        # return abs(angle2 - angle1)
        for point in [current_point, next_point, future_point]:
            if point is None or len(point) != 2:
                return 0

        angle1 = math.atan2(next_point[1] - current_point[1], 
                            next_point[0] - current_point[0])
        angle2 = math.atan2(future_point[1] - next_point[1], 
                            future_point[0] - next_point[0])
        return abs(angle2 - angle1)
    
    def calculate_target_velocity(self, curve_sharpness, distance_to_goal):
        """Računa ciljnu brzinu na osnovu oštrine krivine i udaljenosti od cilja"""
        curve_velocity = self.max_linear_velocity * math.exp(-self.k_velocity * curve_sharpness)
        approach_velocity = min(distance_to_goal, self.max_linear_velocity)
        target_velocity = min(curve_velocity, approach_velocity)
        return max(target_velocity, self.min_velocity)
    
    def pid_angular_control(self, angle_error):
        """PID kontroler za ugaonu brzinu"""
        self.angular_error_sum += angle_error * self.dt
        angular_error_rate = (angle_error - self.last_angular_error) / self.dt
        
        control = (self.kp_angular * angle_error + 
                  self.ki_angular * self.angular_error_sum +
                  self.kd_angular * angular_error_rate)
        
        self.last_angular_error = angle_error
        return min(max(control, -self.max_angular_velocity), self.max_angular_velocity)

    def find_look_ahead_point(self, path, look_ahead_distance):
        #"""Pronalazi look_ahead tačku na putanji"""
        # for i in range(len(path) - 1):
        #     p1 = path[i]
        #     p2 = path[i + 1]
            
        #     # Implementacija geometrijskog preseka kružnice i linije
        #     # za pronalaženje look_ahead tačke
            
        #     # Return najbližu tačku ako nema preseka
        #     return p2  # Pojednostavljena verzija

        """Pronalazi look_ahead tačku na putanji koristeći preseke"""
        for i in range(len(path) - 1):
            p1 = np.array(path[i])
            p2 = np.array(path[i + 1])
            
            # Pravac linije
            d = p2 - p1
            d_norm = np.linalg.norm(d)
            if d_norm == 0:
                continue  # Preskoči degenerate segmente
            
            d = d / d_norm  # Jedinični vektor
            f = np.array([data.x_current, data.y_current]) - p1
            
            # Koeficijenti kvadratne jednačine (|f + t*d| = look_ahead_distance)
            a = np.dot(d, d)
            b = 2 * np.dot(f, d)
            c = np.dot(f, f) - look_ahead_distance**2
            
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                continue  # Nema preseka
            
            discriminant = math.sqrt(discriminant)
            t1 = (-b - discriminant) / (2*a)
            t2 = (-b + discriminant) / (2*a)
            
            # Provera validnih t vrednosti (unutar segmenta)
            if 0 <= t1 <= 1:
                return p1 + t1 * d
            if 0 <= t2 <= 1:
                return p1 + t2 * d
        
        # Ako nema preseka, vrati poslednju tačku
        return path[-1]

    def pure_pursuit_control(self, path_points, current_index):
        """Unapređeni Pure Pursuit kontroler sa dinamičkim podešavanjem parametara"""

        if path_points is None or len(path_points) < 2:
            raise ValueError("Path mora sadržati bar dve tačke.")
        
        if current_index >= len(path_points):
            raise ValueError("Trenutni indeks je van opsega putanje.")


        current_pos = (data.x_current, data.y_current)
        next_point = path_points[min(current_index + 1, len(path_points) - 1)]
        future_point = path_points[min(current_index + 2, len(path_points) - 1)]
        
        curve_sharpness = self.calculate_curve_sharpness(current_pos, next_point, future_point)
        look_ahead = self.adjust_look_ahead(curve_sharpness, self.current_linear_velocity)
        
        # Pronalaženje look_ahead tačke na putanji
        target_point = self.find_look_ahead_point(path_points[current_index:], look_ahead)
        
        dx = target_point[0] - data.x_current
        dy = target_point[1] - data.y_current
        
        target_angle = math.atan2(dy, dx)
        angle_error = math.atan2(math.sin(target_angle - data.f_current),
                                math.cos(target_angle - data.f_current))
        
        distance_to_goal = math.hypot(dx, dy)
        target_velocity = self.calculate_target_velocity(curve_sharpness, distance_to_goal)
        angular_velocity = self.pid_angular_control(angle_error)
        
        self.smooth_velocity_change(target_velocity, angular_velocity)
        
        # Konverzija u komande za motore
        self.MVR = int((self.current_linear_velocity + self.current_angular_velocity) * self.POJACAJ)
        self.MVL = int((self.current_linear_velocity - self.current_angular_velocity) * self.POJACAJ)


    def go_curve(self, path):

        current_index = 0
        try:
            while current_index < len(path) - 1:
                start_time = time.time()
                
                self.pure_pursuit_control(path, current_index)
                
                # Ažuriranje trenutnog indeksa na putanji
                if self.calculate_distance(data.x_current, data.y_current, 
                                        path[current_index][0], path[current_index][1]) < robot.waypoint_tolerance:
                    current_index += 1
                else:
                # Proveri stagnaciju
                    stagnation_threshold = 0.5  # Sekunde bez napretka
                    if time.time() - start_time > stagnation_threshold:
                        raise RuntimeError("Robot ne napreduje prema cilju!")
                    
                # Održavanje konstantnog vremena ciklusa
                elapsed = time.time() - start_time
                if elapsed < robot.dt:
                    time.sleep(robot.dt - elapsed)

        except KeyboardInterrupt:
            self.MVL = 0
            self.MVR = 0





    def search_target_index(self, waypoints):
        # Traži indeks najbliže tačke
        if self.old_nearest_point_index is None:
            dx = data.x_current - waypoints[:, 0]
            dy = data.y_current - waypoints[:, 1]
            d = np.hypot(dx, dy)
            ind = np.argmin(d)
            self.old_nearest_point_index = ind
        else:
            ind = self.old_nearest_point_index
            distance_this_index = self.calc_distance(waypoints[ind][0], waypoints[ind][1])
            while True:
                distance_next_index = self.calc_distance(waypoints[ind + 1][0], waypoints[ind + 1][1])
                if distance_this_index < distance_next_index:
                    break
                ind = ind + 1 if (ind + 1) < len(waypoints) else ind
                distance_this_index = distance_next_index
            self.old_nearest_point_index = ind

        Lf = self.k_look_ahead * data.f_current + self.look_ahead  # Ažuriramo udaljenost za gledanje unapred

        # Traži ciljnu tačku u zavisnosti od Lf
        while Lf > self.calc_distance(waypoints[ind][0], waypoints[ind][1]):
            if (ind + 1) >= len(waypoints):
                break  # Ne prelazi cilj
            ind += 1
        
        self.old_nearest_point_index = None

        return ind, Lf


    def pure_pursuit_steer_control(self, waypoints, pind):
        ind, Lf = self.search_target_index(waypoints)

        if pind >= ind:
            ind = pind

        # waypoints numpy niz parova x,y
        if ind < len(waypoints):
            tx = waypoints[ind][0]
            ty = waypoints[ind][1]
        else:  # toward goal
            tx = waypoints[-1][0]
            ty = waypoints[-1][1]
            ind = len(waypoints) - 1

        alpha = math.atan2(ty - data.y_current, tx - data.x_current) - data.f_current

        delta = math.atan2(2.0 * data.OdometryData.polurastojanje_ose_tockova * 2 * math.sin(alpha) / Lf, 1.0)

        self.current_angular_velocity += self.current_linear_velocity / data.OdometryData.polurastojanje_ose_tockova * 2. * math.tan(delta) * self.dt

        return ind


    def update(self, a):
        if self.current_linear_velocity < self.max_linear_velocity:
            self.current_linear_velocity += a * self.dt
        else:
            self.current_linear_velocity = self.max_linear_velocity

        # MVR_rad_s = (self.MVR * 2 * math.pi) / 60
        # MVL_rad_s = (self.MVL * 2 * math.pi) / 60
        # self.current_angular_velocity = (data.OdometryData.poluprecnik_tocka * (MVR_rad_s - MVL_rad_s)) / (2 * data.OdometryData.polurastojanje_ose_tockova)
        
        self.MVL = int(self.current_linear_velocity - self.current_angular_velocity)
        self.MVR = int(self.current_linear_velocity + self.current_angular_velocity)
        print(f"CURR LINEAR {self.current_linear_velocity} \n")
        print(f"CURR ANGULAR {self.current_angular_velocity} \n")
        print(f"NOVI MVR {self.MVR} \n")
        print(f"NOVI MVL {self.MVL} \n")
        print(f"CURR X CURRENT {data.x_current} \n")
        print(f"NOVI Y CURRENT {data.y_current} \n")
        print(f"NOVI F CURRENT {data.f_current} \n")        

    def calc_distance(self, point_x, point_y):
        dx = data.x_current - point_x
        dy = data.y_current - point_y
        return math.hypot(dx, dy)

    def proportional_control(self, target, current):
        a = self.Kp_linear * (target - current)
        return a




if __name__ == "__main__":

    try:
        robot = RealRobotController(
            wheel_radius=2*0.03572,    # Adjust to your robot's dimensions
            wheel_base= 2*0.152,      # Distance between wheels
            max_rpm=11000,        # Maximum motor RPM
            gear_ratio=16.0,      # If you have gear reduction
            # PID gains - tune these based on your robot's behavior
            Kp_linear=10.0, # 310.0
            Ki_linear=5.5,
            Kd_linear=4.0,
            Kp_angular=2.5,
            Ki_angular=0.5,
            Kd_angular=0.0,
            max_acceleration=16.0,     # m/s²
            max_deceleration=3.5,     # m/s²
            max_angular_acceleration=2.0,  # rad/s²
            max_angular_deceleration=1.0,  # rad/s²
            dt=0.01,              # Control loop time step
        )
        

        # points = np.array([[data.x_current, data.y_current],[100,100], [300,300], [300,800], [1000,1500]])
        # waypoints = CurveGenerator.generate_curve(points) # vraca np.array

        # FLOAT 
        start_x = data.x_current
        start_y = data.y_current
        start_yaw = np.radians(data.f_current)

        end_x = 100.0
        end_y = 600.0
        end_yaw = np.radians(-45.0)
        # Veći offset: Kontrolne tačke će biti bliže početnoj i krajnjoj tački → Kriva postaje oštrija i više lokalizovana.
        # Manji offset: Kontrolne tačke će biti dalje → Kriva postaje mekša i duže se "proteže".
        offset = 1.0 # 3.0

        waypoints, _ = CurveGenerator.calc_4points_bezier_path(
        start_x, start_y, start_yaw, end_x, end_y, end_yaw, offset)
        print(f"WAYPOINTS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA {np.size(waypoints)}\n")
        np.set_printoptions(suppress=True, precision=2)
        print(f"{waypoints}\n")
        # robot.navigate_waypoints(waypoints)
        # robot.go_curve(waypoints)

        lastIndex = len(waypoints) - 1
        target_speed = 150.0  # [mm/s]
        target_ind, _ = robot.search_target_index(waypoints)

        while lastIndex > target_ind:
            ai = robot.proportional_control(target_speed, robot.current_linear_velocity)
            target_ind = robot.pure_pursuit_steer_control(waypoints, target_ind)
            robot.update(ai)  # Control vehicle

    except KeyboardInterrupt:
        print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALOOOOOOOOOOOOOOOOO F CURRENT {data.f_current}")
        print("\nTrajectory interrupted by user")
        robot.emergency_stop()

