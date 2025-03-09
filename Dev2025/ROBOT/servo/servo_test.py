# from XL430 import parallel_rotate
# import time

# # parallel_rotate([9, 7, 3], [300, 300, 300])

# parallel_rotate([11, 2, 8], [230, 230, 230])
# time.sleep(1)
# parallel_rotate([11, 2, 8], [140, 140, 140])

from WaveshareSC09.servo_test3 import ServoController
import time

def main():
    # Create controller
    servo = ServoController('/dev/ttyUSB0')  # Adjust port name if needed
    
    try:
        # Initialize servo settings (speed and acceleration)
        servo.packetHandler.write1ByteTxRx(servo.portHandler, servo.SCS_ID, 41, 0)  # acc
        servo.packetHandler.write2ByteTxRx(servo.portHandler, servo.SCS_ID, 46, 0)  # speed
        
        # Example movements
        print("Moving to position 1000")
        servo.move_servo(1000)
        time.sleep(1)
        
        print("Moving to position 2000")
        servo.move_servo(2000)
        time.sleep(1)
        
        print("Moving to position 3000")
        servo.move_servo(3000)
        time.sleep(1)
        
    finally:
        servo.close()

if __name__ == "__main__":
    main()