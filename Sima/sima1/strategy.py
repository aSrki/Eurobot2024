from moving import *
from Tof400f import *
from tof_sensor import *
import threading
import data
import time

first_stopped = False

tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

threading.Thread(target=read_distance, args = [tof_port]).start()
threading.Thread(target=stop_sima).start()
init_sima()
translate(200)
rotate(90)
translate(900)
rotate(-90)
translate(400)
rotate(90)
translate(600)