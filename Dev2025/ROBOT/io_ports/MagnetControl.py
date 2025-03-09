import RPi.GPIO as GPIO
import time

class MagnetControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        # Initialize all magnet pins
        # 17 DESNA RUKA
        # 18 ZID NAPRED
        # 20 LEVA RUKA
        # 27 ZID NAZAD
        self.magnet_pins = [17, 18, 20, 27]
        for pin in self.magnet_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)  # Start with magnets off
    
    def left_arm_on(self):
        GPIO.output(self.magnet_pins[2], GPIO.LOW)

    def left_arm_off(self):
        GPIO.output(self.magnet_pins[2], GPIO.HIGH)

    def right_arm_on(self):
        GPIO.output(self.magnet_pins[0], GPIO.LOW)

    def right_arm_off(self):
        GPIO.output(self.magnet_pins[0], GPIO.HIGH)

    def front_wall_on(self):
        GPIO.output(self.magnet_pins[1], GPIO.LOW)

    def front_wall_off(self):
        GPIO.output(self.magnet_pins[1], GPIO.HIGH)

    def back_wall_on(self):
        GPIO.output(self.magnet_pins[3], GPIO.LOW)

    def back_wall_off(self):
        GPIO.output(self.magnet_pins[3], GPIO.HIGH)



    def all_on(self):
        """Turn all magnets on"""
        print("Magnets ON")
        for pin in self.magnet_pins:
            GPIO.output(pin, GPIO.LOW)
    
    def all_off(self):
        """Turn all magnets off"""
        print("Magnets OFF")
        for pin in self.magnet_pins:
            GPIO.output(pin, GPIO.HIGH)
    
    def cleanup(self):
        """Clean up GPIO resources"""
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        magnet = MagnetControl()
        # TEST 
        # time.sleep(1)
        # print("POCETAK")
        # print("LEVA RUKA")
        # magnet.left_arm_on()
        # time.sleep(1)
        # magnet.left_arm_off()
        # time.sleep(1)

        # print("DESNA RUKA")
        # magnet.right_arm_on()
        # time.sleep(1)
        # magnet.right_arm_off()
        # time.sleep(1)

        # print("ZID NAPRED")
        # magnet.front_wall_on()
        # time.sleep(1)
        # magnet.front_wall_off()
        # time.sleep(1)

        # print("ZID NAZAD")
        # magnet.back_wall_on()
        # time.sleep(1)
        # magnet.back_wall_off()
        # time.sleep(1)

        # print("SVE")
        # magnet.all_on()
        # time.sleep(3)
        # magnet.all_off()
        # time.sleep(1)
        # print("KRAJ")

        print(f"GPIO : {magnet.magnet_pins}")
        while True:
            gpio, state = map(int, input("Unesi dve vrednosti odvojene razmakom (GPIO) (0 iskljuceno, 1 ukljuceno): ").split())

            if state == 1:
                GPIO.output(gpio, GPIO.LOW)
            else:
                GPIO.output(gpio, GPIO.HIGH)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    finally:
        GPIO.cleanup()
