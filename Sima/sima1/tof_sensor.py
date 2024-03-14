import serial
import data
import threading
import sys
import time

def read_distance(serial_port:serial.Serial):
    while True:
        serial_port.write([0x01,0x03,0x00,0x10,0x00,0x01,0x85,0xCF])
        read = serial_port.read(7)
        # serial_port.flush()
        msg_length = sys.getsizeof(read)
        if msg_length == 24:
            data.distance = (read[3]<<8) + read[4]
        else:
            data.distance = 1000
        print(f"Read distance {data.distance}, read {read}, msg {msg_length}")
        time.sleep(0.05)
        # serial_port.flush()

def run_sensor(port : serial.Serial):
    tof_thread = threading.Thread(target=read_distance, args=[port])
    tof_thread.start()


if __name__ == "__main__":
    tof_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)
    read_distance(tof_port)
