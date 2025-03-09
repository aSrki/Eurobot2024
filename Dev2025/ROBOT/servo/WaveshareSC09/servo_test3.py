# servo_controller.py
from WaveshareSC09.scservo_sdk import *

class ServoController:
    def __init__(self, device='/dev/ttyUSB0', baudrate=115200, servo_id=1):
        self.SCS_ID = servo_id
        self.DEVICENAME = device
        self.portHandler = PortHandler(device)
        self.packetHandler = PacketHandler(1)  # protocol_end = 1
        
        self.portHandler.openPort()
        self.portHandler.setBaudRate(baudrate)
        
    def move_servo(self, position):
        position = max(100, min(4000, position))
        self.packetHandler.write2ByteTxRx(
            self.portHandler, 
            self.SCS_ID, 
            42,  # ADDR_SCS_GOAL_POSITION
            position
        )
        
    def close(self):
        self.portHandler.closePort()