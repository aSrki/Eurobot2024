from moving import *
from Tof400f import *
from sensor import *
import threading
import data
import time
import socket

first_stopped = False

tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.settimeout(0.5)
socket1.connect((data.IP, 1234))

while True:
    msg_data = socket1.recv
    print(msg_data)

init_sima()
init_sensor()



threading.Thread(target=read_distance).start()
threading.Thread(target=stop_sima).start()

translate(200)
rotate(90)
translate(900)
rotate(-90)
translate(400)
rotate(90)
translate(600, False)