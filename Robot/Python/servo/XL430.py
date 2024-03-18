from dynamixel_sdk import *
import time
import threading
from enum import Enum

if __name__ == "__main__":
    import sys
    sys.path.append("..")

else:
    import sys
    sys.path.append("/home/robot/Eurobot2024/Robot/Python")
import data


debug = False

TORQUE = 64
MODE = 11
GOAL_POSITION = 116
CURRENT_POSITION = 132
VELOCITY = 112
LED = 65
POSITION_P = 84
VELOCITY_P = 78
VELOCITY_I = 76


def rotate(handler, portHandler, id, angle):

    servo_angle = int((int(angle)/360)*4095)

    # setting goal position angle (4095 = 360deg)
    communication_result, servo_error = handler.write4ByteTxRx(
        portHandler, id, GOAL_POSITION, servo_angle)
    if debug:
        print("POSITION : %s" %
              handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("POSITION : %s" % handler.getRxPacketError(servo_error))

    return


def read_current_load(handler, portHandler, id):
    load, _, _ = handler.read2ByteTxRx(portHandler, id, 126)

    if load > 30000:
        load -= 65535

    return load


def read_current_position(handler, portHandler, id):
    try:
        current_position, _, _ = handler.read4ByteTxRx(
            portHandler, id, CURRENT_POSITION)

    except Exception as e:
        current_position, _, _ = handler.read4ByteTxRx(
            portHandler, id, CURRENT_POSITION)

    if current_position > 2147483648:
        current_position -= 4294967296

    return int((current_position/4095)*360)


def parallel_rotate(ids, angles):
    print("JA SAM SADA U PARALELI OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    portHandler = PortHandler(data.SERVO_PORT)
    portHandler.openPort()

    # Baud rate set via Wizard (default value is 57600)
    portHandler.setBaudRate(115200)

    handler = Protocol2PacketHandler()

    for i in range(len(angles)):
        angles[i] = int((angles[i] / 360)*4095)

    for id in ids:
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, id, TORQUE, 0)
        if debug:
            print("TORQUE : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

    for i in range(len(ids)):
        # Choosing operating mode
        print("Single mode on")
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, ids[i], MODE, 3)
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
            print("TORQUE : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

    dxl_goal_position = angles

    groupSyncWritePosition = GroupSyncWrite(
        portHandler, handler, GOAL_POSITION, 4)
    groupSyncWriteVelocity = GroupSyncWrite(portHandler, handler, VELOCITY, 4)

    velocity_added = False

    for i in range(len(ids)):
        # Allocate goal position value into byte array
        param_goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_position[i])), DXL_HIBYTE(DXL_LOWORD(
            dxl_goal_position[i])), DXL_LOBYTE(DXL_HIWORD(dxl_goal_position[i])), DXL_HIBYTE(DXL_HIWORD(dxl_goal_position[i]))]

        # Add goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWritePosition.addParam(
            ids[i], param_goal_position)
        if dxl_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % ids[i])
            quit()

    # Syncwrite velocity
    if velocity_added:
        dxl_comm_result = groupSyncWriteVelocity.txPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % handler.getTxRxResult(dxl_comm_result))

        groupSyncWriteVelocity.clearParam()

    # Syncwrite goal position
    dxl_comm_result = groupSyncWritePosition.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % handler.getTxRxResult(dxl_comm_result))

    # Clear syncwrite parameter storage
    groupSyncWritePosition.clearParam()

    ANGLE_TOLERANCE = 4
    MAX_ANGLE = 225
    max_load = 500
    num_success = len(ids)
    success_cnt = 0
    data.object_sensor = 0

    array_ids = [2, 3, 7, 8, 9, 11]

    if any(i in array_ids for i in ids):
        detection_cnt = 0
        # print("uso sam u onaj IF")
        while success_cnt < num_success:
            # print("uso sam u onaj WHILE")
            for i in range(num_success):
                # print("uso sam u onaj FOR")
                if (int(ids[i]) == data.IDS.id_gripper_back_1.value):
                    # print("servo 9")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 9: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                elif (ids[i] == data.IDS.id_gripper_back_2.value):
                    # print("servo 7")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 7: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                elif (ids[i] == data.IDS.id_gripper_back_3.value):
                    # print("servo 3")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 3: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                elif (ids[i] == data.IDS.id_gripper_front_1.value):
                    # print("servo 11")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 11: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                elif (ids[i] == data.IDS.id_gripper_front_2.value):
                    # print("servo 2")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 2: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                elif (ids[i] == data.IDS.id_gripper_front_3.value):
                    # print("servo 8")
                    id = ids[i]
                    current_position = read_current_position(
                        handler, portHandler, id)
                    current_load = read_current_load(handler, portHandler, id)
                    print(
                        f"Servo: {id}:, Current position: {current_position}")
                    # print(f"load 8: {current_load}")
                    if current_load > max_load:
                        print("LOAAAADDDDD")
                        rotate(handler, portHandler, id, current_position - 1)
                        success_cnt += 1
                        if abs(current_position - MAX_ANGLE) < ANGLE_TOLERANCE:
                            detection_cnt += 1
                    elif abs((current_position/360)*4095 - angles[i]) < 20:
                        success_cnt += 1
                # print(f"success_num: {success_cnt}")
        print(f"detected: {detection_cnt}")
        if detection_cnt == 3:
            data.object_sensor = 1
            print("all grippers empty")
        return


class ServoXL430:

    id = 0
    speed = 0
    angle = 0
    mode = "s"
    portHandler = None
    handler = None

    def __init__(self, id, speed=1023, mode="s", debug=False):
        self. id = id
        self.speed = speed
        self.mode = mode

        self.portHandler = PortHandler(data.SERVO_PORT)
        self.portHandler.openPort()

        # Baud rate set via Wizard (default value is 57600)
        self.portHandler.setBaudRate(115200)

        self.handler = Protocol2PacketHandler()

        # Disable torque in order to set operating mode
        communication_result, servo_error = self.handler.write1ByteTxRx(
            self.portHandler, id, TORQUE, 0)

        if debug:
            print("TORQUE : %s" %
                  self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % self.handler.getRxPacketError(servo_error))

        # choosing operating mode
        if (self.mode == "m"):
            print("Multi mode on")
            communication_result, servo_error = self.handler.write1ByteTxRx(
                self.portHandler, id, MODE, 4)
            if debug:
                print("MULTIMODE : %s" %
                      self.handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("MULTIMODE : %s" %
                      self.handler.getRxPacketError(servo_error))
        else:
            print("Single mode on")
            communication_result, servo_error = self.handler.write1ByteTxRx(
                self.portHandler, id, MODE, 3)
            if debug:
                print("SINGLEMODE : %s" %
                      self.handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("SINGLEMODE : %s" %
                      self.handler.getRxPacketError(servo_error))

        # # changing pid paramateres
        # communication_result, servo_error = self.handler.write2ByteTxRx(
        #     self.portHandler, id, POSITION_P, 500)
        # if debug:
        #     print("POSITION P GAIN : %s" %
        #           self.handler.getTxRxResult(communication_result))
        # if servo_error != 0:
        #     print("POSITION P GAIN : %s" %
        #           self.handler.getRxPacketError(servo_error))

        # communication_result, servo_error = self.handler.write2ByteTxRx(
        #     self.portHandler, id, VELOCITY_P, 70)
        # if debug:
        #     print("VELOCITY P GAIN : %s" %
        #           self.handler.getTxRxResult(communication_result))
        # if servo_error != 0:
        #     print("VELOCITY P GAIN : %s" %
        #           self.handler.getRxPacketError(servo_error))

        # communication_result, servo_error = self.handler.write2ByteTxRx(
        #     self.portHandler, id, VELOCITY_I, 1920)
        # if debug:
        #     print("VELOCITY I GAIN : %s" %
        #           self.handler.getTxRxResult(communication_result))
        # if servo_error != 0:
        #     print("VELOCITY I GAIN : %s" %
        #         self.handler.getRxPacketError(servo_error))

        # enabling torque in order to set position goal and velocity
        communication_result, servo_error = self.handler.write1ByteTxRx(
            self.portHandler, id, TORQUE, 1)
        if debug:
            print("TORQUE : %s" %
                  self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % self.handler.getRxPacketError(servo_error))

    def __del__(self):
        self.portHandler.closePort()

    def read_current_position(self):
        try:
            current_position, _, _ = self.handler.read4ByteTxRx(
                self.portHandler, self.id, CURRENT_POSITION)

        except Exception as e:
            current_position, _, _ = self.handler.read4ByteTxRx(
                self.portHandler, self.id, CURRENT_POSITION)

        if current_position > 2147483648:
            current_position -= 4294967296

        return int((current_position/4095)*360)

    def read_current_load(self):
        load, _, _ = self.handler.read2ByteTxRx(
            self.portHandler, self.id, 126)\

        if load > 30000:
            load -= 65535

        return load

    def rotate(self, *args):
        if len(args) == 1:
            velocity = self.speed
            sleep = 0
        if len(args) == 2:
            velocity = int(args[1])
            sleep = 0
        if len(args) == 3:
            velocity = int(args[1])
            sleep = int(args[2])

        current_position = 10000000000000
        servo_angle = int((int(args[0])/360)*4095)
        servo_speed = int(((velocity*10.23)/1023)*327.67)

        # setting velocity of Dynamixel
        communication_result, servo_error = self.handler.write4ByteTxRx(
            self.portHandler, self.id, VELOCITY, servo_speed)
        if debug:
            print("VELOCITY : %s" %
                  self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("VELOCITY : %s" % self.handler.getRxPacketError(servo_error))

        # setting goal position angle (4095 = 360deg)
        communication_result, servo_error = self.handler.write4ByteTxRx(
            self.portHandler, self.id, GOAL_POSITION, servo_angle)
        if debug:
            print("POSITION : %s" %
                  self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("POSITION : %s" % self.handler.getRxPacketError(servo_error))

        tolerance = 50

        while (abs(abs(current_position) - abs(servo_angle)) > tolerance) and data.elapsed_time < data.time_strategy_type:
            time.sleep(.01)
            try:
                current_position, result, servo_error = self.handler.read4ByteTxRx(
                    self.portHandler, self.id, CURRENT_POSITION)

                if current_position > 2147483648:
                    current_position -= 4294967296

            except:
                servo_error = 1

            load = self.read_current_load()
            # print(f"LOAD : {load}")

            if (load > 500) and (self.id == 11 or self.id == 8 or self.id == 2 or self.id == 9 or self.id == 7 or self.id == 3):
                print(f"LOAD detected : {load}")
                goal_angle = int(((current_position - 11)/4095)*365)
                threading.Thread(target=self.rotate, args=[goal_angle]).start()
                # self.rotate(goal_angle)
                return

            # elif (load > 700) and (self.id == 9 or self.id == 7 or self.id == 3):
            #     print(f"LOAD detected : {load}")
            #     goal_angle = int(((current_position - 11)/4095)*365)
            #     threading.Thread(target=self.rotate, args=[goal_angle]).start()
            #     # self.rotate(goal_angle)
            #     return

            if servo_error != 0:
                print("DEAD SERVO : %s" % str(self.id))

                dxl_comm_result, dxl_error = self.handler.reboot(
                    self.portHandler, self.id)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % self.handler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % self.handler.getRxPacketError(dxl_error))

                time.sleep(.1)

                print("[ID:%03d] reboot Succeeded\n" % self.id)

                data.stop = True
                data.dead_servo = self.id
                return

        time.sleep(sleep/1000)

        return


if __name__ == "__main__":
    while True:
        # USB port used by U2D2
        # SERVO_PORT = "/dev/ttyUSB0"

        portHandler = PortHandler(data.SERVO_PORT)
        portHandler.openPort()
        # Baud rate set via Wizard (default value is 57600)
        portHandler.setBaudRate(115200)

        id = int(input("Enter ID: "))

        mode = input("Ented mode s/m: ")

        handler = Protocol2PacketHandler()

        # Disable torque in order to set operating mode
        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, id, 64, 0)
        print("TORQUE : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

        if (mode == "m"):
            print("Multi mode on")
            communication_result, servo_error = handler.write1ByteTxRx(
                portHandler, id, 11, 4)
            print("MULTIMODE : %s" %
                  handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("MULTIMODE : %s" % handler.getRxPacketError(servo_error))
        else:
            print("Single mode on")
            communication_result, servo_error = handler.write1ByteTxRx(
                portHandler, id, 11, 3)
            print("SINGLEMODE : %s" %
                  handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("SINGLEMODE : %s" %
                      handler.getRxPacketError(servo_error))

        # turning the led off
        current_position = 10000000000000

        angle = int(input("Enter goal angle: "))
        angle = int((angle/360)*4095)

        speed = int(input("Enter speed: "))
        speed = int(((speed*10.23)/1023)*327.67)

        communication_result, servo_error = handler.write1ByteTxRx(
            portHandler, id, 64, 1)
        print("TORQUE : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % handler.getRxPacketError(servo_error))

        # setting velocity of Dynamixel
        communication_result, servo_error = handler.write4ByteTxRx(
            portHandler, id, 112, speed)
        print("VELOCITY : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("VELOCITY : %s" % handler.getRxPacketError(servo_error))

        # setting goal position angle (4095 = 360deg)
        communication_result, servo_error = handler.write4ByteTxRx(
            portHandler, id, 116, int(angle))
        print("POSITION : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("POSITION : %s" % handler.getRxPacketError(servo_error))

        if (angle >= 0):
            communication_result, servo_error = handler.write1ByteTxRx(
                portHandler, id, 65, 0)
            print("LED : %s" % handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("LED : %s" % handler.getRxPacketError(servo_error))
