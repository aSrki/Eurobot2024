from dynamixel_sdk import *
import time 
from servo_init import *

ADDR_PRESENT_POSITION = 132
# port = "/dev/ttyUSB0"
# baudrate = 115200
ids = (1, 4)

def read_positions(ids):
    # port_handler = PortHandler(port)
    # packet_handler = PacketHandler(2.0)

    # # Open the port
    # if port_handler.openPort():
    #     print("Port opened successfully")
    # else:
    #     print("Failed to open the port")
    #     exit(1)

    # # Set port baudrate
    # if port_handler.setBaudRate(baudrate):
    #     print(f"Baudrate set to {baudrate}")
    # else:
    #     print("Failed to change the baudrate")
    #     exit(1)
    with communication_lock:
        position = EncXL430(SERVO_PORT = "/dev/ttyUSB0", BAUD_RATE = 115200)
        if EncXL430.permission == 1:
            positions = {}
            for motor_id in ids:
                time.sleep(0.0001)
                # Read the present position of each motor
                dxl_present_position, _, _ = position.handler.read2ByteTxRx(
                    position.portHandler, motor_id, ADDR_PRESENT_POSITION
                )
                positions[motor_id] = dxl_present_position
                # print(f"Motor {motor_id} - Current position: {positions[motor_id]}")
                # print(f"MOTOR ID IN FOR LOOP {motor_id}")

            pos_r = positions[ids[0]]   # = position[1]
            pos_l = positions[ids[1]]   # = position[4]
            # port_handler.closePort()
            # print("Port handler closed")
            return pos_r,pos_l

if __name__ == "__main__":
    pos = []
    pos = read_positions((1,4))

