from XM330 import *
import time
from math import *
from data import *

def rotate(deg):
    global left_theta
    global right_theta

    theta = int((((deg * L/2)/d)))

    if deg >= 0:
        left_theta -= theta
        right_theta -= theta
        parallel_rotate([1, 4], [left_theta, right_theta])
    else:
        left_theta -= theta
        right_theta -= theta
        parallel_rotate([1, 4], [left_theta, right_theta])
    time.sleep(.5)
    print(f"Theta {theta}")
    print(f"LTheta {left_theta}")
    print(f"RTheta {right_theta}")

def translate(len):
    global left_theta
    global right_theta
    theta = int((len/(2*d*pi))*360)
    if len >= 0:
        left_theta += theta
        right_theta -= theta
        parallel_rotate([1, 4], [left_theta, right_theta])
    else:
        left_theta += theta
        right_theta -= theta
        parallel_rotate([1, 4], [left_theta, right_theta])    
    time.sleep((len/300))

def init_sima():
    parallel_rotate([1, 4], [0, 0], 4000)
    time.sleep(5)
    print("Init done!")

def go_to_xy(x, y):
    dx = x - curr_x
    dy = y - curr_y
    theta = degrees(atan2(dy, dx)) + curr_a
    d = sqrt((dy ** 2) + (dx ** 2))
    print(f"dx : {dx}")
    print(f"dy : {dy}")
    print(f"theta : {theta}")
    print(f"d : {d}")

    rotate(theta)
    time.sleep(1)
    translate(d)
    time.sleep(1.5)

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
