import time
import threading
from dynamixel_sdk import *

# Set the device and baudrate according to your setup
DEVICE_NAME = "/dev/ttyUSB0"
BAUDRATE = 115200

# Dynamixel parameters
DXL_ID = 1

# Control table addresses for Dynamixel XL430
ADDR_PRESENT_POSITION = 132  # Address for present position
ADDR_GOAL_VELOCITY = 104  # Address for goal velocity
ADDR_TORQUE_ENABLE = 64   # Address for torque enable

# Set the duration for which to read the position (in seconds)
DURATION_SECONDS = 2 

# Global variables to store present position and control the thread
present_position = None
stop_thread = False

def initialize_dynamixel(port_handler, baudrate):
    # Open the serial port
    if port_handler.openPort():
        print("Succeeded to open the port")
    else:
        raise ConnectionError("Failed to open the port")

    # Set baudrate
    if port_handler.setBaudRate(baudrate):
        print(f"Succeeded to set baudrate: {baudrate}")
    else:
        raise ConnectionError(f"Failed to set baudrate: {baudrate}")

def set_goal_velocity(port_handler, packet_handler, dxl_id, velocity):
    # Enable torque
    packet_handler.write1ByteTxRx(port_handler, dxl_id, ADDR_TORQUE_ENABLE, 1)

    # Set goal velocity
    packet_handler.write4ByteTxRx(port_handler, dxl_id, ADDR_GOAL_VELOCITY, velocity)

def stop_motor(port_handler, packet_handler, dxl_id):
    # Disable torque
    packet_handler.write1ByteTxRx(port_handler, dxl_id, ADDR_TORQUE_ENABLE, 0)

def read_position_thread(port_handler, packet_handler, dxl_id):
    global present_position
    while not stop_thread:
        position, _, _ = packet_handler.read4ByteTxRx(port_handler, dxl_id, ADDR_PRESENT_POSITION)
        if position >= 0:
            present_position = position
        time.sleep(0.001)  # Sleep for 1 millisecond between readings

def main():
    global present_position, stop_thread

    port_handler = PortHandler(DEVICE_NAME)
    packet_handler = PacketHandler(2.0)  # Use Protocol 2.0

    try:
        initialize_dynamixel(port_handler, BAUDRATE)

        # Example: Set the velocity to 100 (you can change this value as needed)
        velocity = 255
        set_goal_velocity(port_handler, packet_handler, DXL_ID, velocity)
        print(f"GOAL VELOCITY: {velocity}")

        # Start the thread for reading the present position
        position_thread = threading.Thread(target=read_position_thread, args=(port_handler, packet_handler, DXL_ID))
        position_thread.start()

        start_time = time.time()
        while time.time() - start_time < DURATION_SECONDS:
            if present_position is not None:
                print(f"Present Position: {present_position}")
            set_goal_velocity(port_handler, packet_handler, DXL_ID, 0)
            time.sleep(0.01)  # Adjust this delay as needed for the main loop

        # Stop the reading thread
        stop_thread = True
        position_thread.join()

        stop_motor(port_handler, packet_handler, DXL_ID)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the serial port
        port_handler.closePort()

if __name__ == "__main__":
    main()
