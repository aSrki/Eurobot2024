if __name__ == '__main__':
    import os
    import sys

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    sys.path.append(parent_dir)

    from XL430 import ServoXL430
else:
    from servo.XL430 import ServoXL430

from roboclaw.roboclaw_python.roboclaw_3 import Roboclaw
from io_ports.MagnetControl import MagnetControl

import data
from data import IDS
import time


class Servo_Moving:

    def __init__(self):
        self.debug = True

        self.port = "/dev/tty_TTLroboclaw"
        self.baud = 38400
        try:
            self.roboclaw55 = Roboclaw(self.port, self.baud) 
            print(f"Opening roboclaw port at {self.port}")
            self.roboclaw55.Open()
        except:
            print(f"Error opening roboclaw port at {self.port}")
            exit()
        self.encoder_2_count = self.roboclaw55.SetEncM2(0x80, 0)
        try:
            self.roboclaw56 = Roboclaw(self.port, self.baud) 
            print(f"Opening roboclaw port at {self.port}")
            self.roboclaw56.Open()
        except:
            print(f"Error opening roboclaw port at {self.port}")
            exit()
        self.encoder_1_count = self.roboclaw56.SetEncM1(0x80, 0)

        self.magnet = MagnetControl()

    def operation(self, __ID, __angle, __velocity=100, __time=0.2):
        if not data.running.is_set():
            return

        # data.log.add_info_message(f"Servo id is: ", __ID)
        # if data.debug:
        #    print("Servo id is : ", __ID)

        # kucati if ID == neki broj pa vozi
        # if __ID == IDS.id_trougao.value:
        #     servo = ServoXL430(__ID, __velocity, "m")
        #     curr_pos = servo.read_current_position()
        #     print(f"TRENUTNA POS:  {curr_pos}\n\n\n")
        #     servo.rotate(curr_pos - 179)
        elif __ID < 53:
            if self.debug:
                print("XL-430", __ID, __angle, __velocity)
            servo = ServoXL430(__ID, __velocity, "s")
            servo.rotate(__angle)

        elif __ID == 55:
            if self.debug:
                print("Maxon_Lift_Prednji", __ID, __angle, __velocity)

            self.brzina = 2000 * __velocity

            self.broj_krugova = __angle/40
            
            self.roboclaw56.SpeedAccelDeccelPositionM1(
                0x80, 1000000000, self.brzina, 10000000, round(self.broj_krugova * 106496), 1)

        elif __ID == 56:
            if self.debug:
                print("Maxon_Lift_Zadnji", __ID, __angle, __velocity)
            
            brzina = 2000 * __velocity

            self.broj_krugova = __angle/40 #40 je precnik pogonske remenice * pi
            print(f"BRZINA {brzina}, pos {self.broj_krugova * 106496}")
            self.roboclaw55.SpeedAccelDeccelPositionM2(
                0x80, 1000000000, brzina, 10000000, round(self.broj_krugova * 106496), 1)
            
            
        elif __ID == 57:
            if self.debug:
                print("Leva_ruka - magnet: ", __ID, __angle) 

            if __angle == 1:
                self.magnet.left_arm_on()
            elif __angle == 0:
                self.magnet.left_arm_off()

        elif __ID == 58:
            if self.debug:
                print("Desna_ruka - magnet: ", __ID, __angle) 

            if __angle == 1:
                self.magnet.right_arm_on()
            elif __angle == 0:
                self.magnet.right_arm_off()

        elif __ID == 59:
            if self.debug:
                print("Zid_prednji - magnet: ", __ID, __angle) 

            if __angle == 1:
                self.magnet.front_wall_on()
            elif __angle == 0:
                self.magnet.front_wall_off()

        elif __ID == 60:
            if self.debug:
                print("Zid_zadnji - magnet: ", __ID, __angle) 

            if __angle == 1:
                self.magnet.back_wall_on()
            elif __angle == 0:
                self.magnet.back_wall_off()

        else:
            if self.debug:
                print("EMPTY OPERATIONS")

        # timer = 0
        # print('SERVO')
        # while __time * 1000 >= timer:
        #     time.sleep(.001)
        #     timer += 1
        #     # print('timer       ',timer)

        return

 

    # def pokreni_ruku(self):

        # desno dole 180 start -> max pos 90    ID 8        180, 125 ako ne zelimo da udarimo odom, 
        # desno gore 270 start -> max pos 90    ID 1        270, 180, 

        # levo dole 90 start   -> max pos 180   ID 10       90, 145
        # levo gore 90 start   -> max pos 270   ID 5        90, 180



if __name__ == "__main__":
    bool_test = True
    operations = Servo_Moving()
    data.running.set()

    while bool_test:
        input_id = int(input("input id: "))
        input_pos = int(input("input angle: "))
        input_vel = int(input("input vel: "))

        operations.operation(input_id, input_pos, input_vel)

    operations.pokreni_ruku()
