from can_comm import *
from position import *

can_comm = CAN_COMM()
can_comm.start()

pose = Position()
pose.start()
