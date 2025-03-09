import datetime
from typing import Tuple, List, Dict
import time
from ctypes import *
import numpy as np
import sys
import threading
import matplotlib as plt
import os


if __name__ == '__main__':

    import sys
    sys.path.append("..")

import data
from communication.maxon_epos_driver import MaxonMotor
from communication.can_comm import *

import matplotlib.pyplot as plt
from matplotlib import use as mpl_use
try:
    mpl_use('TkAgg')  # Try to use TkAgg backend
except:
    pass

class PlotManager:
    def __init__(self, save_dir='trajectory_plots'):
        """Initialize PlotManager with a directory for saving plots."""
        self.plotting_enabled = False
        try:
            self.plt = plt
            self.plotting_enabled = True
            
            # Create directory for saving plots
            self.save_dir = save_dir
            os.makedirs(self.save_dir, exist_ok=True)
            
            # Create a unique subdirectory for this run
            timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            self.run_dir = os.path.join(self.save_dir, f'run_{timestamp}')
            os.makedirs(self.run_dir, exist_ok=True)
            
            print(f"Plots will be saved to: {self.run_dir}")
            
        except Exception as e:
            print(f"Warning: Could not initialize plotting: {e}")
            self.plotting_enabled = False
    
    def plot_current_state(self, robot, trajectory, target_x, target_y, iteration=0):
        """Save current state plot to a file."""
        if not self.plotting_enabled:
            return
        
        try:
            # Create new figure (don't use previous one since we're saving to file)
            plt.figure(figsize=(10, 10))
            
            # Plot planned trajectory
            plt.plot(trajectory[:, 0], trajectory[:, 1], '--b', label='Planned Path')
            
            # Plot actual path from history
            if len(robot.history['x']) > 0:
                plt.plot(robot.history['x'], robot.history['y'], '-r', label='Actual Path')
            
            # Plot start and target points
            plt.plot(robot.x, robot.y, 'go', label='Start')
            plt.plot(target_x, target_y, 'r*', label='Target')
            
            # Plot current position
            if len(robot.history['x']) > 0:
                plt.plot(robot.history['x'][-1], robot.history['y'][-1], 'mo', 
                        label='Current Position')
                
                # Add robot orientation arrow
                current_x = robot.history['x'][-1]
                current_y = robot.history['y'][-1]
                current_theta = robot.history['theta'][-1]
                arrow_length = 0.2  # meters
                dx = arrow_length * np.cos(current_theta)
                dy = arrow_length * np.sin(current_theta)
                plt.arrow(current_x, current_y, dx, dy, 
                         head_width=0.05, head_length=0.1, fc='g', ec='g')
            
            plt.grid(True)
            plt.legend()
            plt.title(f'Robot Trajectory Tracking - Step {iteration}')
            plt.xlabel('X (meters)')
            plt.ylabel('Y (meters)')
            plt.axis('equal')
            
            # Save the plot
            filename = os.path.join(self.run_dir, f'trajectory_{iteration:04d}.png')
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()  # Close the figure to free memory
            
            print(f"Saved plot to: {filename}")
            
            # If this is not the first plot, create additional plots for analysis
            if len(robot.history['x']) > 1:
                self.plot_analysis(robot, iteration)
                
        except Exception as e:
            print(f"Warning: Could not save plot: {e}")
    
    def plot_analysis(self, robot, iteration):
        """Create and save analysis plots."""
        try:
            # Create a figure with 2x2 subplots
            plt.figure(figsize=(15, 15))
            
            # Plot velocities
            plt.subplot(2, 2, 1)
            plt.plot(robot.history['v'], label='Linear Velocity (m/s)')
            plt.plot(robot.history['omega'], label='Angular Velocity (rad/s)')
            plt.grid(True)
            plt.legend()
            plt.title('Robot Velocities')
            
            # Plot RPM
            plt.subplot(2, 2, 2)
            plt.plot(robot.history['rpm_right'], label='Right Wheel RPM')
            plt.plot(robot.history['rpm_left'], label='Left Wheel RPM')
            plt.grid(True)
            plt.legend()
            plt.title('Wheel RPM')
            
            # Plot errors
            plt.subplot(2, 2, 3)
            plt.plot(robot.history['linear_error'], label='Distance to Goal (m)')
            plt.grid(True)
            plt.legend()
            plt.title('Distance Error')
            
            # Plot angular error
            plt.subplot(2, 2, 4)
            plt.plot(robot.history['angular_error'], label='Angular Error (rad)')
            plt.grid(True)
            plt.legend()
            plt.title('Angular Error')
            
            # Save the analysis plot
            filename = os.path.join(self.run_dir, f'analysis_{iteration:04d}.png')
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()
            
            print(f"Saved analysis plot to: {filename}")
            
        except Exception as e:
            print(f"Warning: Could not save analysis plot: {e}")
    
    def cleanup(self):
        """Clean up resources."""
        if not self.plotting_enabled:
            return
        try:
            plt.close('all')
        except:
            pass


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

        self.delay = 0.005
        
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
        self.max_linear_velocity = max_linear_velocity  # m/s
        self.max_angular_velocity = max_angular_velocity  # rad/s
        self.max_acceleration = max_acceleration
        self.max_deceleration = max_deceleration
        self.max_angular_acceleration = max_angular_acceleration
        self.max_angular_deceleration = max_angular_deceleration
        
        # Trajectory tracking parameters
        self.goal_tolerance = goal_tolerance  # meters
        self.velocity_threshold = velocity_threshold # meters

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

    # Analysis of Velocity Control Issues and Recommended Solutions

    def improved_calculate_pid_velocities(self, target_x: float, target_y: float, target_theta: float,
                                x_current: float, y_current: float, 
                                theta_current: float) -> Tuple[float, float]:
        """Calculate desired velocities using PID control with improved velocity smoothing.
        
        Key improvements:
        1. Added velocity ramping
        2. Improved error calculation
        3. Added low-pass filtering
        4. Better handling of integral windup
        """
        # Calculate errors in robot's frame
        error_x = target_x - x_current
        error_y = target_y - y_current
        
        # Transform errors to robot's local frame
        error_local_x = np.cos(theta_current) * error_x + np.sin(theta_current) * error_y
        error_local_y = -np.sin(theta_current) * error_x + np.cos(theta_current) * error_y
        
        # Calculate heading error
        theta_error = target_theta - theta_current
        theta_error = np.arctan2(np.sin(theta_error), np.cos(theta_error))
        
        # Calculate distance error with improved smoothing
        error_distance = np.sqrt(error_local_x**2 + error_local_y**2)
        error_direction = np.sign(error_local_x)
        
        # Add low-pass filter for distance error
        alpha = 0.2  # Filter coefficient (0 < alpha < 1)
        if not hasattr(self, 'filtered_distance_error'):
            self.filtered_distance_error = error_distance
        self.filtered_distance_error = (alpha * error_distance + 
                                    (1 - alpha) * self.filtered_distance_error)
        
        # Improved integral windup prevention
        if abs(self.linear_integral) * self.Ki_linear > self.max_linear_velocity:
            self.linear_integral = np.sign(self.linear_integral) * self.max_linear_velocity / self.Ki_linear
        
        # Update linear PID terms with filtered error
        self.linear_integral += self.filtered_distance_error * error_direction * self.dt
        linear_derivative = ((self.filtered_distance_error * error_direction - 
                            self.linear_prev_error) / self.dt)
        
        # Calculate base linear velocity
        v_desired = (self.Kp_linear * self.filtered_distance_error * error_direction +
                    self.Ki_linear * self.linear_integral +
                    self.Kd_linear * linear_derivative)
        
        # Improved velocity ramping
        if not hasattr(self, 'current_v'):
            self.current_v = 0.0
        
        max_v_change = self.max_acceleration * self.dt
        v_target = np.clip(v_desired, -self.max_linear_velocity, self.max_linear_velocity)
        v_change = np.clip(v_target - self.current_v, 
                        -max_v_change, max_v_change)
        v_desired = self.current_v + v_change
        self.current_v = v_desired
        
        # Scale velocity based on distance and improved heading factor
        approach_factor = min(1.0, error_distance / self.velocity_threshold)
        heading_factor = 0.5 * (1 + np.cos(theta_error))  # Smoother heading factor
        v_desired *= approach_factor * max(0.3, heading_factor)
        
        # Angular control with improved smoothing
        if not hasattr(self, 'filtered_theta_error'):
            self.filtered_theta_error = theta_error
        self.filtered_theta_error = alpha * theta_error + (1 - alpha) * self.filtered_theta_error
        
        # Update angular PID with filtered error
        self.angular_integral += self.filtered_theta_error * self.dt
        if abs(self.angular_integral) * self.Ki_angular > self.max_angular_velocity:
            self.angular_integral = (np.sign(self.angular_integral) * 
                                self.max_angular_velocity / self.Ki_angular)
        
        angular_derivative = (self.filtered_theta_error - self.angular_prev_error) / self.dt
        
        # Calculate angular velocity with improved smoothing
        omega_desired = (self.Kp_angular * self.filtered_theta_error +
                        self.Ki_angular * self.angular_integral +
                        self.Kd_angular * angular_derivative)
        
        # Apply angular velocity ramping
        if not hasattr(self, 'current_omega'):
            self.current_omega = 0.0
        
        max_omega_change = self.max_angular_acceleration * self.dt
        omega_target = np.clip(omega_desired, -self.max_angular_velocity, self.max_angular_velocity)
        omega_change = np.clip(omega_target - self.current_omega,
                            -max_omega_change, max_omega_change)
        omega_desired = self.current_omega + omega_change
        self.current_omega = omega_desired
        
        # Update previous errors with filtered values
        self.linear_prev_error = self.filtered_distance_error * error_direction
        self.angular_prev_error = self.filtered_theta_error
        
        return v_desired, omega_desired

    def improved_velocities_to_rpm(self, v: float, omega: float) -> Tuple[int, int]:
        """Convert velocities to RPM with improved smoothing and acceleration limiting.
        
        Key improvements:
        1. Added acceleration limiting
        2. Improved RPM calculation
        3. Added deadband compensation
        4. Better handling of wheel velocity differences
        """
        # Calculate wheel velocities
        v_right = (v + omega * self.wheel_base / 2)
        v_left = (v - omega * self.wheel_base / 2)
        
        # Convert to RPM with improved accuracy
        rpm_right = int((v_right * 60) / (2 * np.pi * self.wheel_radius) * self.gear_ratio)
        rpm_left = int((v_left * 60) / (2 * np.pi * self.wheel_radius) * self.gear_ratio)
        
        # Add deadband compensation (adjust these values based on your motors)
        deadband = 50  # RPM
        if abs(rpm_right) < deadband and rpm_right != 0:
            rpm_right = np.sign(rpm_right) * deadband
        if abs(rpm_left) < deadband and rpm_left != 0:
            rpm_left = np.sign(rpm_left) * deadband
        
        # Get current RPM values
        current_rpm_right = self.history['rpm_right'][-1] if self.history['rpm_right'] else 0
        current_rpm_left = self.history['rpm_left'][-1] if self.history['rpm_left'] else 0
        
        # Calculate maximum allowed RPM change based on acceleration limits
        # Convert acceleration limit to RPM/s
        max_rpm_change = int((self.max_acceleration * 60) / 
                            (2 * np.pi * self.wheel_radius) * self.gear_ratio * self.dt)
        
        # Add additional smoothing for large changes
        if abs(rpm_right - current_rpm_right) > 2 * max_rpm_change:
            max_rpm_change = max_rpm_change * 0.75  # Reduce maximum change for large jumps
        
        # Apply acceleration limits with improved smoothing
        rpm_right = np.clip(rpm_right, 
                        current_rpm_right - max_rpm_change,
                        current_rpm_right + max_rpm_change)
        rpm_left = np.clip(rpm_left,
                        current_rpm_left - max_rpm_change,
                        current_rpm_left + max_rpm_change)
        
        # Apply global RPM limits
        rpm_right = np.clip(rpm_right, -self.max_rpm, self.max_rpm)
        rpm_left = np.clip(rpm_left, -self.max_rpm, self.max_rpm)
        
        # Ensure wheel speeds maintain desired ratio for turning
        if v != 0:
            desired_ratio = v_right / v_left if v_left != 0 else 1
            actual_ratio = rpm_right / rpm_left if rpm_left != 0 else 1
            if abs(desired_ratio - actual_ratio) > 0.1:  # If ratio is off by more than 10%
                # Adjust RPMs to better maintain the desired ratio
                avg_rpm = (rpm_right + rpm_left) / 2
                rpm_right = avg_rpm * (1 + 0.5 * (desired_ratio - 1))
                rpm_left = avg_rpm * (1 - 0.5 * (desired_ratio - 1))
        
        return int(rpm_right), int(rpm_left)


    
    def calculate_pid_velocities(self, target_x: float, target_y: float, target_theta: float,
                                x_current: float, y_current: float, 
                                theta_current: float) -> Tuple[float, float]:
        """Calculate desired velocities using PID control with target orientation.
        
        Args:
            target_x: Target x position
            target_y: Target y position
            target_theta: Target orientation
            x_current: Current x position
            y_current: Current y position
            theta_current: Current orientation
            
        Returns:
            Tuple containing:
            - v_desired: Desired linear velocity
            - omega_desired: Desired angular velocity
        """
        # Calculate errors in robot's frame
        error_x = target_x - x_current
        error_y = target_y - y_current
        
        # Transform errors to robot's local frame
        error_local_x = np.cos(theta_current) * error_x + np.sin(theta_current) * error_y
        error_local_y = -np.sin(theta_current) * error_x + np.cos(theta_current) * error_y
        
        # Calculate heading error using target_theta
        theta_error = target_theta - theta_current
        theta_error = np.arctan2(np.sin(theta_error), np.cos(theta_error))  # Normalize to [-pi, pi]
        
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
        
        # Scale velocity based on distance and heading error
        approach_factor = min(1.0, error_distance / self.velocity_threshold)
        heading_factor = np.cos(theta_error)  # Reduce speed when heading is off
        v_desired *= approach_factor * max(0.2, heading_factor)
        
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
        # print(f"RPM uncliped: right: {desired_rpm_right}       left: {desired_rpm_left}")?
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
        

        # print(f"RPM: right: {rpm_right}       left: {rpm_left}")
        return int(rpm_right), int(rpm_left)
        # return int(1000), int(1000)
    
    def generate_straight_line_trajectory(self, start_pos: np.ndarray, target_pos: np.ndarray, 
                                    num_points: int = 100) -> np.ndarray:
        """Generate straight line trajectory from start to target position with angles.
        
        Args:
            start_pos: Starting position [x, y]
            target_pos: Target position [x, y]
            num_points: Number of points in trajectory
        
        Returns:
            trajectory: Array of shape (num_points, 3) containing [x, y, theta] for each point
        """
        # Calculate direction vector
        direction = target_pos - start_pos
        distance = np.linalg.norm(direction)
        
        if distance < 1e-6:  # If start and target are very close
            return np.column_stack((
                np.tile(start_pos, (num_points, 1)),
                np.zeros(num_points)  # Keep current heading if no movement
            ))
        
        # Calculate desired heading angle (constant throughout straight line)
        target_angle = np.arctan2(direction[1], direction[0])
        
        # Generate equally spaced points along the line
        t = np.linspace(0, 1, num_points)[:, np.newaxis]
        positions = start_pos + t * direction
        
        # Create array of target angles (same angle for straight line)
        angles = np.full(num_points, target_angle)
        
        # Combine positions and angles
        trajectory = np.column_stack((positions, angles))
        
        return trajectory

    def move_to_target(self, target_x: float, target_y: float) -> Dict:
        """Execute straight line trajectory to target position with PID control."""
        print(f"Moving to target: ({target_x}, {target_y})")
        
        # Initialize plot manager
        # plot_manager = PlotManager()
        
        try:
            # Generate straight line trajectory with angles
            start_pos = np.array([self.x, self.y])
            target_pos = np.array([target_x, target_y])
            trajectory = self.generate_straight_line_trajectory(start_pos, target_pos)
            
            # Plot initial state
            # plot_manager.plot_current_state(self, trajectory[:, :2], target_x, target_y, 0)
            print("Starting movement...")
            
            target_idx = 0
            max_time = 30.0  # seconds
            start_time = time.time()
            last_plot_time = start_time
            plot_iteration = 1
            
            while True:
                current_time = time.time()
                
                # Get current state
                x_current = data.y_current / 1000  # Convert from mm to meters
                y_current = data.x_current / 1000
                theta_current = np.deg2rad(data.f_current)
                
                # Update internal state
                self.x = x_current
                self.y = y_current
                self.theta = theta_current
                
                # Check if goal is reached
                dist_to_goal = np.sqrt((target_x - x_current)**2 + (target_y - y_current)**2)
                if dist_to_goal < self.goal_tolerance:
                    print(f"Goal reached! Final position: ({x_current:.2f}, {y_current:.2f})")
                    self.stop_motors()
                    # plot_manager.plot_current_state(self, trajectory[:, :2], target_x, target_y, plot_iteration)
                    break
                
                # Get current target point from trajectory (including angle)
                current_target = trajectory[min(target_idx, len(trajectory)-1)]
                
                # Calculate desired velocities using PID with target angle

                # v_desired, omega_desired = self.calculate_pid_velocities(
                #     current_target[0], current_target[1], current_target[2],
                #     x_current, y_current, theta_current
                # )


                v_desired, omega_desired = self.improved_calculate_pid_velocities(
                    current_target[0], current_target[1], current_target[2],
                    x_current, y_current, theta_current
                )
                
                
                # Print current control signals
                print(f"Control: v={v_desired:.3f} m/s, omega={omega_desired:.3f} rad/s", end='\r')
                
                # Convert to motor RPM
                # rpm_right, rpm_left = self.velocities_to_rpm(v_desired, omega_desired)
                rpm_right, rpm_left = self.improved_velocities_to_rpm(v_desired, omega_desired)
            
                # Update motor commands
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
                
                # Update plot and print status every 5 seconds
                if current_time - last_plot_time >= 0.5:
                    print("\n" + "="*50)  # Clear the control signals line and add separator
                    print(f"Status Update - Time elapsed: {current_time - start_time:.1f}s")
                    print(f"Current position: ({x_current:.2f}, {y_current:.2f})")
                    print(f"Current heading: {np.degrees(theta_current):.1f} degrees")
                    print(f"Distance to goal: {dist_to_goal:.3f}m")
                    print(f"Current velocities: Linear={v_desired:.3f}m/s, Angular={omega_desired:.3f}rad/s")
                    print(f"Motor commands: Right={rpm_right}rpm, Left={rpm_left}rpm")
                    print("="*50)
                    
                    # Save plots
                    # plot_manager.plot_current_state(self, trajectory, target_x, target_y, plot_iteration)
                    last_plot_time = current_time
                    plot_iteration += 1
                
                # Move to next trajectory point if close enough
                if np.sqrt((current_target[0] - x_current)**2 + 
                        (current_target[1] - y_current)**2) < 0.1:
                    target_idx = min(target_idx + 1, len(trajectory)-1)
                
                # Control loop timing
                time.sleep(self.dt)
                
        except Exception as e:
            print(f"\nError during movement: {e}")
            self.emergency_stop()
            raise
        finally:
            # Clean up
            print("\nCleaning up...")
            self.reset_pid_states()  # Reset PID controller states
            # plot_manager.cleanup()
            
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

    def plot_results(self, history: Dict, target_x: float, target_y: float):
        """Plot the trajectory tracking results with all relevant data.
        
        Args:
            history (Dict): Dictionary containing movement history
            target_x (float): Target x position
            target_y (float): Target y position
        """
        try:
            # Create directory for final plots if it doesn't exist
            save_dir = 'final_plots'
            os.makedirs(save_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Create figure with subplots
            plt.figure(figsize=(20, 15))
            
            # 1. Trajectory plot
            plt.subplot(2, 2, 1)
            # Plot actual path
            plt.plot(history['x'], history['y'], '-r', label='Robot Path')
            # Plot start and end points
            plt.plot(history['x'][0], history['y'][0], 'go', label='Start')
            plt.plot(target_x, target_y, 'r*', label='Target')
            plt.plot(history['x'][-1], history['y'][-1], 'mo', label='End Position')
            
            plt.grid(True)
            plt.legend()
            plt.title('Robot Trajectory')
            plt.xlabel('X (meters)')
            plt.ylabel('Y (meters)')
            plt.axis('equal')
            
            # 2. Velocities plot
            plt.subplot(2, 2, 2)
            time_points = np.arange(len(history['v'])) * self.dt
            plt.plot(time_points, history['v'], label='Linear Velocity (m/s)')
            plt.plot(time_points, history['omega'], label='Angular Velocity (rad/s)')
            plt.grid(True)
            plt.legend()
            plt.title('Robot Velocities')
            plt.xlabel('Time (s)')
            plt.ylabel('Velocity')
            
            # 3. Motor RPM plot
            plt.subplot(2, 2, 3)
            plt.plot(time_points, history['rpm_right'], label='Right Wheel RPM')
            plt.plot(time_points, history['rpm_left'], label='Left Wheel RPM')
            plt.grid(True)
            plt.legend()
            plt.title('Motor RPM')
            plt.xlabel('Time (s)')
            plt.ylabel('RPM')
            
            # 4. Error plot
            plt.subplot(2, 2, 4)
            plt.plot(time_points, history['linear_error'], label='Distance to Goal (m)')
            plt.plot(time_points, history['angular_error'], label='Angular Error (rad)')
            plt.grid(True)
            plt.legend()
            plt.title('Tracking Errors')
            plt.xlabel('Time (s)')
            plt.ylabel('Error')
            
            # Save the plot
            filename = os.path.join(save_dir, f'final_results_{timestamp}.png')
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()
            
            print(f"\nFinal results plot saved to: {filename}")
            
            # Create additional analysis plots
            self._plot_detailed_analysis(history, timestamp, save_dir)
        
        except Exception as e:
            print(f"Error while plotting results: {e}")

    def _plot_detailed_analysis(self, history: Dict, timestamp: str, save_dir: str):
        """Create additional analysis plots."""
        try:
            plt.figure(figsize=(15, 10))
            time_points = np.arange(len(history['v'])) * self.dt
            
            # Calculate some statistics
            avg_linear_vel = np.mean(history['v'])
            max_linear_vel = np.max(np.abs(history['v']))
            avg_angular_vel = np.mean(np.abs(history['omega']))
            max_angular_vel = np.max(np.abs(history['omega']))
            avg_error = np.mean(history['linear_error'])
            final_error = history['linear_error'][-1]
            
            # Plot velocity profiles with statistics
            plt.subplot(2, 1, 1)
            plt.plot(time_points, np.abs(history['v']), label='|Linear Velocity|')
            plt.axhline(y=avg_linear_vel, color='r', linestyle='--', 
                    label=f'Avg Linear Vel: {avg_linear_vel:.3f} m/s')
            plt.grid(True)
            plt.legend()
            plt.title(f'Velocity Analysis\nMax Linear Vel: {max_linear_vel:.3f} m/s, ' 
                    f'Max Angular Vel: {max_angular_vel:.3f} rad/s')
            plt.xlabel('Time (s)')
            plt.ylabel('Velocity (m/s)')
            
            # Plot error convergence
            plt.subplot(2, 1, 2)
            plt.plot(time_points, history['linear_error'], label='Distance Error')
            plt.axhline(y=avg_error, color='r', linestyle='--', 
                    label=f'Avg Error: {avg_error:.3f} m')
            plt.grid(True)
            plt.legend()
            plt.title(f'Error Convergence Analysis\nFinal Error: {final_error:.3f} m')
            plt.xlabel('Time (s)')
            plt.ylabel('Error (m)')
            
            # Save the analysis plot
            filename = os.path.join(save_dir, f'detailed_analysis_{timestamp}.png')
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()
            
            print(f"Detailed analysis plot saved to: {filename}")
            
        except Exception as e:
            print(f"Error while plotting detailed analysis: {e}")

# Example usage
if __name__ == "__main__":
    
    # Initialize robot controller with tuned gains
    robot = RealRobotController(
        wheel_radius=2*0.03572,    # Adjust to your robot's dimensions
        wheel_base= 2*0.152,      # Distance between wheels
        max_rpm=11000,        # Maximum motor RPM
        gear_ratio=16.0,      # If you have gear reduction
        # PID gains - tune these based on your robot's behavior
        Kp_linear=310.0,
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
        goal_tolerance = 0.01,
        max_linear_velocity = 3.0,
        max_angular_velocity = 2.0,
        velocity_threshold = 1.0
        
    )
    
    # Main control loop

    try:
        # Get target position
        target_x = 1.0
        target_y = 0.0
        
        # Move to target
        history = robot.move_to_target(target_x, target_y)
        robot.plot_results(history, target_x, target_y)

    except KeyboardInterrupt:
        print("\nTrajectory interrupted by user")
        robot.stop_motors()
        # robot.plot_results(history, target_x, target_y)
                
