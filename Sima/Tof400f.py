import smbus2
import time

# Define I2C address of TOF400F sensor
TOF400F_ADDRESS = 0x6e

# Define registers for TOF400F sensor
TOF400F_DISTANCE_REGISTER = 0x00
TOF400F_STATUS_REGISTER = 0x01

# Create I2C bus instance
bus = smbus2.SMBus(1)  # Change to 0 if you're using Raspberry Pi 1 or 0

def read_distance():
    try:
        # Read distance data from TOF400F sensor
        distance_data = bus.read_i2c_block_data(TOF400F_ADDRESS, TOF400F_DISTANCE_REGISTER, 2)
        distance = (distance_data[0] << 8) | distance_data[1]
        return distance
    except IOError:
        print("Error: Device not found")
        return None

def read_status():
    try:
        # Read status data from TOF400F sensor
        status = bus.read_byte_data(TOF400F_ADDRESS, TOF400F_STATUS_REGISTER)
        return status
    except IOError:
        print("Error: Device not found")
        return None

def main():
    while True:
        distance = read_distance()
        status = read_status()
        if distance is not None and status is not None:
            print("Distance:", distance, "mm")
            print("Status:", bin(status))
        time.sleep(1)

if __name__ == "__main__":
    main()
