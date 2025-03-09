#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import threading
import signal
import sys

if __name__ == "__main__":
    import sys
    sys.path.append("/home/robot/Eurobot2024/Robot/Python")
import data
from data import Sensors
from tof_sensors import TOFProcessManager  


class TOFSwitches:
    """
    Class to manage TOF sensors with support for different sensor modes
    Uses existing data variables
    """
    debug = True  # Debug set to True by default
    debug_interval = 0.01  # How often to print debug info (in seconds)
    
    # Set up CINC GPIO
    GPIO.setmode(GPIO.BCM)
    CINC = 4
    GPIO.setup(CINC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def __init__(self, port=data.TOF_PORT, baudrate=921600):
        # Initialize TOF sensor manager
        self.tof_manager = TOFProcessManager(port=port, baudrate=baudrate)
        self.tof_distances = {}  # Dictionary to store latest TOF distances by sensor_id
        
        # Map sensor IDs to positions for easier reference
        self.sensor_positions = {
            0: "FRONT_LEFT",    # TOF ID 0 is front left
            1: "FRONT_RIGHT",   # TOF ID 1 is front right
            2: "BACK_LEFT",     # TOF ID 2 is back left
            3: "BACK_RIGHT"     # TOF ID 3 is back right
        }
        
        # Store raw distances internally (not in data module)
        self._raw_distances = {0: 0, 1: 0, 2: 0, 3: 0}
        
        # For tracking last debug print time
        self._last_debug_time = 0

        self.rate = 0

        self.MIN_DISTANCE = 12
        self.MAX_DISTANCE = 500

        self.debug_running = threading.Event()

    def start(self):
        # Start TOF sensor process
        self.tof_manager.start()
        
        # Start TOF monitoring thread
        thread = threading.Thread(target=self.run)
        thread.daemon = True  # Set as daemon so it exits when main thread exits
        thread.start()
        
        # If debug is enabled, also start a dedicated debug printing thread
        if self.debug:
            self.debug_running.set()
            debug_thread = threading.Thread(target=self.debug_loop)
            debug_thread.daemon = True
            debug_thread.start()
        
        # Register signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def signal_handler(self, sig, frame):
        print("TOF Switches received shutdown signal")
        self.tof_manager.stop()

    def run(self):
        """Main thread function that continuously checks TOF sensors"""
        while data.running.is_set():
            self.check()
            time.sleep(0.01)  # Small delay to prevent CPU overuse

    def debug_loop(self):
        """Dedicated thread for printing debug information at regular intervals"""
        while data.running.is_set():
            if self.debug:
                self.debug_print()
            time.sleep(self.debug_interval)

    def check(self):
        """Check TOF sensors based on current sensor mode"""
        # Always read CINC input
        data.cinc = GPIO.input(self.CINC)
        
        # Get latest TOF sensor data
        tof_data = self.tof_manager.get_data()
        
        if tof_data and data.SENSORS_ENABLED:
            # Check for errors
            if "error" in tof_data:
                print(f"Error in TOF process: {tof_data['error']}")
                return
            
            # Update stored distances with latest readings
            for sensor_id, distance in tof_data.get("readings", []):
                self._raw_distances[sensor_id] = distance
            
            # Apply sensor mode logic
            if data.sensors == Sensors.FRONT_ON:
                # Front sensors are enabled (0 and 1)
                self.update_front_sensors()
                self.clear_back_sensors()
                
            elif data.sensors == Sensors.BACK_ON:
                # Back sensors are enabled (2 and 3)
                self.clear_front_sensors()
                self.update_back_sensors()
                
            elif data.sensors == Sensors.ALL_OFF:
                # All sensors disabled
                self.clear_all_sensors()
                
            elif data.sensors == Sensors.ALL_ON:
                # Handle OBJECT mode - enable all sensors for safety
                self.update_all_sensors()
                
            else:
                # Unknown mode, enable all (for safety)
                self.update_all_sensors()

    def update_front_sensors(self):
        """Update front TOF sensor values in data module"""
        # Update sensor 0 (Front Left)
        if 0 in self._raw_distances:
            distance = self._raw_distances[0]
            # Set sensor flag if distance is within threshold (12-300mm)
            data.sensor_front_left = 1 if self.MIN_DISTANCE < distance < self.MAX_DISTANCE else 0
        
        # Update sensor 1 (Front Right)
        if 1 in self._raw_distances:
            distance = self._raw_distances[1]
            # Set sensor flag if distance is within threshold (12-300mm)
            data.sensor_front_right = 1 if self.MIN_DISTANCE < distance < self.MAX_DISTANCE else 0

    def update_back_sensors(self):
        """Update back TOF sensor values in data module"""
        # Update sensor 2 (Back Left)
        if 2 in self._raw_distances:
            distance = self._raw_distances[2]
            # Set sensor flag if distance is within threshold (12-300mm)
            data.sensor_back_left = 1 if self.MIN_DISTANCE < distance < self.MAX_DISTANCE else 0
            
        # Update sensor 3 (Back Right)
        if 3 in self._raw_distances:
            distance = self._raw_distances[3]
            # Set sensor flag if distance is within threshold (12-300mm)
            data.sensor_back_right = 1 if self.MIN_DISTANCE < distance < self.MAX_DISTANCE else 0

    def update_all_sensors(self):
        """Update all TOF sensor values"""
        self.update_front_sensors()
        self.update_back_sensors()

    def clear_front_sensors(self):
        """Clear front sensor values"""
        data.sensor_front_left = 0
        data.sensor_front_right = 0

    def clear_back_sensors(self):
        """Clear back sensor values"""
        data.sensor_back_left = 0
        data.sensor_back_right = 0

    def clear_all_sensors(self):
        """Clear all TOF sensor values"""
        self.clear_front_sensors()
        self.clear_back_sensors()
        
    def get_raw_distance(self, sensor_id):
        """Get the raw distance reading for a specific sensor"""
        return self._raw_distances.get(sensor_id, 0)

    def debug_print(self):
        """Print debug information"""
        # Get current reading rate if available through the TOF manager
        tof_data = self.tof_manager.get_data(timeout=0.01)
        if tof_data and "rate" in tof_data:
            self.rate = tof_data["rate"]
        
        print("\n--- TOF Sensor Status ---")
        if self.rate:
            print(f"Reading rate: {self.rate:.2f} Hz")
        
        # Get the current sensor mode
        sensor_mode = getattr(data, 'sensors', None)
        print(f"Mode: {sensor_mode}")
        print(f"CINC: {data.cinc}")
        
        # Print raw distances for all sensors
        for sensor_id, distance in self._raw_distances.items():
            position = self.sensor_positions.get(sensor_id, f"UNKNOWN_{sensor_id}")
            print(f"TOF {position} (ID: {sensor_id}): {distance} mm")
        
        # Print the virtual sensor flags
        print("Virtual sensor flags:")
        print(f"  Front Left: {data.sensor_front_left}")
        print(f"  Front Right: {data.sensor_front_right}")
        print(f"  Back Left: {data.sensor_back_left}")
        print(f"  Back Right: {data.sensor_back_right}")
        print("------------------------\n")


# For standalone testing
if __name__ == "__main__":
    # Set up data module for standalone testing
    if not hasattr(data, 'running'):
        data.running = threading.Event()
    data.running.set()
    
    # Use existing Sensors enum
    data.sensors = Sensors.ALL_ON
    data.SENSORS_ENABLED = True
    
    # Initialize sensor variables if needed
    if not hasattr(data, 'sensor_front_left'):
        data.sensor_front_left = 0
    if not hasattr(data, 'sensor_front_right'):
        data.sensor_front_right = 0
    if not hasattr(data, 'sensor_back_left'):
        data.sensor_back_left = 0
    if not hasattr(data, 'sensor_back_right'):
        data.sensor_back_right = 0
    if not hasattr(data, 'cinc'):
        data.cinc = 0
    
    # Create and start TOF switches
    tof_switches = TOFSwitches()
    tof_switches.debug = True
    tof_switches.debug_interval = 0.01  # Print debug info every 1 second
    tof_switches.start()
    
    try:
        print("TOF Switches running. Press Ctrl+C to exit.")
        
        while data.running.is_set():
            time.sleep(0.1)  # Just keep the main thread alive
            
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected, Shutting down...")
        
    finally:
        data.running.clear()
        tof_switches.tof_manager.stop()
        tof_switches.debug_running.clear()
        GPIO.cleanup()