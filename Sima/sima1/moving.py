from XM330 import *
import time
from math import *
import data

def stop_moving():
    l, r = read_curr_pos_group(portHandler, handler)
    l = l*360/4095
    r = r*360/4095
    parallel_rotate([1, 4], [int(l), int(r)])

def stop_sima():
    print("radi tred")
    data.stopped = False
    while not data.stop_threads:
        if data.distance == 1 and not data.stopped and data.detect:
            print("U detekciji sam")
            l, r = read_curr_pos_group(portHandler, handler)
            l = l*360/4095
            r = r*360/4095
            print(f"DETENKCIJAAAAAAAAAAAAAAAAAAAAAAAAAAA L:{l} R:{r}")
            data.stopped = True
            parallel_rotate([1, 4], [int(l), int(r)])
        if data.distance == 0 and data.stopped:
            parallel_rotate([1,4], [data.old_left, data.old_right])
            time.sleep(1)
            data.stopped = False
            print("stojim")
        time.sleep(0.05)


def rotate(deg):
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
    parallel_rotate([1, 4], [data.left_theta, data.right_theta])
    time.sleep(1)
    print("rotiram")
    data.detect = True

def translate(len, detect = True):
    data.detect = detect
    if not detect:
        while data.stopped == 1:
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
    parallel_rotate([1, 4], [data.left_theta, data.right_theta])
    print("idem")
    time.sleep((len/150))

def init_sima():
    init_servos([1,4])
    l, r = read_curr_pos_group(portHandler, handler)
    data.left_theta = l*360/4095
    data.right_theta = r*360/4095
    parallel_rotate([1, 4], [data.left_theta, data.right_theta], 4000)
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
