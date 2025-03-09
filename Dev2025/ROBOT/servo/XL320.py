from dynamixel_sdk import *
import sys
import time
debug = False

TORQUE = 24
MODE = 11
GOAL_POSITION = 30
CURRENT_POSITION = 37
LED = 25


def parallel_rotateXL320(ids, angles):
    for i in range(len(angles)):
        angles[i] = int((angles[i] / 360)*1023)

    SERVO_PORT = "/dev/ttyUSB0"
    portHandler = PortHandler(SERVO_PORT)
    portHandler.openPort()

    # Baud rate set via Wizard (default value is 57600)
    portHandler.setBaudRate(115200)

    handler = Protocol2PacketHandler()

    for id in ids:
        # Disable torque in order to set operating mode
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, id, TORQUE, 0)
        if debug:
            print("TORQUE : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

    for i in range(len(ids)):
        # Choosing operating mode
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, ids[i], MODE, 2)
        if debug:
            print("SINGLEMODE : %s" %
                  handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("SINGLEMODE : %s" %
                  handler.getRxPacketError(servo_error))

        # Enabling torque in order to set position goal and velocity
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, ids[i], TORQUE, 1)
        if debug:
            print(f"TORQUE {ids[i]}:  {handler.getTxRxResult(communication_result)}")
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

    dxl_goal_position = angles

    groupSyncWrite = GroupSyncWrite(portHandler, handler, GOAL_POSITION, 2)

    for i in range(len(ids)):
        # Allocate Dynamixel#1 goal position value into byte array
        param_goal_position = [DXL_LOBYTE(dxl_goal_position[i]), DXL_HIBYTE(dxl_goal_position[i])]

        # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(
            ids[i], param_goal_position)
        if dxl_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % ids[i])
            #quit()
            return

    # Syncwrite goal position
    dxl_comm_result = groupSyncWrite.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % handler.getTxRxResult(dxl_comm_result))

    # Clear syncwrite parameter storage
    groupSyncWrite.clearParam()

    return

if __name__ == "__main__":
    while True:
        parallel_rotateXL320([1,5],[180,90])
        print("rotiram")
        time.sleep(1)
        parallel_rotateXL320([1,5],[90,270])
        print("opet rotiram")
        time.sleep(1)
