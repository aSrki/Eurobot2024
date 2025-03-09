#!/usr/bin/env python3
import serial
import time
import sys
import multiprocessing as mp
import signal

if __name__ == "__main__":
    import sys
    sys.path.append("/home/robot/Eurobot2024/Robot/Python")
import data

class TOFSensor:
    """
    Class for managing Time of Flight (TOF) sensors communication
    Optimized for maximum speed
    """
    # Constants
    TOF_LENGTH = 16
    TOF_HEADER = (87, 0, 255)  # 0x57, 0x00, 0xff
    
    def __init__(self, port=data.TOF_PORT, baudrate=921600, timeout=0.1):
        """
        Initialize the TOF sensor manager
        
        Args:
            port (str): Serial port to connect to
            baudrate (int): Baud rate for serial communication
        """
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.commands = [
            bytes([0x57, 0x10, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0x63]),  # command Tof_ID = 0
            bytes([0x57, 0x10, 0xFF, 0xFF, 0x01, 0xFF, 0xFF, 0x64]),  # command Tof_ID = 1
            bytes([0x57, 0x10, 0xFF, 0xFF, 0x02, 0xFF, 0xFF, 0x65])   # command Tof_ID = 2
        ]
        
    def open_serial(self):
        """Open the serial connection to the TOF sensors"""

        print(f"Opening serial port {self.port} with boudrate {self.baudrate}")
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            self.ser.flushInput()
            return self.ser
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return None
        
    def close_serial(self):
        """Close the serial connection"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            
    def verify_checksum(self, data, length):
        """
        Verify the checksum of received data
        
        Args:
            data (bytes): Data received from sensor
            length (int): Length of data including checksum
            
        Returns:
            bool: True if checksum is valid, False otherwise
        """
        TOF_check = 0
        for k in range(0, length - 1):
            TOF_check += data[k]
        TOF_check = TOF_check % 256
        
        return TOF_check == data[length - 1]
    
    def read_tof(self, command):
        """
        Send command to TOF sensor and read response
        
        Args:
            command (bytes): Command to send to sensor
            
        Returns:
            bytes: Response from the sensor
        """
        self.ser.reset_input_buffer()
        self.ser.write(command)
        return self.ser.read(self.TOF_LENGTH)
    
    def parse_tof_distance(self, tof_data):
        """
        Fast parse of TOF sensor data - only extracts distance
        
        Args:
            tof_data (bytes): Raw data from TOF sensor
            
        Returns:
            tuple: (sensor_id, distance) or (None, None) if invalid
        """
        # Fast validation
        if (len(tof_data) == self.TOF_LENGTH and
            tof_data[0] == self.TOF_HEADER[0] and 
            tof_data[1] == self.TOF_HEADER[1] and
            tof_data[2] == self.TOF_HEADER[2] and
            self.verify_checksum(tof_data, self.TOF_LENGTH)):
            
            # Valid data - extract only what we need
            sensor_id = tof_data[3]
            distance = (tof_data[8]) | (tof_data[9] << 8) | (tof_data[10] << 16)
            return sensor_id, distance
        
        return None, None
    
    def read_all_sensors_fast(self):
        """
        Read data from all TOF sensors with minimal processing
        
        Returns:
            list: List of (sensor_id, distance) tuples
        """
        results = []
        
        for command in self.commands:
            tof_data = self.read_tof(command)
            sensor_id, distance = self.parse_tof_distance(tof_data)
            if sensor_id is not None:
                results.append((sensor_id, distance))
            
        return results


class TOFProcessManager:
    """
    Manager class to run TOF sensor reading in a separate process
    Optimized for maximum speed
    """
    def __init__(self, port=data.TOF_PORT, baudrate=921600):
        """
        Initialize the TOF process manager
        
        Args:
            port (str): Serial port for TOF sensors
            baudrate (int): Baud rate for serial communication
        """
        self.port = port
        self.baudrate = baudrate
        self.data_queue = mp.Queue()
        self.control_queue = mp.Queue()
        self.process = None
    
    def start(self):
        """Start the TOF reading process"""
        if self.process is not None and self.process.is_alive():
            return
        
        self.process = mp.Process(
            target=self._process_function,
            args=(self.data_queue, self.control_queue, self.port, self.baudrate),
            daemon=True  # Set as daemon for auto-termination when main process exits
        )
        self.process.start()
    
    def stop(self):
        """Stop the TOF reading process"""
        if self.process and self.process.is_alive():
            self.control_queue.put("STOP")
            self.process.join(timeout=2)
            
            if self.process.is_alive():
                self.process.terminate()
                self.process.join(timeout=1)
            
        self.process = None

        print("TOF process stopped.")
    
    def is_running(self):
        """Check if the TOF process is running"""
        return self.process is not None and self.process.is_alive()
    
    def get_data(self, timeout=0.01):
        """
        Get the latest data from the TOF process with minimal wait
        
        Args:
            timeout (float): Timeout for queue.get() in seconds
            
        Returns:
            dict: TOF sensor data or None if no data is available
        """
        try:
            return self.data_queue.get(timeout=timeout)
        except mp.queues.Empty:
            return None
    
    @staticmethod
    def _process_function(data_queue, control_queue, port, baudrate):
        """
        Process function that reads TOF sensors and puts data in a queue
        Optimized for speed
        """
        # Set up signal handling for this process
        def signal_handler(sig, frame):
            if tof_sensor:
                tof_sensor.close_serial()
            sys.exit(0)
            
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        tof_sensor = None
        
        try:
            # Initialize TOF sensor
            tof_sensor = TOFSensor(port, baudrate)
            tof_sensor.open_serial()
            
            count = 0
            start_time = time.time()
            
            # Main loop - optimized for speed
            while True:
                # Quick check for control commands
                if not control_queue.empty():
                    cmd = control_queue.get()
                    if cmd == "STOP":
                        break
                
                # Read all sensors with minimal processing
                readings = tof_sensor.read_all_sensors_fast()
                
                # Prepare minimal output
                output = {
                    "timestamp": time.time(),
                    "readings": readings
                }
                
                # Put data in queue for main process
                data_queue.put(output)
                
                # Only calculate speed occasionally to reduce overhead
                count += 1
                if count % 10 == 0:
                    current_time = time.time()
                    elapsed = current_time - start_time
                    if elapsed > 0:
                        rate = count / elapsed
                        output["rate"] = rate
                        start_time = current_time
                        count = 0
                
        except Exception as e:
            # Put error in queue
            data_queue.put({"error": str(e)})
        finally:
            # Clean up
            if tof_sensor:
                tof_sensor.close_serial()


# Example standalone usage
if __name__ == "__main__":
    # Create TOF process manager
    tof_manager = TOFProcessManager()
    
    # Set up signal handling for main process
    def signal_handler(sig, frame):
        print("\nSignal received, shutting down...")
        tof_manager.stop()
        sys.exit(0)
        
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Start TOF process
        tof_manager.start()
        print("TOF process started. Press Ctrl+C to exit.")
        
        # Main loop
        while True:
            try:
                # Get data from TOF process with a timeout
                data = tof_manager.get_data(timeout=0.1)  # Longer timeout to make interrupt more responsive
                
                if data:
                    # Check for errors
                    if "error" in data:
                        print(f"Error in TOF process: {data['error']}")
                        break
                    
                    # Process TOF data - just print readings
                    for sensor_id, distance in data.get("readings", []):
                        print(f"Sensor {sensor_id}: {distance} mm")
                    
                    # Print rate if available
                    if "rate" in data:
                        print(f"Reading rate: {data['rate']:.2f} Hz")
                
            except KeyboardInterrupt:
                # This inner try/except makes sure we catch keyboard interrupts that occur
                # during the data processing loop
                print("\nKeyboard interrupt detected, shutting down...")
                break
                
    except KeyboardInterrupt:
        # This outer try/except catches keyboard interrupts at the start or between iterations
        print("\nKeyboard interrupt detected, shutting down...")
    except Exception as e:
        # Handle any other exceptions
        print(f"\nError occurred: {e}")
    finally:
        # Always make sure to stop the TOF process
        print("Stopping TOF process...")
        tof_manager.stop()
        print("Shutdown complete.")