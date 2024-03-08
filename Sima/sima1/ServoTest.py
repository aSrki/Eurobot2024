from XM330 import *
import time

# L = 128.7
# d = 64



parallel_rotate([1, 4], [0, 0])
time.sleep(1)
l, r = read_curr_pos_group()
print(f"L:{l}, R:{r}")

parallel_rotate([1, 4], [360, -360])
time.sleep(1)
l, r = read_curr_pos_group()
print(f"L:{l}, R:{r}")

