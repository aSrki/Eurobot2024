import threading
import data
from dataclasses import dataclass
# from communication.can_commXYF import CAN_COMM
# from communication.maxon_can_drives import MaxonMotor

# robot 2024
from communication.can_comm import CAN_COMM
from communication.maxon_epos_driver import MaxonMotor
############
import os
from datetime import datetime
import time
from time import sleep
from collections import deque


import regulation_controller.PidPlotGenerator as ppg

@dataclass
class PIDParams:
    Kp: float = 0.0
    Ki: float = 0.0
    Kd: float = 0.0
    Ti: float = 0.0
    Td: float = 0.0

class PositionRegulation:
    def __init__(self, debug_mode: bool = True):
        self.debug_mode = debug_mode

        # PID PLOTTER KLASA
        self.plot_generator = ppg.PIDPlotter(should_plot_rotation=False)

        # Constants
        self.MAX_COUNT = 100
        self.DELAY = 0.01  # speed regulation ~30ms
        self.MAX_PID = 100000 # 4000
        self.MIN_PID = 0
        
        # Movement parameters
        self.CURVE_INC_TRANS = 0.2
        self.CURVE_INC_ROT = 0.25
        self.RAMP_INCREMENT_START = 100
        self.RAMP_INCREMENT_STOP = 50
        self.ROT_RAMP_UP_INCREMENT = 100
        self.ROT_RAMP_DOWN_INCREMENT = 50

        # State variables
        self.sending_trans = False
        self.sending_rot = False
        self.sending_stop = False
        self.stop_position = False
        
        # Initialize motors
        
        self.maxon_left = MaxonMotor(1, 100000, 50000)
        self.maxon_right = MaxonMotor(2, 100000, 50000)
        # ROBOT 2025
        # self.maxon_left = MaxonMotor(1, 5000, 10000)
        # self.maxon_right = MaxonMotor(5, 5000, 10000)

        # Position and movement tracking
        self.W_d = 0  # Desired position
        # nema desired rotation?
        self.W_F = data.f_current  # Current angle
        self.W_F_s = 0  # Previous angle target
        self.speed = 0
        self.rot_speed = 0
        self.MVL = 0  # Motor velocity left
        self.MVR = 0  # Motor velocity right
        
        # PID control variables
        self.pid_params = {
            'translation': PIDParams(),
            'rotation': PIDParams()
        }
        self.reset_pid_state()
        
        # Initialize communication
        self.can_communication = CAN_COMM()
        self._init_threads()

    def _set_rotation_pid_params(self):
        """Set PID parameters for rotation"""
        pojacanje = data.translate_pojacanje
        rotpoj = 1

        #ROBOT'25
        # self.pid_params['translation'].Kp = 20 * pojacanje
        # self.pid_params['rotation'].Kp = 90 * pojacanje * rotpoj # 120

        #ROBOT'24
        self.pid_params['translation'].Kp = 1 * pojacanje
        self.pid_params['rotation'].Kp = 1 * pojacanje * rotpoj # 120

        self.pid_params['translation'].Ti = 0
        self.pid_params['rotation'].Ti = 0

        self.pid_params['translation'].Td = 0
        self.pid_params['rotation'].Td = 0.015 # 0.009

    def _set_translation_pid_params(self):
        """Set PID parameters for translation"""
        pojacanje = data.translate_pojacanje
        self.speed_gain = data.top_speed
        rotpoj = 1

        #ROBOT'25
        # print("Transliram")
        # self.pid_params['translation'].Kp = 25 * pojacanje # 8
        # self.pid_params['rotation'].Kp =  110 * pojacanje * rotpoj # 50 100

        #ROBOT'24
        self.pid_params['translation'].Kp = 1 * pojacanje # 8
        self.pid_params['rotation'].Kp =  3 * pojacanje * rotpoj # 50 100

        self.pid_params['translation'].Ti = 0
        self.pid_params['rotation'].Ti = 0

        self.pid_params['translation'].Td = 0.075 # 0.075
        self.pid_params['rotation'].Td = 0 # 0.8

    def _set_stop_pid_params(self):
        """Set PID parameters for stopping"""
        self.pid_params['translation'].Kp = 2
        self.pid_params['rotation'].Kp = 0.5

        self.pid_params['translation'].Ti = 20
        self.pid_params['rotation'].Ti = 20

        self.pid_params['translation'].Td = 0
        self.pid_params['rotation'].Td = 0

    def reset_pid_state(self):
        """Reset all PID control state variables"""
        # Basic PID state
        self.integral_K = 0
        self.integral_R = 0
        self.en_K = 0
        self.en_R = 0
        self.es_K = 0
        self.es_R = 0
        self.ess_K = 0
        self.ess_R = 0
        
        # Movement state
        self.old_speed = 0
        self.old_rot_speed = 0
        self.t_trans = 0.03
        self.t_rot = 0.03
        
        # Anti-windup and filtering state
        self.dif_K = 0  # Filtered derivative for translation
        self.dif_R = 0  # Filtered derivative for rotation
        self.last_output_trans = 0  # For rate limiting
        self.last_output_rot = 0    # For rate limiting

    def _init_threads(self):
        """Initialize and start motor control threads"""
        self.threads = []
        for target in [self.send_vel_left, self.send_vel_right]:
            thread = threading.Thread(target=target)
            thread.start()
            self.threads.append(thread)

    def start(self):
        """Start the position regulation system"""
        self.can_communication.start()
        self.is_running = True
        thread = threading.Thread(target=self.running_calculation)
        thread.start()
        self.threads.append(thread)

    def running_calculation(self):
        """Main calculation loop"""
        while data.running.is_set():
            self.calculate_position()
            sleep(self.DELAY)

    def calculate_position(self):
        """Calculate current position and apply control"""
        d = data.d_current
        f = data.f_current

        if self.stop_position:
            self._stop_motors()
            
        else:
            self.regulation(d, f, True)

    def regulation(self, d, f, debug=False):
        """Main regulation logic"""
        # Get desired position and current state
        W_F = self.W_F
        W_d = self.W_d
        D = data.d_ukupno

        # Calculate errors
        self.en_K = W_d - D
        self.en_R = self._normalize_angle_error(W_F - f)

        # Set PID parameters based on movement type
        self._set_pid_parameters()
        
        # Calculate PID outputs
        pid_K = self._calculate_pid_translation()
        pid_R = self._calculate_pid_rotation()

        # Apply speed ramping
        self._apply_speed_ramping(pid_K, pid_R)
        
        # Apply anti-windup and motor control
        self._apply_motor_control()

    def _normalize_angle_error(self, error):
        """Normalize angle error to -180 to 180 range"""
        if error > 180:
            return -360 + error
        elif error < -180:
            return 360 + error
        return error

    def _set_pid_parameters(self):
        """Set PID parameters based on current movement state"""
        if self.sending_rot and not self.sending_stop:
            self._set_rotation_pid_params()
        elif self.sending_trans and not self.sending_stop:
            self._set_translation_pid_params()
        else:
            self._set_stop_pid_params()

    def _calculate_pid_translation(self):
        """Calculate PID output for translation with anti-windup"""
        params = self.pid_params['translation']
        dt = self.DELAY
        
        # Apply low-pass filter to error for smoother response
        filtered_error = 0.8 * self.en_K + 0.2 * self.es_K
        
        # Calculate P term
        Kp = params.Kp * filtered_error
        
        # Calculate I term with anti-windup
        if params.Ti != 0:
            # Calculate predicted integral term
            integral_term = self.integral_K + filtered_error * dt
            Ki_raw = params.Kp * (1 / params.Ti) * integral_term
            
            # Apply back-calculation anti-windup
            if abs(Ki_raw) > self.MAX_PID * 0.3:  # Limit integral to 30% of max output
                # Reset integral to prevent windup
                Ki = self.MAX_PID * 0.3 * (Ki_raw / abs(Ki_raw))
                self.integral_K = Ki * params.Ti / params.Kp
            else:
                Ki = Ki_raw
                self.integral_K = integral_term
        else:
            Ki = 0
            self.integral_K = 0
        
        # Calculate D term with derivative filtering
        if params.Td != 0:
            derivative = (filtered_error - self.es_K) / dt
            filtered_derivative = 0.8 * derivative + 0.2 * self.dif_K  # Low-pass filter
            Kd = params.Kp * params.Td * filtered_derivative
            self.dif_K = filtered_derivative
        else:
            Kd = 0
            self.dif_K = 0
        
        # Update error history
        self.ess_K = self.es_K
        self.es_K = filtered_error
        
        # Calculate total output with rate limiting
        output = Kp + Ki + Kd
        max_rate = self.MAX_PID * dt  # Maximum change per time step
        
        if abs(output - self.last_output_trans) > max_rate:
            output = self.last_output_trans + max_rate * (output - self.last_output_trans) / abs(output - self.last_output_trans)
        
        self.last_output_trans = output

        #print("$$$$$$$$LOGGING$$$$$$$$$$$")
        # Log debug data
        self.plot_generator._log_plot_data('translation', {
            'x_location': data.x_current,
            'y_location': data.y_current,
            'des_location': self.W_d,
            'error': self.en_K,
            'filtered_error': filtered_error,
            'p_term': Kp,
            'i_term': Ki,
            'd_term': Kd,
            'output': output
        })

        #print POSITION
        # print("X: " + str(data.x_current) + "         Y: " + str(data.y_current))
        
        return output

    def _calculate_pid_rotation(self):
        """Calculate PID output for rotation with anti-windup"""
        params = self.pid_params['rotation']
        dt = self.DELAY
        
        # Apply low-pass filter to error for smoother response
        filtered_error = 0.9 * self.en_R + 0.1 * self.es_R
        
        # Calculate P term
        Kp = params.Kp * filtered_error
        
        # Calculate I term with anti-windup
        if params.Ti != 0:
            # Calculate predicted integral term
            integral_term = self.integral_R + filtered_error * dt
            Ki_raw = params.Kp * (1 / params.Ti) * integral_term
            
            # Apply back-calculation anti-windup
            if abs(Ki_raw) > self.MAX_PID * 0.3:  # Limit integral to 30% of max output
                # Reset integral to prevent windup
                Ki = self.MAX_PID * 0.3 * (Ki_raw / abs(Ki_raw))
                self.integral_R = Ki * params.Ti / params.Kp
            else:
                Ki = Ki_raw
                self.integral_R = integral_term
        else:
            Ki = 0
            self.integral_R = 0
        
        # Calculate D term with derivative filtering
        if params.Td != 0:
            derivative = (filtered_error - self.es_R) / dt
            filtered_derivative = 0.8 * derivative + 0.2 * self.dif_R  # Low-pass filter
            Kd = params.Kp * params.Td * filtered_derivative
            self.dif_R = filtered_derivative
        else:
            Kd = 0
            self.dif_R = 0
        
        # Update error history
        self.ess_R = self.es_R
        self.es_R = filtered_error
        
        # Calculate total output with rate limiting
        output = Kp + Ki + Kd
        max_rate = self.MAX_PID * dt  # Maximum change per time step
        
        if abs(output - self.last_output_rot) > max_rate:
            output = self.last_output_rot + max_rate * (output - self.last_output_rot) / abs(output - self.last_output_rot)
        
        self.last_output_rot = output

        #Log plot data
        if self.debug_mode:
            self.plot_generator._log_plot_data('rotation', {
                'error': self.en_R,
                'filtered_error': filtered_error,
                'p_term': Kp,
                'i_term': Ki,
                'd_term': Kd,
                'output': output
            })
        
        return output

    def _apply_speed_ramping(self, pid_K, pid_R):
        """Apply `speed ramping to smooth movement"""
        # Handle translation movement
        if self.sending_trans:
            dif_speed = pid_K - self.old_speed
            
            if self.W_d >= 0:  # Forward movement
                curve = self.calculate_curve_trans(self.t_trans)
                self.t_trans += self.CURVE_INC_TRANS * data.translate_pojacanje

                if dif_speed < -self.RAMP_INCREMENT_STOP:
                    self.speed -= self.RAMP_INCREMENT_STOP
                elif pid_K > curve:
                    self.speed = curve
                else:
                    self.speed = pid_K
                    self.t_rot = 0.03
            else:  # Backward movement
                curve = self.calculate_curve_trans(self.t_trans)
                self.t_trans += self.CURVE_INC_TRANS * data.translate_pojacanje
                
                if pid_K < -curve:
                    self.speed = -curve
                elif dif_speed > self.RAMP_INCREMENT_STOP:
                    self.speed += self.RAMP_INCREMENT_STOP
                else:
                    self.speed = pid_K
                    self.t_rot = 0.03
        else:
            self.speed = pid_K

        self.speed = pid_K

        # Handle rotation movement
        if self.sending_rot:
            dif_rot_speed = pid_R - self.old_rot_speed
            
            if self.en_R > 0:  # Clockwise rotation
                curve = self.calculate_curve_rot(self.t_rot)
                self.t_rot += self.CURVE_INC_ROT * data.rotate_pojacanje

                if dif_rot_speed < -self.ROT_RAMP_DOWN_INCREMENT:
                    self.rot_speed -= self.ROT_RAMP_DOWN_INCREMENT
                elif pid_R > curve:
                    self.rot_speed = curve
                else:
                    self.rot_speed = pid_R
                    self.t_trans = 0.03
            else:  # Counter-clockwise rotation
                curve = self.calculate_curve_rot(self.t_rot)
                self.t_rot += self.CURVE_INC_ROT * data.rotate_pojacanje

                if pid_R < -curve:
                    self.rot_speed = -curve
                elif dif_rot_speed > self.ROT_RAMP_DOWN_INCREMENT:
                    self.rot_speed += self.ROT_RAMP_DOWN_INCREMENT
                else:
                    self.rot_speed = pid_R
                    self.t_trans = 0.03
        else:
            self.rot_speed = pid_R

        self.rot_speed = pid_R

        # Update previous speeds for next iteration
        self.old_rot_speed = self.rot_speed
        self.old_speed = self.speed

    def _apply_motor_control(self):
        """Apply final motor control values"""
        # Apply speed limits
        self.speed = max(min(self.speed, self.MAX_PID * data.top_speed), 
                        -self.MAX_PID * data.top_speed)

        # Calculate motor velocities
        # ROBOT 2025
        # self.MVL = int(self.speed + self.rot_speed)
        # self.MVR = int(self.speed - self.rot_speed)

        # ROBOT 2024
        self.MVL = int(self.speed - self.rot_speed)
        self.MVR = int(self.speed + self.rot_speed)

        # print(f"abs(self.en_K) {abs(self.en_K)} ; abs(self.en_R) {abs(self.en_R)}")
        print(f"x {data.x_current} ; y {data.y_current} ; f {data.f_current} ; mvl {self.MVL} ; mvr {self.MVR}")

        # Check if target reached
        # if abs(self.en_K) <= 3 and abs(self.en_K) > 0.1 and abs(self.en_R) <= 0.5 and abs(self.en_R) > 0.05 and -50 < self.MVL < 50 and - 50 < self.MVR < 50:
        # if abs(self.en_K) <= 3 and abs(self.en_R) <= 0.5 and -50 < self.MVL < 50 and - 50 < self.MVR < 50:
        if abs(self.en_K) <= 3 and abs(self.en_R) <= 0.5 and -50 < self.MVL < 50 and - 50 < self.MVR < 50:
            print("------------------------------------------------------------------------")
            # print(f"abs(self.en_K) {abs(self.en_K)} ; abs(self.en_R) {abs(self.en_R)}")
            print(f"USLOV ZA HANDLE TARGET REACHED : x {data.x_current} ; y {data.y_current} ; f {data.f_current} ; mvl {self.MVL} ; mvr {self.MVR}")
            print("------------------------------------------------------------------------")
            self._handle_target_reached()
        else:
            data.last_MVL = self.MVL
            data.last_MVR = self.MVR
            self.sending_stop = False
            
            #Log motor commands for debugging
            if self.debug_mode:
                self.plot_generator._log_motor_data(self.MVL, self.MVR)

    def _handle_target_reached(self):
        """Handle when target position is reached"""
        data.budz = True
        self._stop_motors()
        self.integral_K = 0
        self.integral_R = 0
        self.sending_stop = True

        print("----------------TARGET REACHED FUNCTION----------------")

        # If debug mode is enabled, save plots
        if self.debug_mode:
            try:
                #self.plot_generator.plot_translation(save=True)
                self.plot_generator.plot_all(save=True)
                # Clear debug data for next movement
                #self._clear_debug_data() -- NIJE IMPLEMENTIRANO --
                
            except Exception as e:
                print(f"Error saving debug plot: {str(e)}")

    def _stop_motors(self):
        """Stop both motors"""
        print("----------------------STOPPING MOTORS----------------------")
        self.maxon_left.rotate_with_rpm(0)
        self.maxon_right.rotate_with_rpm(0)

    def send_vel_left(self):
        """Send velocity commands to left motor"""
        while data.running.is_set():
            if not self.stop_position:
                self.maxon_left.rotate_with_rpm(self.MVL)
                sleep(self.DELAY)

    def send_vel_right(self):
        """Send velocity commands to right motor"""
        while data.running.is_set():
            if not self.stop_position:
                self.maxon_right.rotate_with_rpm(-self.MVR)
                sleep(self.DELAY)

    def calculate_curve_trans(self, t):
        """Calculate translation curve"""
        return 0.002*(t**5) - 0.14*(t**4) + 3.233*(t**3) - 19.5*(t**2) + 43*t

    def calculate_curve_rot(self, t):
        """Calculate rotation curve"""
        return 0.002*(t**5) - 0.14*(t**4) + 3.233*(t**3) - 19.5*(t**2) + 43*t

    def stop(self):
        """Stop all movement"""
        print("----------------Stopping all movement function----------------")
        self.stop_position = True

    def reset_position(self):
        """Reset position control"""
        self.stop_position = False
            
    def enable_debug(self):
        """Enable debug mode"""
        self.debug_mode = True
        self.start_time = time.time()
        
    def disable_debug(self):
        """Disable debug mode"""
        self.debug_mode = False