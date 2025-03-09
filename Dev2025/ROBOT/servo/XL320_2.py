from dynamixel_sdk import *
import sys
import time

if __name__ == "__main__":
    import sys
    sys.path.append("..")
import data

debug = False

TORQUE = 24
MODE = 11
GOAL_POSITION = 30
CURRENT_POSITION = 37
LED = 25

BAUDRATE = 1000000

def normalize_angle(angle):
    """Normalize angle to [0, 360) range."""
    return angle % 360

def parallel_rotateXL320(ids, angles):
    # Normalize angles to [0, 360) and convert to position values
    angles = [normalize_angle(a) for a in angles]
    dxl_goal_position = [int((a / 360.0) * 1023) for a in angles]

    SERVO_PORT = "/dev/ttyUSB0"
    portHandler = PortHandler(SERVO_PORT)

    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        return

    # Set baud rate (XL320 default: 1,000,000 bps)
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to set the baudrate")
    else:
        print("Failed to set the baudrate")
        portHandler.closePort()
        return

    handler = Protocol2PacketHandler()

    try:
        # Disable torque for all servos
        for id in ids:
            comm_result, error = handler.write1ByteTxRx(portHandler, id, TORQUE, 0)
            if debug:
                print(f"{id} TORQUE OFF: {handler.getTxRxResult(comm_result)}")
            if error != 0:
                raise ValueError(f"{id} TORQUE OFF: {handler.getRxPacketError(error)}")

        # Set operating mode to Joint Mode (3)
        for id in ids:
            comm_result, error = handler.write1ByteTxRx(portHandler, id, MODE, 3)
            if debug:
                print(f"{id} SINGLEMODE: {handler.getTxRxResult(comm_result)}")
            if error != 0:
                raise ValueError(f"{id} SINGLEMODE: {handler.getRxPacketError(error)}")

        # Re-enable torque
        for id in ids:
            comm_result, error = handler.write1ByteTxRx(portHandler, id, TORQUE, 1)
            if debug:
                print(f"{id} TORQUE ON: {handler.getTxRxResult(comm_result)}")
            if error != 0:
                raise ValueError(f"{id} TORQUE ON: {handler.getRxPacketError(error)}")

        # Prepare sync write
        groupSyncWrite = GroupSyncWrite(portHandler, handler, GOAL_POSITION, 2)

        for i in range(len(ids)):
            param_goal = [
                DXL_LOBYTE(dxl_goal_position[i]),
                DXL_HIBYTE(dxl_goal_position[i])
            ]
            if not groupSyncWrite.addParam(ids[i], param_goal):
                raise ValueError(f"{ids[i]} sync write failed")

        # Execute sync write
        result = groupSyncWrite.txPacket()
        if result != COMM_SUCCESS:
            raise ValueError(handler.getTxRxResult(result))

    except (OSError, ValueError) as e:
        print(f"Error: {e}")

    finally:
        # Clear sync write and close port
        groupSyncWrite.clearParam()
        portHandler.closePort()

    return