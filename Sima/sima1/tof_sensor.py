import serial
import data
import threading
import sys
import time

def read_distance(serial_port:serial.Serial):
    print("VAJL")
    serial_port.write([0x01,0x03,0x00,0x10,0x00,0x01,0x85,0xCF])
    read = serial_port.read(7)
    msg_length = sys.getsizeof(read)
    if msg_length == 24:
        data.distance = (read[3]<<8) + read[4]
    else:
        data.distance = 1000
    print(data.distance)

def run_sensor(port : serial.Serial):
    tof_thread = threading.Thread(target=read_distance, args=[port])
    tof_thread.start()