import RPi.GPIO as GPIO
import time

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)



try:
  while True:
    print("ON")
    GPIO.output(servoPIN, 1) #DUVA
    time.sleep(1)
    print("OFF")
    GPIO.output(servoPIN, 0)  #UVLACI
    time.sleep(1)


except KeyboardInterrupt:
  GPIO.cleanup()