import math
import sys
import os
import threading
import time
import traceback
import subprocess
from shapely.geometry import LineString, Point, Polygon
from math import cos, sin, pi, floor, sqrt, degrees, atan
from communication_with_main_process import Communication
from global_var import *
import global_var
from adafruit_rplidar import RPLidar
# import data

# Setup the RPLidar
lidar = RPLidar(None, '/dev/ttyUSB_LIDAR', timeout=3)


def arg_finder(arg_finde):
    for arg in sys.argv:
        if arg == arg_finde:
            return True
    return False


def initialize_lidar():
    global fd_read1, fd_write1
    global fd_read2, fd_write2
    fd_read1, fd_write1 = os.pipe()  # for parent -> child writes
    fd_read2, fd_write2 = os.pipe()  # for child ->paren writes
    print("DESKRIPTORI   :  ", fd_read1, fd_write1,
          fd_read2, fd_write2)  # for parent -> child writes

    if arg_finder('d'):
        subprocess.Popen(["python3.7", "obstacle_detector.py", str(fd_read2), str(fd_write1), 'd'],
                         pass_fds=(fd_read2, fd_write1),
                         cwd="/home/malirobot/robot/lidar")
    else:
        subprocess.Popen(["python3.7", "obstacle_detector.py", str(fd_read2), str(fd_write1)],
                         pass_fds=(fd_read2, fd_write1),
                         cwd="/home/malirobot/robot/lidar")

    print("Inicijalizovan PIPE")
    time.sleep(.3)


if arg_finder('d'):
    display_lidar = True

try:

    if display_lidar:
        from lidar_display import LidarDisplay

        Display = LidarDisplay()

except:
    traceback.print_exc()
    print("unexpected error :", sys.exc_info()[0])
    print('Stoping.')
    lidar.set_pwm(0)
    lidar.stop()
    lidar.disconnect()

    sys.exit()


class ObstacleDetection:
    frontdetected = False
    backdetected = False

    communication = Communication()

    def __init__(self):
        try:

            self.debug_comm = True
            self.debug = True

            self.distance = 0
            self.is_detection = False
        except:
            traceback.print_exc()
            print("unexpected error :", sys.exc_info()[0])
            print('Stoping.')
            lidar.set_pwm(0)
            lidar.stop()
            lidar.disconnect()
            sys.exit()

    def start(self):

        thread = threading.Thread(target=self.detection).start()

    def detection(self):

        scanned_angles = [0] * 360

        for i in range(0, 360):
            scanned_angles[i] = 0
            scanned_data[i] = 100000000

        # Broj skeniranja pre ciscenja
        num_of_scanned = 0
        max_num_of_scanned = 3

        # Uzimanje podataka iz lidara
        for scan in lidar.iter_scans():

            # inicijalizacija parametara novog kruga skeniranja

            end_angle = start_angle = 0

            # cisti stare vrednosti

            if num_of_scanned == max_num_of_scanned:
                num_of_scanned = 0

                for i in range(0, 360):
                    if not scanned_angles[i]:
                        scanned_data[i] = 100000000
                    scanned_angles[i] = 0
            num_of_scanned += 1

            # uzima skenirane vrednosti  (manje od 360)
            for (_, angle, distance) in scan:
                angle = min([359, floor(angle)])
                if (360 - LIDAR_ANGLE / 2) <= angle or angle <= LIDAR_ANGLE / 2:
                    scanned_data[angle] = distance
                    scanned_angles[angle] = 1

            # ____________OBRADA SKENIRANOG  I PRAVLJENJE OBSTACLES________________________

            prev_distance1 = [10000, 10000]
            prev_distance2 = [10000, 10000]
            self.frontdetected = False
            self.backdetected = False
            for angle in range(360):

                if (UPPER_BOUNDERY > scanned_data[angle] > LOWER_BOUNDERY):

                    received_distance = scanned_data[angle]

                    x_coor = received_distance * math.sin(math.radians(angle))
                    y_coor = received_distance * math.cos(math.radians(angle))

                    if abs(y_coor) < StoppingArea.length and abs(prev_distance1[1]) < StoppingArea.length \
                            and abs(x_coor) < StoppingArea.width / 2:
                        # print(f"length  {StoppingArea.length} , width {StoppingArea.width}")
                        # print("detected at : ", x_coor, y_coor)
                        if y_coor > 0:
                            # print(f'Front detected at {y_coor}')
                            self.frontdetected = True
                            # print(f"Front {self.frontdetected}")
                        elif y_coor < 0:
                            # print(f'Back detected at {y_coor}')
                            self.backdetected = True
                            # print(f"Back {self.backdetected}")

                        self.distance = y_coor

                    prev_distance1 = [x_coor, y_coor]
                    prev_distance2 = prev_distance1

                else:
                    pass

                # ------------------------------------------------------

            if not global_var.RUN_THREADS:
                raise KeyboardInterrupt

            if __name__ == "__main__" and not arg_finder('x'):
                self.communication.write_to_main(
                    f"f{self.frontdetected};b{self.backdetected};")
            else:
                print(f"f{self.frontdetected};b{self.backdetected};")

            if display_lidar:
                Display.process_data(scanned_data, [])


if __name__ == "__main__":

    try:

        o = ObstacleDetection()
        o.detection()
        # print(o.is_detected, o.distance)

    except KeyboardInterrupt:

        print('Stoping.')

    except:
        traceback.print_exc()
        print("unexpected error :", sys.exc_info()[0])

    finally:
        lidar.set_pwm(0)
        lidar.stop()
        lidar.disconnect()
        print("kraj")
        sys.exit()
