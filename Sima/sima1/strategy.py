from moving import *
from Tof400f import *
from tof_sensor import *
import threading

first_stopped = False

tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

threading.Thread(target=read_distance, args = [tof_port]).start()

init_sima()
translate(1500)

while not first_stopped:
    if data.distance < 200:
        print("Mali dist")
        first_stopped = True
        stop_sima()

# rotate(90)
# translate(900)
# rotate(-90)
# translate(400)
# rotate(90)
# translate(600)