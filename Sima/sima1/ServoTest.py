from XM330 import *
import time

# L = 128.7
# d = 64



parallel_rotate([1, 4], [0, 0])
time.sleep(0.5)
parallel_rotate([1, 4], [-1800, 1800])
time.sleep(2.0)
parallel_rotate([1, 4], [0, 0])

