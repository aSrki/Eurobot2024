from moving import *
from Tof400f import *
from sensor import *
import threading
import data
import time
import socket

first_stopped = False

host = '0.0.0.0'
port = 12345

tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

init_sima()
init_sensor()

threading.Thread(target=read_distance).start()
threading.Thread(target=stop_sima).start()

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    comm_data = conn.recv(1024).decode()
    print(f"Received {comm_data}")
    conn.close()

    time.sleep(90)

    if comm_data == 'yellow':
        translate(200)
        rotate(90)
        translate(900)
        rotate(-90)
        translate(400)
        rotate(90)
        translate(600, False)
    elif comm_data == 'blue':
        translate(200)
        rotate(-90)
        translate(900)
        rotate(90)
        translate(400)
        rotate(-90)
        translate(600, False)
    print("DONE")