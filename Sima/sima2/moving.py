from XM330 import *
import time
from math import *
import data

def move_arm(ang):
    rotate_arm(ang)

def stop_moving():
    r, l = read_curr_pos_group(portHandler, handler)
    l = l*360/4095
    r = r*360/4095
    print(f"STOP L:{l} R:{r}")
    parallel_rotate([4, 1], [int(l), int(r)], a = 600)

def stop_sima():
    print("radi tred")
    data.stopped = False
    while not data.stop_threads:
        if (time.time() - data.start_time) > 100:
            print(time.time() - data.start_time)
            stop_moving()
            data.stop_threads = True
            return
        if not data.stop_threads:
            if data.distance == 1 and not data.stopped and data.detect:
                print("U detekciji sam")
                r, l = read_curr_pos_group(portHandler, handler)
                l = l*360/4095
                r = r*360/4095
                print(f"DETENKCIJAAAAAAAAAAAAAAAAAAAAAAAAAAA L:{l} R:{r}")
                data.stopped = True
                parallel_rotate([4, 1], [int(l), int(r)], a = 600)
            if data.distance == 0 and data.stopped and not data.stop_threads:
                parallel_rotate([4,1], [data.old_left, data.old_right], a = 100)
                time.sleep(2)
                data.stopped = False
                print("stojim")
        time.sleep(0.05)


def rotate(deg):
    if data.stop_threads:
        return
    data.detect = False
    theta = int((((deg * data.L/2)/data.d)))
    if deg >= 0:
        data.left_theta -= theta
        data.right_theta -= theta
    else:
        data.left_theta -= theta
        data.right_theta -= theta
    data.old_left = data.left_theta
    data.old_right = data.right_theta
    parallel_rotate([4, 1], [data.left_theta, data.right_theta], a = 200)
    time.sleep(0.5)
    print("rotiram")
    data.detect = True

def translate(len, detect = True):
    print(data.stop_threads)
    if data.stop_threads:
        return
    data.detect = detect
    if not detect:
        while data.stopped == 1 and not data.stop_threads:
            time.sleep(0.01)
    theta = int((len/(2*data.d*pi))*360)
    if len >= 0:
        data.left_theta += theta
        data.right_theta -= theta
    else:
        data.left_theta += theta
        data.right_theta -= theta

    data.old_left = data.left_theta
    data.old_right = data.right_theta
    if not data.stop_threads:
        parallel_rotate([4, 1], [data.left_theta, data.right_theta], a = 100)
        print(f"idem : {len}")
        time.sleep((len/330))

def init_sima():
    print("Udao u init sima")
    init_servos([4, 1])
    r, l = read_curr_pos_group(portHandler, handler)
    data.left_theta = l*360/4095
    data.right_theta = r*360/4095
    parallel_rotate([4, 1], [data.left_theta, data.right_theta], 4000)
    print("Izassao iz init sima")
    time.sleep(.5)


if __name__ == "__main__":
    init_sima()
    while True:
        ang= int(input("Angle"))
        rotate(ang)
    # __translate(500)
    # __rotate(-90)
    # __translate(500)
    # __rotate(-90)
    # __translate(500)
    # __rotate(-90)
    # __translate(500)
    # __rotate(-90)

    # __rotate(-90)
    # __rotate(-90)
    # __rotate(-90)
    # __rotate(-90)
