from XM330 import *
import time
from math import *

L = 128.7
d = 64/2

def __rotate(deg):
    theta = int((((deg * L/2)/d)))
    print(f"THETA: {theta}")
    if deg >= 0:
        print("poslao -theta")
        parallel_rotate([1, 4], [-theta, -theta])
    else:
        print("poslao theta")
        parallel_rotate([1, 4], [theta, theta])
    time.sleep(1)

def __init_sima():
    print("init")
    parallel_rotate([1, 4], [0, 0])
    time.sleep(5)

if __name__ == "__main__":
    __init_sima()
    # __rotate(90)    