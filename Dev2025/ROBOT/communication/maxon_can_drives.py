import time
from ctypes import *
import canopen
import random


class MaxonMotor:
    def __init__(self, id, acceleration=100000, deceleration=100000):
        self.PDO_TIME = 0.005
        self.ID = id
        self.acceleration = acceleration
        self.deceleration = deceleration

        # da li se ovo moze raditi 2 puta
        self.network = canopen.Network()
        self.network.connect(channel='can1', bustype='socketcan')

        self.motor = self.network.add_node(self.ID, 'maxon.eds')

        self.network.sync.start(self.PDO_TIME)

        if self.ID == 1:
            self.cob_id = 0x201
            print(f"COB ID : {self.cob_id}, MOTOR ID : {self.ID}")
        elif self.ID == 5:
            self.cob_id = 0x205
            print(f"COB ID : {self.cob_id}, MOTOR ID : {self.ID}")

        self.motor.nmt.state = 'PRE-OPERATIONAL'
        time.sleep(2)
        cob_id = 0x201
        # Configure RPDO1 for velocity control
        self.motor.rpdo.read()
        self.motor.rpdo[1].clear()
        self.motor.rpdo[1].add_variable('Controlword')  # 0x6040
        self.motor.rpdo[1].add_variable('Target velocity')  # 0x60FF
        self.motor.rpdo[1].cob_id = self.cob_id  # Assign unique COB-ID
        self.motor.rpdo[1].trans_type = 1  # Synchronous updates
        self.motor.rpdo[1].enabled = True
        self.motor.rpdo.save()

        # Verify RPDO1 mapping
        print(f"Node {self.ID} RPDO1 COB-ID: {hex(self.motor.rpdo[1].cob_id)}")
        print(f"Node {self.ID} RPDO1 map: {self.motor.rpdo[1].map}")


        try:
            # Reset fault and ensure drive is ready
            self.motor.sdo[0x6040].raw = 0x80  # Fault reset
            time.sleep(0.1)

            self.motor.sdo[0x6060].raw = 0x03

            # Transition to "Ready to Switch On"
            self.motor.sdo[0x6040].raw = 0x06
            time.sleep(0.1)

            # Transition to "Switched On"
            self.motor.sdo[0x6040].raw = 0x07
            time.sleep(0.1)

            # Transition to "Operation Enabled"
            self.motor.sdo[0x6040].raw = 0x0F
            time.sleep(0.1)
            
            # Verify final state
            status = self.motor.sdo[0x6041].raw
            print(f"Node {self.ID} Statusword: {hex(status)}")


        except Exception as e:
            print(f"Error enabling Node {self.ID}: {e}")
            raise

        error_register = self.motor.sdo[0x1001].raw
        print(f"Node {self.ID} Error Register: {bin(error_register)}")
        error_history = self.motor.sdo[0x1003]
        print(f"Node {self.ID} Error History: {list(error_history.values())}")

        if error_register != 0:
            print(f"Node {self.ID} has active warnings/errors. Resolve before proceeding.")
            raise Exception(f"Error detected in Node {self.ID}: {bin(error_register)}")
      
        self.motor.nmt.state = 'OPERATIONAL'
        time.sleep(1)

    def rotate_with_rpm(self, target_speed):
        self.motor.rpdo[1]['Controlword'].raw = 0x0F  # Enable operation
        self.motor.rpdo[1]['Target velocity'].raw = target_speed
        self.motor.rpdo[1].transmit()
        # print(f"Speed set for motor ID:{self.ID} ; {target_speed} counts/sec")

    def disable_driver(self):
        self.motor.sdo[0x6040].raw = 0x06  # Shut down
        time.sleep(0.1)
        self.motor.nmt.state = 'PRE-OPERATIONAL'
        time.sleep(0.1)
        self.network.disconnect()
        print("Disconnected from CAN network.")


if __name__ == "__main__":

    # network = canopen.Network()
    # network.connect(channel='can1', bustype='socketcan')

    # # Slanje jednostavne CAN poruke
    # network.send_message(0x200, [0x01, 0x02, 0x03, 0x04])
    # print("Poruka poslana!")


    # Initiating connection and setting motion profile
    try:
        maxon1 = MaxonMotor(1, 5000, 10000)
        # time.sleep(1)
        maxon2 = MaxonMotor(5, 5000, 10000)

        while True:
            speed = input("Speed 1: ")
            maxon1.rotate_with_rpm(int(speed))
            time.sleep(0.5)
            speed = input("Speed 2: ")
            maxon2.rotate_with_rpm(int(speed))
        
    except KeyboardInterrupt:
        print("Stopping motors and exiting.")
        # maxon1.rotate_with_rpm(1500)
        # maxon2.rotate_with_rpm(-1500)
        # time.sleep(3)
        # maxon1.rotate_with_rpm(-1500)
        # maxon2.rotate_with_rpm(1500)
        # time.sleep(3)
        # maxon1.rotate_with_rpm(0)
        # maxon2.rotate_with_rpm(0)
        # time.sleep(3)
        maxon1.rotate_with_rpm(0)
        maxon2.rotate_with_rpm(0)
        maxon1.disable_driver()
        maxon2.disable_driver()


