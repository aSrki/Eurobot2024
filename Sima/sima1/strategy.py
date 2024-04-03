from moving import *
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
move_arm(225)

while True:
    print("STARTED")

    comm_data = ""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)


    while comm_data == "":
        conn, addr = s.accept()
        comm_data = conn.recv(1024).decode()

    print(f"Received {comm_data}")
    move_arm(225)
    conn.close()

    distance_acquire_thread = threading.Thread(
        target=read_distance, daemon=True)
    stop_sima_thread = threading.Thread(target=stop_sima)

    data.start_time = time.time()

    time.sleep(90)
    init_sima()
    move_arm(225)

    data.stop_threads = False

    distance_acquire_thread.start()
    stop_sima_thread.start()

    if comm_data == 'yellowsiroki':
        translate(300)
        rotate(90)
        translate(600, False)
        rotate(-90)
        translate(250, False)
        rotate(90)
        translate(500, False)

    elif comm_data == 'bluesiroki':
        translate(300)
        rotate(-90)
        translate(600, False)
        rotate(90)
        translate(250, False)
        rotate(-90)
        translate(500, False)

    elif comm_data == 'yellowuski':
        translate(300)
        rotate(90)
        translate(400, False)
        rotate(-90)
        translate(250, False)
        rotate(90)
        translate(700, False)

    elif comm_data == 'blueuski':
        translate(300)
        rotate(-90)
        translate(400, False)
        rotate(90)
        translate(250, False)
        rotate(-90)
        translate(700, False)

    move_arm(330)

    data.stop_threads = True
    print("Ovde sam 1")
    distance_acquire_thread.join()
    print("Ovde sam 2")
    stop_sima_thread.join()
    print("Ovde sam 3")

    data.stop_threads = False

    # stop_moving()

    print("DONE")
