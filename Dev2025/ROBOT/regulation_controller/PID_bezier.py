from typing import Tuple, List, Dict
import time
from ctypes import *
import numpy as np
import sys
import threading
import matplotlib as plt


if __name__ == '__main__':

    import sys
    sys.path.append("..")

import data
from communication.maxon_epos_driver import MaxonMotor
from communication.can_comm import *



def estimate_velocities_rk4(self, x_current: float, y_current: float, theta_current: float) -> Tuple[float, float]:
        """Estimate linear and angular velocities using RK4 method from position data."""
        # Need at least 4 points for RK4
        if len(self.history['x']) < 4:
            return 0.0, 0.0
            
        # Get last 4 positions and current
        x_points = [self.history['x'][-4], self.history['x'][-3], self.history['x'][-2], self.history['x'][-1], x_current]
        y_points = [self.history['y'][-4], self.history['y'][-3], self.history['y'][-2], self.history['y'][-1], y_current]
        theta_points = [self.history['theta'][-4], self.history['theta'][-3], self.history['theta'][-2], self.history['theta'][-1], theta_current]
        
        h = self.dt  # time step
        
        # RK4 slopes for x position
        k1x = (x_points[1] - x_points[0]) / h
        k2x = (x_points[2] - x_points[1]) / h
        k3x = (x_points[3] - x_points[2]) / h
        k4x = (x_points[4] - x_points[3]) / h
        
        # RK4 slopes for y position
        k1y = (y_points[1] - y_points[0]) / h
        k2y = (y_points[2] - y_points[1]) / h
        k3y = (y_points[3] - y_points[2]) / h
        k4y = (y_points[4] - y_points[3]) / h
        
        # RK4 slopes for theta
        k1t = np.arctan2(np.sin(theta_points[1] - theta_points[0]), np.cos(theta_points[1] - theta_points[0])) / h
        k2t = np.arctan2(np.sin(theta_points[2] - theta_points[1]), np.cos(theta_points[2] - theta_points[1])) / h
        k3t = np.arctan2(np.sin(theta_points[3] - theta_points[2]), np.cos(theta_points[3] - theta_points[2])) / h
        k4t = np.arctan2(np.sin(theta_points[4] - theta_points[3]), np.cos(theta_points[4] - theta_points[3])) / h
        
        # Compute velocities using RK4 formula
        dx_dt = (k1x + 2*k2x + 2*k3x + k4x) / 6.0
        dy_dt = (k1y + 2*k2y + 2*k3y + k4y) / 6.0
        dtheta_dt = (k1t + 2*k2t + 2*k3t + k4t) / 6.0
        
        # Calculate linear velocity in robot's frame
        v_global = np.sqrt(dx_dt**2 + dy_dt**2)
        
        # Transform to robot's local frame
        heading = theta_current
        v_local = (dx_dt * np.cos(heading) + dy_dt * np.sin(heading))
        
        # Angular velocity is already in robot's frame
        omega = dtheta_dt
        
        # Apply velocity limits
        v_local = np.clip(v_local, -self.max_linear_velocity, self.max_linear_velocity)
        omega = np.clip(omega, -self.max_angular_velocity, self.max_angular_velocity)
        
        return v_local, omega

def update_state(self, x_current: float, y_current: float, theta_current: float):
    """Update robot's state including velocity estimation."""
    # Update position and orientation
    self.x = x_current
    self.y = y_current
    self.theta = theta_current
    
    # Record in history
    self.history['x'].append(x_current)
    self.history['y'].append(y_current)
    self.history['theta'].append(theta_current)
    
    # Estimate velocities using RK4
    if len(self.history['x']) >= 4:
        self.v, self.omega = self.estimate_velocities_rk4(x_current, y_current, theta_current)
    
    # Record velocities in history
    self.history['v'].append(self.v)
    self.history['omega'].append(self.omega)

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
                 dt=0.01):                # control loop time step
        
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

        self.delay = self.dt
        
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
        
        # Current state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.v = 0.0
        self.omega = 0.0
        
        # Motion limits
        self.max_linear_velocity = 1.5  # m/s
        self.max_angular_velocity = 2.0  # rad/s
        self.max_acceleration = max_acceleration
        self.max_deceleration = max_deceleration
        self.max_angular_acceleration = max_angular_acceleration
        self.max_angular_deceleration = max_angular_deceleration
        
        # Trajectory tracking parameters
        self.goal_tolerance = 0.05  # meters
        self.velocity_threshold = 0.3  # meters

        data.running.set()
        
        # History for debugging and visualization
        self.history = {
            'x': [], 'y': [], 'theta': [],
            'v': [], 'omega': [],
            'rpm_right': [], 'rpm_left': [],
            'linear_error': [], 'angular_error': []
        }

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
            self.maxon_left.rotate_with_rpm(self.rpm_left)
            time.sleep(self.delay)

    def send_vel_right(self):
        while data.running.is_set():
            self.maxon_right.rotate_with_rpm(-self.rpm_right)
            time.sleep(self.delay)

    
    @staticmethod
    def bezier_curve(P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray, 
                     num_points: int = 100) -> np.ndarray:
        """Compute a cubic Bezier curve given four control points."""
        t = np.linspace(0, 1, num_points)[:, np.newaxis]
        return ((1 - t)**3 * P0 + 
                3 * t * (1 - t)**2 * P1 + 
                3 * t**2 * (1 - t) * P2 + 
                t**3 * P3)

    def generate_trajectory(self, start_pos: np.ndarray, target_pos: np.ndarray) -> np.ndarray:
        """Generate Bezier trajectory from start to target position."""
        # Control points for Bezier curve
        P0 = start_pos
        P3 = target_pos
        
        # Calculate control points based on current heading and target
        heading = np.array([np.cos(self.theta), np.sin(self.theta)])
        next_heading = P3 - P0
        next_heading = next_heading / (np.linalg.norm(next_heading) + 1e-6)
        d = min(2.0, np.linalg.norm(P3 - P0) / 3)
        
        P1 = P0 + d * heading
        P2 = P3 - d * next_heading
        
        return self.bezier_curve(P0, P1, P2, P3)
    
    def calculate_pid_velocities(self, target_x: float, target_y: float,
                               x_current: float, y_current: float, 
                               theta_current: float) -> Tuple[float, float]:
        """Calculate desired velocities using PID control."""
        # Calculate errors in robot's frame
        error_x = target_x - x_current
        error_y = target_y - y_current
        
        # Transform errors to robot's local frame
        error_local_x = np.cos(theta_current) * error_x + np.sin(theta_current) * error_y
        error_local_y = -np.sin(theta_current) * error_x + np.cos(theta_current) * error_y
        
        # Calculate desired heading and error
        theta_desired = np.arctan2(error_y, error_x)
        theta_error = theta_desired - theta_current
        theta_error = np.arctan2(np.sin(theta_error), np.cos(theta_error))
        
        # Linear velocity PID
        error_distance = np.sqrt(error_local_x**2 + error_local_y**2)
        error_direction = np.sign(error_local_x)
        
        # Update linear PID terms
        self.linear_integral += error_distance * error_direction * self.dt
        self.linear_integral = np.clip(self.linear_integral, -2.0, 2.0)
        linear_derivative = (error_distance * error_direction - self.linear_prev_error) / self.dt
        
        # Calculate linear velocity
        v_desired = (self.Kp_linear * error_distance * error_direction +
                    self.Ki_linear * self.linear_integral +
                    self.Kd_linear * linear_derivative)
        
        # Scale velocity based on distance to target
        approach_factor = min(1.0, error_distance / self.velocity_threshold)
        v_desired *= approach_factor
        
        # Scale velocity based on heading error
        lateral_error_factor = np.exp(-abs(error_local_y))
        v_desired *= lateral_error_factor
        
        # Angular velocity PID
        self.angular_integral += theta_error * self.dt
        self.angular_integral = np.clip(self.angular_integral, -2.0, 2.0)
        angular_derivative = (theta_error - self.angular_prev_error) / self.dt
        
        # Calculate angular velocity
        omega_desired = (self.Kp_angular * theta_error +
                        self.Ki_angular * self.angular_integral +
                        self.Kd_angular * angular_derivative)
        
        # Update previous errors
        self.linear_prev_error = error_distance * error_direction
        self.angular_prev_error = theta_error
        
        # Apply velocity limits
        v_desired = np.clip(v_desired, -self.max_linear_velocity, self.max_linear_velocity)
        omega_desired = np.clip(omega_desired, -self.max_angular_velocity, self.max_angular_velocity)
        
        return v_desired, omega_desired
    
    def calculate_pid_velocities_with_anti_windup(self, target_x: float, target_y: float,
                                x_current: float, y_current: float, 
                                theta_current: float) -> Tuple[float, float]:
        """Calculate desired velocities using PID control with anti-windup."""
        # Calculate errors in robot's frame
        error_x = target_x - x_current
        error_y = target_y - y_current
        
        # Transform errors to robot's local frame
        error_local_x = np.cos(theta_current) * error_x + np.sin(theta_current) * error_y
        error_local_y = -np.sin(theta_current) * error_x + np.cos(theta_current) * error_y
        
        # Calculate desired heading and error
        theta_desired = np.arctan2(error_y, error_x)
        theta_error = theta_desired - theta_current
        theta_error = np.arctan2(np.sin(theta_error), np.cos(theta_error))
        
        # Linear velocity PID
        error_distance = np.sqrt(error_local_x**2 + error_local_y**2)
        error_direction = np.sign(error_local_x)
        
        # Calculate each PID term separately for linear velocity
        linear_p = self.Kp_linear * error_distance * error_direction
        
        # Calculate current integral term before anti-windup correction
        self.linear_integral += error_distance * error_direction * self.dt
        
        linear_derivative = (error_distance * error_direction - self.linear_prev_error) / self.dt
        linear_d = self.Kd_linear * linear_derivative
        
        # Calculate unconstrained control signal
        v_unconstrained = linear_p + self.Ki_linear * self.linear_integral + linear_d
        
        # Scale velocity based on distance and heading
        approach_factor = min(1.0, error_distance / self.velocity_threshold)
        lateral_error_factor = np.exp(-abs(error_local_y))
        v_unconstrained *= approach_factor * lateral_error_factor
        
        # Apply saturation to get the actual output
        v_desired = np.clip(v_unconstrained, -self.max_linear_velocity, self.max_linear_velocity)
        
        # Anti-windup for linear velocity
        # Calculate the difference between unconstrained and saturated outputs
        linear_windup_error = v_desired - v_unconstrained
        
        # Apply anti-windup correction to integral term
        Kt_linear = 0.1  # Anti-windup tracking time constant
        self.linear_integral += (linear_windup_error / self.Ki_linear) / Kt_linear * self.dt
        
        # Angular velocity PID (similar structure)
        angular_p = self.Kp_angular * theta_error
        
        # Calculate current integral term before anti-windup correction
        self.angular_integral += theta_error * self.dt
        
        angular_derivative = (theta_error - self.angular_prev_error) / self.dt
        angular_d = self.Kd_angular * angular_derivative
        
        # Calculate unconstrained angular control signal
        omega_unconstrained = angular_p + self.Ki_angular * self.angular_integral + angular_d
        
        # Apply saturation to get the actual output
        omega_desired = np.clip(omega_unconstrained, -self.max_angular_velocity, self.max_angular_velocity)
        
        # Anti-windup for angular velocity
        angular_windup_error = omega_desired - omega_unconstrained
        
        # Apply anti-windup correction to integral term
        Kt_angular = 0.1  # Anti-windup tracking time constant
        self.angular_integral += (angular_windup_error / self.Ki_angular) / Kt_angular * self.dt
        
        # Update previous errors
        self.linear_prev_error = error_distance * error_direction
        self.angular_prev_error = theta_error
        
        return v_desired, omega_desired

    def reset_pid_states(self):
        """Reset all PID controller states."""
        self.linear_integral = 0.0
        self.angular_integral = 0.0
        self.linear_prev_error = 0.0
        self.angular_prev_error = 0.0

    def velocities_to_rpm(self, v: float, omega: float) -> Tuple[int, int]:
        """Convert linear and angular velocities to wheel RPM with acceleration limits."""
        # Calculate wheel velocities
        v_right = (v + omega * self.wheel_base / 2)
        v_left = (v - omega * self.wheel_base / 2)
        
        # Get current wheel velocities
        current_rpm_right = self.history['rpm_right'][-1] if self.history['rpm_right'] else 0
        current_rpm_left = self.history['rpm_left'][-1] if self.history['rpm_left'] else 0
        
        # Convert desired velocities to RPM
        desired_rpm_right = int((v_right * 60) / (2 * np.pi * self.wheel_radius) * self.gear_ratio)
        desired_rpm_left = int((v_left * 60) / (2 * np.pi * self.wheel_radius) * self.gear_ratio)
        
        # Calculate maximum RPM change based on acceleration limits
        max_rpm_change = int((self.max_acceleration * 60) / (2 * np.pi * self.wheel_radius) * self.gear_ratio * self.dt)
        
        # Apply acceleration limits
        rpm_right = np.clip(desired_rpm_right, 
                          current_rpm_right - max_rpm_change,
                          current_rpm_right + max_rpm_change)
        rpm_left = np.clip(desired_rpm_left,
                         current_rpm_left - max_rpm_change,
                         current_rpm_left + max_rpm_change)
        
        # Apply RPM limits
        rpm_right = np.clip(rpm_right, -self.max_rpm, self.max_rpm)
        rpm_left = np.clip(rpm_left, -self.max_rpm, self.max_rpm)
        

        print(f"RPM: right: {rpm_right}       left: {rpm_left}")
        return int(rpm_right), int(rpm_left)
        # return int(1000), int(1000)

    def move_to_target(self, target_x: float, target_y: float) -> Dict:
        """Execute trajectory to target position with PID control."""
        print(f"Moving to target: ({target_x}, {target_y})")
        
        try:
            # Generate trajectory
            start_pos = np.array([self.x, self.y])
            target_pos = np.array([target_x, target_y])
            trajectory = self.generate_trajectory(start_pos, target_pos)
            
            target_idx = 0
            max_time = 30.0  # seconds
            start_time = time.time()
            
            while True:
                # Get current state
                x_current = data.x_current / 1000
                y_current = data.y_current / 1000
                theta_current = data.f_current
                
                # Update internal state
                self.x = x_current
                self.y = y_current
                self.theta = theta_current
                
                # Check if goal is reached
                dist_to_goal = np.sqrt((target_x - x_current)**2 + (target_y - y_current)**2)
                if dist_to_goal < self.goal_tolerance:
                    print(f"Goal reached! Final position: ({x_current:.2f}, {y_current:.2f})")
                    self.stop_motors()
                    break
                
                # Check timeout
                if time.time() - start_time > max_time:
                    print("Time limit exceeded!")
                    self.stop_motors()
                    break
                
                # Get current target point from trajectory
                current_target = trajectory[min(target_idx, len(trajectory)-1)]
                
                # Calculate desired velocities using PID
                v_desired, omega_desired = self.calculate_pid_velocities(
                    current_target[0], current_target[1],
                    x_current, y_current, theta_current
                )
                
                # Convert to motor RPM
                rpm_right, rpm_left = self.velocities_to_rpm(v_desired, omega_desired)
                
                # Send commands to motors
                # self.motor_right.rotate_with_rpm(rpm_right)
                # self.motor_left.rotate_with_rpm(rpm_left)

                self.rpm_right = rpm_right
                self.rpm_left = rpm_left
                
                # Record history
                self.history['x'].append(x_current)
                self.history['y'].append(y_current)
                self.history['theta'].append(theta_current)
                self.history['v'].append(v_desired)
                self.history['omega'].append(omega_desired)
                self.history['rpm_right'].append(rpm_right)
                self.history['rpm_left'].append(rpm_left)
                self.history['linear_error'].append(dist_to_goal)
                self.history['angular_error'].append(self.angular_prev_error)
                
                # Move to next trajectory point if close enough
                if np.sqrt((current_target[0] - x_current)**2 + 
                          (current_target[1] - y_current)**2) < 0.1:
                    target_idx = min(target_idx + 1, len(trajectory)-1)
                
                # Control loop timing
                time.sleep(self.dt)
                
        except Exception as e:
            print(f"Error during movement: {e}")
            self.emergency_stop()
            raise
            
        return self.history
    
    def decelerate_to_stop(self, dt):
        """Gradually bring the robot to a stop with controlled deceleration."""
        print("Initiating controlled deceleration...")
        
        try:
            # Get current velocities from history
            current_v = self.history['v'][-1] if self.history['v'] else 0
            current_omega = self.history['omega'][-1] if self.history['omega'] else 0
            
            # Use configured deceleration rates
            decel_rate = self.max_deceleration
            angular_decel_rate = self.max_angular_deceleration
            
            # Calculate time needed to stop
            stop_time = max(
                abs(current_v) / decel_rate if decel_rate > 0 else 0,
                abs(current_omega) / angular_decel_rate if angular_decel_rate > 0 else 0
            )
            
            start_time = time.time()
            while (abs(current_v) > 0.01 or abs(current_omega) > 0.01) and (time.time() - start_time < stop_time + 0.5):
                # Calculate decelerated velocities
                v_decel = np.sign(current_v) * max(0, abs(current_v) - decel_rate * dt)
                omega_decel = np.sign(current_omega) * max(0, abs(current_omega) - angular_decel_rate * dt)
                
                # Convert to wheel RPM
                rpm_right, rpm_left = self.velocities_to_rpm(v_decel, omega_decel)
                
                # Apply to motors
                # self.motor_right.rotate_with_rpm(rpm_right)
                # self.motor_left.rotate_with_rpm(rpm_left)

                self.rpm_right = rpm_right
                self.rpm_left = rpm_left
                
                # Update current velocities
                current_v = v_decel
                current_omega = omega_decel
                
                # Record in history
                self.history['v'].append(v_decel)
                self.history['omega'].append(omega_decel)
                self.history['rpm_right'].append(rpm_right)
                self.history['rpm_left'].append(rpm_left)
                
                time.sleep(dt)
            
            # Final stop
            self.maxon_right.rotate_with_rpm(0)
            self.maxon_left.rotate_with_rpm(0)
            print("Robot successfully stopped")
            
        except Exception as e:
            print(f"Error during deceleration: {e}")
            self.emergency_stop()
            raise

    def stop_motors(self):
        """Stop the motors using controlled deceleration."""
        try:
            # Use controlled deceleration
            self.decelerate_to_stop(self.dt)
        except Exception as e:
            print(f"Error during stop: {e}")
            self.emergency_stop()
    
    def emergency_stop(self):
        """Immediately stop all motors."""
        try:
            self.maxon_right.rotate_with_rpm(0)
            self.maxon_left.rotate_with_rpm(0)
            print("Emergency stop executed")
        except Exception as e:
            print(f"Error during emergency stop: {e}")
    
    def cleanup(self):
        """Cleanup and disable motors."""
        try:
            self.stop_motors()
            self.maxon_right.disable_driver()
            self.maxon_left.disable_driver()
            print("Motors disabled successfully")
        except Exception as e:
            print(f"Error during cleanup: {e}")

    def plot_results(self, history, target_x, target_y):
        """Plot the trajectory tracking results with errors."""
        plt.figure(figsize=(15, 10))
        
        # Trajectory plot
        plt.subplot(2, 2, 1)
        # Plot desired trajectory
        plt.plot(history['desired_x'], history['desired_y'], '--b', label='Desired Path')
        # Plot actual path
        plt.plot(history['x'], history['y'], '-r', label='Robot Path')
        # Plot start, target and control points
        plt.plot(target_x, target_y, 'r*', label='Target')
        plt.plot(self.x, self.y, 'go', label='Start')
        control_points = history['control_points']
        plt.scatter([p[0] for p in control_points], [p[1] for p in control_points], 
                    color='gray', label='Control Points')
        for i, p in enumerate(control_points):
            plt.annotate(f'P{i}', p, textcoords="offset points", xytext=(5, 5))
        
        plt.grid(True)
        plt.legend()
        plt.title('Robot Trajectory')
        plt.axis('equal')
        
        # Velocities plot
        plt.subplot(2, 2, 2)
        plt.plot(history['v'], label='Linear Velocity')
        plt.plot(history['omega'], label='Angular Velocity')
        plt.grid(True)
        plt.legend()
        plt.title('Robot Velocities')
        
        # Control torques plot
        plt.subplot(2, 2, 3)
        plt.plot(history['tau_r'], label='Right Wheel Torque')
        plt.plot(history['tau_l'], label='Left Wheel Torque')
        plt.grid(True)
        plt.legend()
        plt.title('Control Torques')
        
        # Tracking errors plot
        plt.subplot(2, 2, 4)
        plt.plot(history['linear_error'], label='Linear Error')
        plt.plot(history['angular_error'], label='Angular Error')
        plt.grid(True)
        plt.legend()
        plt.title('Tracking Errors')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    
    # Initialize robot controller with tuned gains
    robot = RealRobotController(
        wheel_radius=2*0.03572,    # Adjust to your robot's dimensions
        wheel_base= 2*0.152,      # Distance between wheels
        max_rpm=11000,        # Maximum motor RPM
        gear_ratio=16.0,      # If you have gear reduction
        # PID gains - tune these based on your robot's behavior
        Kp_linear=10.0,
        Ki_linear=0.5,
        Kd_linear=0.0,
        Kp_angular=0.0,
        Ki_angular=0.0,
        Kd_angular=0.0,
        dt=0.01              # Control loop time step
    )
    
    # Main control loop

    try:
        # Get target position
        target_x = 1.0
        target_y = 1.5
        
        # Move to target
        history = robot.move_to_target(target_x, target_y)
        robot.plot_results(history, target_x, target_y)

    except KeyboardInterrupt:
        print("\nTrajectory interrupted by user")
        robot.stop_motors()
        # robot.plot_results(history, target_x, target_y)
                
