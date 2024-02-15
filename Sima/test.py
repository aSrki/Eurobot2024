from servo_init import *
from XL430 import *
from enc import *
import threading
import time
from odom import *

# Problem 1
# Ako je init klase pre starta thread-a procita dobro.. ako je odma nakon trhreada cita 0, 0
# 1 resenje initi svih klasa pre starta bilo kog thread-a

# print("--------------------------------------")
# print("--------------------------------------")
# print("--------------------------------------")
# Odom = odom(100, 100, 0, 0)
# print("--------------------------------------")
# print("--------------------------------------")
# print("--------------------------------------")

# Problem 2
# Pored EncXL430.permission i dalje ima problem sa citanjem jer thread upadne pre seta promenljive
# Uvodjenjem promenljive se smanjio broj citanja 0 tokom upisivanja
# 1 resenje provera citanje trenutno i prethodno ako su oba 0 usvojiti, ako ne citati ponovo
# 2 resenje samo odbaciti 0 i citati opet

# def ODOM():
# 	try:
# 		while True:
# 			if EncXL430.permission == 1:
# 				read_positions([1,4])
# 			time.sleep(0.0005)
# 	except KeyboardInterrupt:
# 		send_velocity_multiple([1,4],[0,0])
# 		thread.join()
        

# thread = threading.Thread(target=ODOM)
# thread.start()

# time.sleep(0.5)

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
odom = Odom(100, 100, 0, 0)
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

# time.sleep(0.5)
# ID_1 MOTOR RIGHT
# ID_4 MOTOR LEFT
try:
	odom.run_odom()
	# send_velocity_multiple([1,4],[-50,50])	# forward
	# time.sleep(2)
	# send_velocity_multiple([1,4],[0,0])
	# time.sleep(1)
	# send_velocity_multiple([1,4],[50,-50])	# backward
	# time.sleep(2)
	# send_velocity_multiple([1,4],[0,0])
	# time.sleep(1)
	# send_velocity_multiple([1,4],[50,50])	# - 
	# time.sleep(2)
	# send_velocity_multiple([1,4],[0,0])
	# time.sleep(1)
	# send_velocity_multiple([1,4],[-50,-50]) # +
	# time.sleep(2)
	# send_velocity_multiple([1,4],[0,0])
	# time.sleep(1)    

	# square
	odom.go_to_XY(300,100)
	odom.go_to_XY(300,300)
	odom.go_to_XY(100,300)
	odom.go_to_XY(100,100)
      
	# odom.go_to_XY(1150,100)      
	# odom.go_to_XY(-2000,100) 

	# odom.go_to_XY(600,100)
	# odom.go_to_XY(100,300)

except KeyboardInterrupt:
    odom.stop_odom()


# send_velocity_multiple([1,4],[-50,-50])
# time.sleep(1)
# send_velocity_multiple([1,4],[0,0])
# time.sleep(1)