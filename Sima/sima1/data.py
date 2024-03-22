import threading

L = 125
d = 75/2

start_time = 0

stopped = False
detect = True

stop_threads = False

IP = '192.168.0.23'

left_theta = 0
right_theta = 0

curr_x = 2000 - 145/2
curr_y = 1500 - 75
curr_a = 90

distance = 10000

old_left = 0
old_right = 0
