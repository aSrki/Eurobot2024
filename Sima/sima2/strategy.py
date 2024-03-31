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

init_sensor()
init_sima()
move_arm(180)

while True:
    comm_data = ""
    print("STARTED")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    while comm_data == "":
        conn, addr = s.accept()
        comm_data = conn.recv(1024).decode()

    print(f"Received {comm_data}")
    conn.close()

    move_arm(180)

    distance_acquire_thread = threading.Thread(
        target=read_distance, daemon=True)
    stop_sima_thread = threading.Thread(target=stop_sima)

    data.start_time = time.time()

    time.sleep(91)

    init_sima()
    move_arm(180)

    data.stop_threads = False

    distance_acquire_thread.start()
    stop_sima_thread.start()

    if comm_data == 'yellow':
        translate(20)
        rotate(90)
        translate(1100, False)
        rotate(-45)

    elif comm_data == 'blue':
        translate(20)
        rotate(-90)
        translate(1100, False)
        rotate(45)

    move_arm(270)

    data.stop_threads = True
    print("Ovde sam 1")
    distance_acquire_thread.join()
    print("Ovde sam 2")
    stop_sima_thread.join()
    print("Ovde sam 3")

    data.stop_threads = False

    # stop_moving()

    print("DONE")
