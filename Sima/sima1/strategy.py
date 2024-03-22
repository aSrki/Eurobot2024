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

tof_port = serial.Serial(port='/dev/ttyS0', baudrate=115200,
                         bytesize=8, parity='N', stopbits=1, timeout=1)

init_sima()
init_sensor()

while True:
    print("STARTED")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    conn, addr = s.accept()
    comm_data = conn.recv(1024).decode()

    print(f"Received {comm_data}")
    conn.close()

    distance_acquire_thread = threading.Thread(
        target=read_distance, daemon=True)
    stop_sima_thread = threading.Thread(target=stop_sima)

    data.start_time = time.time()

    time.sleep(5)

    data.stop_threads = False

    distance_acquire_thread.start()
    stop_sima_thread.start()

    if comm_data == 'yellow':
        translate(200)
        rotate(90)
        translate(700)
        translate(370, False)
        print("yellow gotov")

    elif comm_data == 'blue':
        translate(200)
        rotate(-90)
        translate(700)
        translate(370, False)
        print("blue gotov")

    data.stop_threads = True
    print("Ovde sam 1")
    distance_acquire_thread.join()
    print("Ovde sam 2")
    stop_sima_thread.join()
    print("Ovde sam 3")

    data.stop_threads = False

    stop_moving()

    print("DONE")
