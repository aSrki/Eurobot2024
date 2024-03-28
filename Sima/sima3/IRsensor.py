import RPi.GPIO as GPIO
import time

sensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# za detekciju vraca 1 .....
try: 
    while True:
        print(GPIO.input(sensor))
        if not GPIO.input(sensor):
            print("Object Detected")
        else:
            print("Not detected")
        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()