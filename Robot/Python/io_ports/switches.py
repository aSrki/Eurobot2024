import RPi.GPIO as GPIO
import time
import threading
if __name__ == "__main__":
    import sys
    sys.path.append("/home/robot/Eurobot2024/Robot/Python")
import data
from data import Sensors


class Switches:
    debug = False
    GPIO.setmode(GPIO.BCM)
    FRONT_LEFT = 17
    FRONT_RIGHT = 27
    BACK_LEFT = 22
    BACK_RIGHT = 21

    OBJECT1 = 18
    OBJECT2 = 23

    CINC = 4

    # SENZORI
    GPIO.setup(FRONT_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FRONT_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BACK_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BACK_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(OBJECT1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(OBJECT2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(CINC, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __init__(self):
        pass

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        while data.running.is_set():
            self.check()
            time.sleep(0.01)

    def check(self):

        if data.SENSORS_ENABLED:

            if data.sensors == data.Sensors.FRONT_ON:
                data.sensor_front_left = GPIO.input(self.FRONT_LEFT)
                data.sensor_front_right = GPIO.input(self.FRONT_RIGHT)
                data.sensor_back_left = 0
                data.sensor_back_right = 0

            elif (data.sensors == data.Sensors.BACK_ON) and (data.elapsed_time > 90) and not (data.x_current > 1400 and (-700 < data.y_current < 700)):
                # print("\n Uspesno upaljeni senzori za sime \n!!!")
                data.object_sensor_1 = GPIO.input(self.OBJECT1)
                data.object_sensor_2 = GPIO.input(self.OBJECT2)

                # ovo je specificno za ovu godinu jer su object senzori sa zadnje strane
                data.sensor_back_left = GPIO.input(self.BACK_LEFT)
                data.sensor_back_right = GPIO.input(self.BACK_RIGHT)
                data.sensor_front_left = 0
                data.sensor_front_right = 0

            elif data.sensors == data.Sensors.BACK_ON:
                data.sensor_back_left = GPIO.input(self.BACK_LEFT)
                data.sensor_back_right = GPIO.input(self.BACK_RIGHT)
                data.sensor_front_left = 0
                data.sensor_front_right = 0

            elif data.sensors == data.Sensors.ALL_OFF:
                data.sensor_front_left = 0
                data.sensor_front_right = 0
                data.sensor_back_left = 0
                data.sensor_back_right = 0

            else:
                print("\n\n\n\n\t\tGRESKA U SWITCHEVIMA\n\n\n\n")
                data.sensor_front_left = GPIO.input(self.FRONT_LEFT)
                data.sensor_front_right = GPIO.input(self.FRONT_RIGHT)
                data.sensor_back_left = GPIO.input(self.BACK_LEFT)
                data.sensor_back_right = GPIO.input(self.BACK_RIGHT)

        data.cinc = GPIO.input(self.CINC)

        if self.debug:
            print(
                f"FRONT --> left: { data.sensor_front_left}  right: {data.sensor_front_right} BACK -->> left: {data.sensor_back_left}  right: {data.sensor_back_right}")
            print(f"BACK : {data.sensor_back_left} , {data.sensor_back_right}")
            print("CINCa : ", GPIO.input(self.CINC))
            print(f"CAKE HERE <3: {data.cake_sensor}")


if __name__ == "__main__":
    data.running.set()
    data.sensors = None
    switches = Switches()
    switches.debug = True

    while True:
        switches.check()
        time.sleep(0.1)
