from moving import *
from Tof400f import *
from tof_sensor import *

tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

while True:
    read_distance(tof_port)
# init_sima()
# translate(150)
# rotate(90)
# translate(900)
# rotate(-90)
# translate(400)
# rotate(90)
# translate(600)