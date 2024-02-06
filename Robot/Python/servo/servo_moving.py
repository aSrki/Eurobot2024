
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
        if __ID == IDS.id_doser.value:
            servo = ServoXL430(__ID, __velocity, "m")
            curr_pos = servo.read_current_position()
            if data.first_cherry:
                data.first_cherry = False
                servo.rotate(curr_pos + 22.5)
            else:
                servo.rotate(curr_pos + 45)
        elif __ID < 50:
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
    def home(self):
        return
        # ServoXL430(IDS.id_cherry_pipe.value).rotate(170)
        # ServoXL430(IDS.id_vacuum.value).rotate(173)
        # ServoXL430(IDS.id_reservoir_door.value).rotate(190)
        # ServoXL430(IDS.id_gripper.value).rotate(48)
        # ServoXL430(IDS.id_lift.value).rotate(10)
        # ServoXL430(IDS.id_doser.value).rotate(310)
        


if __name__ == "__main__":
    bool_test = True
    operations = Servo_Moving()
    data.running.set()

    while bool_test:
        input_id = int(input("input id: "))
        input_pos = int(input("input angle: "))

        operations.operation(input_id, input_pos, 100)