import serial
import data
import threading
import sys
import time
import RPi.GPIO as GPIO   

def init_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_distance():
    while not data.stop_threads:
        data.distance = GPIO.input(5)
        time.sleep(0.1)


def run_sensor(port : serial.Serial):
    tof_thread = threading.Thread(target=read_distance, args=[port])
    tof_thread.start()


if __name__ == "__main__":
    init_sensor()
    read_distance()
