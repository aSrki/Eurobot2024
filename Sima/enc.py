from dynamixel_sdk import *
import time 

ADDR_PRESENT_POSITION = 132
port = "/dev/ttyUSB0"
baudrate = 115200
ids = (1, 4)

def read_positions(ids):
    port_handler = PortHandler(port)
    packet_handler = PacketHandler(2.0)

    # Open the port
    if port_handler.openPort():
        print("Port opened successfully")
    else:
        print("Failed to open the port")
        exit(1)

    # Set port baudrate
    if port_handler.setBaudRate(baudrate):
        print(f"Baudrate set to {baudrate}")
    else:
        print("Failed to change the baudrate")
        exit(1)

    positions = {}
    for motor_id in ids:
        time.sleep(0.0001)
        # Read the present position of each motor
        dxl_present_position, _, _ = packet_handler.read2ByteTxRx(
            port_handler, motor_id, ADDR_PRESENT_POSITION
        )
        positions[motor_id] = dxl_present_position
        print(f"Motor {motor_id} - Current position: {positions[motor_id]}")
    
    port_handler.closePort()
    print("Port handler closed")
    return positions

if __name__ == "__main__":
    pos = []
    pos = read_positions((1,4))

