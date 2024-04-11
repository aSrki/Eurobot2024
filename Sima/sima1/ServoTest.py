from XM330 import *
import time

# L = 128.7
# d = 64

init_servos([1, 4])
parallel_rotate([1, 4], [10000, 10000])

rotate_arm(330)
time.sleep(1)
rotate_arm(236)
