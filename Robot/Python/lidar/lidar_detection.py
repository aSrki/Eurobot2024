from adafruit_rplidar import RPLidar
import time
import math
# import matplotlib.pyplot as plt
if __name__ == "__main__":
    from matrix import TransformMatrix
    import sys
    sys.path.append("..")
else:
    from lidar.matrix import TransformMatrix
import threading
import data
from data import Sensors


def euclidian_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))


class LidarDetection:

    def __init__(self):
        self.lidar = None
        self.max_num_of_scans = 3
        self.transform = TransformMatrix(50)
        self.front_cone = 100
        self.back_cone = 100
        self.distance = 1000
        self.lidar_thread = None
        self.init()
        
    def start(self):
        self.lidar_thread = threading.Thread(target=self.scan)
        self.lidar_thread.start()

    def init(self):
        try:
            self.lidar = RPLidar(None, data.LIDAR_PORT,
                                 baudrate=115200, timeout=3)
            self.lidar.logging = False
            print(self.lidar.health)
            print(self.lidar._serial_port)
        except Exception as e:
            print(f"LIDAR INIT ERROR: {e}")
            return

    def scan(self):
        scan_data = [0]*360
        num_of_scans = 0

        try:

            for scan in self.lidar.iter_scans():
                # print(self.lidar._serial_port)
                if not data.running.is_set():
                    print("KRAJ LIDARA")
                    break

                if num_of_scans == self.max_num_of_scans:
                    scan_data = [0]*360
                    num_of_scans = 0
                    # plt.clf()

                num_of_scans += 1

                for (_, angle, distance) in scan:
                    angle = min([359, math.floor(angle)])
                    scan_data[angle] = distance

                    # proverava prednju stranu ako je ukkljucena detekcija
                    if ((angle > 360 - self.front_cone/2) or
                            (angle <= self.front_cone/2)) and \
                            distance < self.distance and \
                            data.lidar == Sensors.FRONT_ON:
                        x, y = self.transform.lidar2table(
                            data.x_current, data.y_current, distance, angle, data.f_current)

                        if 50 < x < 1950 and 50 < y < 2950:
                            dist = euclidian_distance(
                                x, data.x_current, y, data.y_current)

                            if dist < data.lidar_view:
                                print("LIIIIIIDDDDDDDDDDAAAAAAAAARRRRRRRRRRRRRR Detected")
                                data.front_lidar_detection = True
                    # proverava zadnju stranu ako je ukljucena detekcija
                    elif ((angle < 180 + self.back_cone/2) and
                          (angle >= 180 - self.back_cone/2)) and \
                            distance < self.distance and \
                            data.lidar == Sensors.BACK_ON:
                        x, y = self.transform.lidar2table(
                            data.x_current, data.y_current, distance, angle, data.f_current)

                        if 50 < x < 1950 and 50 < y < 2950:
                            dist = euclidian_distance(
                                x, data.x_current, y, data.y_current)

                            if dist < data.lidar_view:
                                print("LIIIIIIDDDDDDDDDDAAAAAAAAARRRRRRRRRRRRRR Detected")
                                data.back_lidar_detection = True
                    else:
                        # print("LIDAR ALL OFF")
                        data.back_lidar_detection = False
                        data.front_lidar_detection = False

                        # plt.plot(y, x, "-ro")

            # plt.draw()
            # plt.pause(0.01)

            # print(scan_data)

        except Exception as e:
            # plt.show()
            print(f"LIDAR SCAN ERROR: {e}")

        self.stop()

    def stop(self):
        try:
            self.lidar.stop()
            self.lidar.stop_motor()
            print("DISCONNECTING")
            self.lidar.disconnect()
            time.sleep(0.1)
        except Exception as e:
            print(f"LIDAR ERROR: {e}")


if __name__ == "__main__":
    try:
        data.running.set()
        detection = LidarDetection()
        detection.start()
        while True:
            print("HELLOO")
            time.sleep(2)

    except KeyboardInterrupt:
        # plt.show()
        print("Zavrsavam u mainu")
        data.running.clear()
        if detection.lidar_thread.is_alive():
            detection.lidar_thread.join()
