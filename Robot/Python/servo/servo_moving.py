
if __name__ == '__main__':

    import sys
    sys.path.append("..")
    from XL430 import ServoXL430
else:
    from servo.XL430 import ServoXL430


import data
import time
from data import IDS


class Servo_Moving:

    def __init__(self):
        self.debug = True

    def operation(self, __ID, __angle, __velocity=100, __time=0.2):
        if not data.running.is_set():
            return

        # data.log.add_info_message(f"Servo id is: ", __ID)
        # if data.debug:
        #     print("Servo id is : ", __ID)

        # kucati if ID == neki broj pa vozi
        if __ID == IDS.id_trougao.value:
            servo = ServoXL430(__ID, __velocity, "m")
            curr_pos = servo.read_current_position()
            print(f"TRENUTNA POS:  {curr_pos}\n\n\n")
            servo.rotate(curr_pos - 179)
        elif __ID < 53:
            if self.debug:
                print("XL-430", __ID, __velocity)
            servo = ServoXL430(__ID, __velocity, "s")
            servo.rotate(__angle)
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

    # dovodi sve servoe na pocetni polozaj
    def init_yellow(self):
        ServoXL430(IDS.id_back_arm.value).rotate(190, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(100, 30)
        ServoXL430(IDS.id_centar.value).rotate(30)
        ServoXL430(IDS.id_gripper_back_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_3.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_3.value).rotate(215)
        ServoXL430(IDS.id_back_arm.value).rotate(165, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(95, 30)
        ServoXL430(IDS.id_grtalica_prednja_leva.value).rotate(300)
        ServoXL430(IDS.id_grtalica_prednja_desna.value).rotate(60)
        ServoXL430(IDS.id_grtalica_zadnja_desna.value).rotate(300)
        ServoXL430(IDS.id_grtalica_zadnja_leva.value).rotate(60)
        return

    def init_blue(self):
        ServoXL430(IDS.id_back_arm.value).rotate(190, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(100, 30)
        ServoXL430(IDS.id_centar.value).rotate(300)
        ServoXL430(IDS.id_gripper_back_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_3.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_3.value).rotate(215)
        ServoXL430(IDS.id_back_arm.value).rotate(175, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(75, 30)
        ServoXL430(IDS.id_grtalica_prednja_leva.value).rotate(300)
        ServoXL430(IDS.id_grtalica_prednja_desna.value).rotate(60)
        ServoXL430(IDS.id_grtalica_zadnja_desna.value).rotate(300)
        ServoXL430(IDS.id_grtalica_zadnja_leva.value).rotate(60)
        return

    def home(self):
        ServoXL430(IDS.id_back_arm.value).rotate(190, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(100, 30)
        ServoXL430(IDS.id_centar.value).rotate(180)
        ServoXL430(IDS.id_gripper_back_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_back_3.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_1.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_2.value).rotate(215)
        ServoXL430(IDS.id_gripper_front_3.value).rotate(215)
        ServoXL430(IDS.id_back_arm.value).rotate(158, 30)
        ServoXL430(IDS.id_front_arm.value).rotate(65, 30)
        ServoXL430(IDS.id_grtalica_prednja_leva.value).rotate(300)
        ServoXL430(IDS.id_grtalica_prednja_desna.value).rotate(60)
        ServoXL430(IDS.id_grtalica_zadnja_desna.value).rotate(300)
        ServoXL430(IDS.id_grtalica_zadnja_leva.value).rotate(60)
        return
        return


if __name__ == "__main__":
    bool_test = True
    operations = Servo_Moving()
    data.running.set()

    while bool_test:
        input_id = int(input("input id: "))
        input_pos = int(input("input angle: "))
        input_vel = int(input("input vel: "))

        operations.operation(input_id, input_pos, input_vel)
