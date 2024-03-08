import serial
import time
import sys 

distance = 0
serial_port = None

def read_distance():
    global distance
    while True:
        serial_port.write([0x01,0x03,0x00,0x10,0x00,0x01,0x85,0xCF])
        read = serial_port.read(7)
        if sys.getsizeof(read) == 24:
            distance = (read[3]<<8) + read[4]
        else:
            distance = 1000

def init_tof():
    global serial_port
    serial_port = serial.Serial('/dev/ttyS0')
    return serial_port

if __name__ == "__main__":
    print("CODE STARTED")
    time.sleep(0.1)
    serial_port = init_tof()
    try:
        read_distance()
        print("Distance:", distance)

    except KeyboardInterrupt:
        serial_port.close()