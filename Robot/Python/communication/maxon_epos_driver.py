import time
from ctypes import *

class MaxonMotor:
    def __init__(self, id, acceleration = 100000, deceleration = 100000):
        self.baudrate = 1000000
        self.timeout = 500
        self.pErrorCode = c_uint()
        self.pDeviceErrorCode = c_uint()
        self.path='/home/robot/robot/communication/libEposCmd.so'
        cdll.LoadLibrary(self.path)
        self.epos = CDLL(self.path)
        self.ID = id
        self.acceleration = acceleration
        self.deceleration = deceleration

        if self.ID == 1:
            self.keyHandle = self.epos.VCS_OpenDevice(b'EPOS4', b'MAXON SERIAL V2', b'USB', b'USB0', byref(self.pErrorCode)) # specify EPOS version and interface
        elif self.ID == 2:
            self.keyHandle = self.epos.VCS_OpenDevice(b'EPOS4', b'MAXON SERIAL V2', b'USB', b'USB1', byref(self.pErrorCode)) # specify EPOS version and interface

        print(self.keyHandle)
        
        
        self.epos.VCS_SetProtocolStackSettings(self.keyHandle, self.baudrate, self.timeout, byref(self.pErrorCode)) # set baudrate
        self.epos.VCS_ClearFault(self.keyHandle, self.ID, byref(self.pErrorCode)) # clear all faults
        self.epos.VCS_ActivateProfileVelocityMode(self.keyHandle, self.ID, byref(self.pErrorCode)) # activate profile position mode
        self.epos.VCS_SetEnableState(self.keyHandle, self.ID, byref(self.pErrorCode)) # enable device
        
        self.epos.VCS_SetVelocityProfile(self.keyHandle, self.ID, self.acceleration, self.deceleration, byref(self.pErrorCode)) # set profile parameters

    def rotate_with_rpm(self, target_speed):
        self.epos.VCS_MoveWithVelocity(self.keyHandle, self.ID, target_speed, byref(self.pErrorCode)) # rotate with speed

    def disable_driver(self):
        self.epos.VCS_SetDisableState(self.keyHandle, self.ID, byref(self.pErrorCode)) # disable device
        self.epos.VCS_CloseDevice(self.keyHandle, byref(self.pErrorCode)) # close device

if __name__ == "__main__":
    # Initiating connection and setting motion profile
    try:
        maxon1 = MaxonMotor(1, 5000, 10000)
        maxon2 = MaxonMotor(2, 5000, 10000)


        while True:
            speed1 = input("Speed: ")
            maxon1.rotate_with_rpm(int(speed1))
            maxon2.rotate_with_rpm(-int(speed1))
        # maxon1.rotate_with_rpm(1500)
        # maxon2.rotate_with_rpm(-1500)
        # time.sleep(3)
        # maxon1.rotate_with_rpm(-1500)
        # maxon2.rotate_with_rpm(1500)
        # time.sleep(3)
        # maxon1.rotate_with_rpm(0)
        # maxon2.rotate_with_rpm(0)
        # time.sleep(3)
        maxon1.disable_driver()
        maxon2.disable_driver()
    except KeyboardInterrupt:
        maxon1.rotate_with_rpm(0)
        maxon2.rotate_with_rpm(0)
   


