from dynamixel_sdk import *

class EncXL430:
    SERVO_PORT = "/dev/ttyUSB0"
    BAUD_RATE = 115200

    def __init__(self, BAUD_RATE, SERVO_PORT):
        self.BAUD_RATE = BAUD_RATE
        self.SERVO_PORT = SERVO_PORT
        self.portHandler = PortHandler(self.SERVO_PORT)
        self.portHandler.openPort()
        self.portHandler.setBaudRate(self.BAUD_RATE)
        self.handler = Protocol2PacketHandler()

