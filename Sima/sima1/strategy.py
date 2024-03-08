from moving import *
from Tof400f import *
from tof_sensor import *

tof_port = serial.Serial('/dev/ttyS0')

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