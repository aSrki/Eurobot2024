from io_ports.switches import Switches
import threading
import data
from data import Sensors
import time

DEBUG = True


def custom_print(msg):
    if DEBUG:
        print(msg)


class SensorsDetection:
    debug = True

    def __init__(self):
        self.switches = Switches()

    def start(self):
        self.switches.start()

        data.sensors = Sensors.ALL_OFF
        data.lidar = Sensors.ALL_OFF
        threading.Thread(target=self.run).start()

    def run(self):
        custom_print("SENSORS")

        while True:
            if not data.running.is_set():
                return

            if (self.front_sensors() or self.back_sensors() or self.lidar_back_sensors() or self.lidar_front_sensor()) and not data.stop:
                data.stop = True
                data.is_front = (data.sensors == Sensors.FRONT_ON) or (
                    data.lidar == Sensors.FRONT_ON)
                data.is_back = (data.sensors == Sensors.BACK_ON) or (
                    data.lidar == Sensors.BACK_ON)

                data.sensors = Sensors.ALL_OFF
                data.lidar = Sensors.ALL_OFF

            time.sleep(.01)

    def front_sensors(self):
        if data.sensor_front_right or data.sensor_front_left:
            custom_print("Detected in front")
            return True

        return False

    def back_sensors(self):
        if data.sensor_back_right or data.sensor_back_left:
            custom_print("Detected in back")
            return True

        return False

    def lidar_front_sensor(self):
        if data.front_lidar_detection:
            custom_print("Lidar detected in front")
            return True

        return False

    def lidar_back_sensors(self):
        if data.back_lidar_detection:
            custom_print("Lidar detected in back")
            return True

        return False
