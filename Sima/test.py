from servo_init import *
from XL430 import *
from enc import *
import threading
import time

def odom():
	try:
		while True:
			if EncXL430.permission == 1:
				read_positions([1,4])
			time.sleep(0.0005)
	except KeyboardInterrupt:
		send_velocity_multiple([1,4],[0,0])
		thread.join()
        

thread = threading.Thread(target=odom)
thread.start()

send_velocity_multiple([1,4],[-50,-50])
time.sleep(2)
send_velocity_multiple([1,4],[0,0])
time.sleep(2)
send_velocity_multiple([1,4],[100,100])
time.sleep(2)
send_velocity_multiple([1,4],[0,0])