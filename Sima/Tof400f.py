# import smbus2
# import time

# # Define I2C address of TOF400F sensor
# TOF400F_ADDRESS = 0x6e

# # Define registers for TOF400F sensor
# TOF400F_DISTANCE_REGISTER = 0x00
# TOF400F_STATUS_REGISTER = 0x01

# # Create I2C bus instance
# try:
#     bus = smbus2.SMBus(1)  # Change to 0 if you're using Raspberry Pi 1 or 0
#     time.sleep(.5)
#     print("BUS OTVOREN")
# except:
#     bus = smbus2.SMBus(1)
#     time.sleep(.5)

# def read_distance():
#     try:
#         # Read distance data from TOF400F sensor
#         distance_data = bus.read_i2c_block_data(TOF400F_ADDRESS, TOF400F_DISTANCE_REGISTER, 2)
#         distance = (distance_data[0] << 8) | distance_data[1]
#         return distance
#     except IOError:
#         print("Error: Device not found")
#         return None

# def read_status():
#     try:
#         # Read status data from TOF400F sensor
#         status = bus.read_byte_data(TOF400F_ADDRESS, TOF400F_STATUS_REGISTER)
#         return status
#     except IOError:
#         print("Error: Device not found")
#         return None

# def main():
#     while True:
#         distance = read_distance()
#         status = read_status()
#         if distance is not None and status is not None:
#             print("Distance:", distance, "mm")
#             print("Status:", bin(status))
#         time.sleep(1)

# if __name__ == "__main__":
#     main()



# import VL53L1X
# import time
# # Open and start the VL53L1X sensor.
# # If you've previously used change-address.py then you
# # should use the new i2c address here.
# # If you're using a software i2c bus (ie: HyperPixel4) then
# # you should `ls /dev/i2c-*` and use the relevant bus number.
# for i in range(50):
#     try:
#         tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=i)
#         time.sleep(.1)
#         tof.open()
#         tof.start_ranging(1)
#         distance_in_mm = tof.get_distance()
#         tof.stop_ranging()
#         print(f"DISTANCEEEEEEEEE : {distance_in_mm}")
#     except:
#         continue

# # Optionally set an explicit timing budget
# # These values are measurement time in microseconds,
# # and inter-measurement time in milliseconds.
# # If you uncomment the line below to set a budget you
# # should use `tof.start_ranging(0)`
# # tof.set_timing(66000, 70)

#   # Start ranging
#                       # 0 = Unchanged
#                       # 1 = Short Range
#                       # 2 = Medium Range
#                       # 3 = Long Range

# # Grab the range in mm, this function will block until
# # a reading is returned.




import serial
import sys 

def read_distance(serial_port:serial.Serial):
    print("Citam distancu")
    # SlaveAddr, FuncNumb, RegisterHighAddr, RegisterLowAddr, DataHigh, DataLow, CRC_CheckLow, CRC_CheckHigh
    try:
        serial_port.write([0x01,0x03,0x00,0x10,0x00,0x01,0x85,0xCF])
    except Exception as e:
        print(f"Write error" + str(e))

    try:
        print(serial_port.bytesize())
        read = serial_port.read(7) # response 7 bytes: SlaveAddr, FuncNumb, NumOfDataBytes, DataHigh, DataLow, ... , CRC_CheckLow, CRC_CheckHigh
    except Exception as e:
        print(f"Write error" + str(e))

    if sys.getsizeof(read) == 24:
        return (read[3]<<8) + read[4]
    else:
        return None

if __name__ == "__main__":
    print("CODE STARTED")

    try:
        serial_port = serial.Serial(port ='/dev/ttyAMA0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)
    except Exception as e:
        print(e)

    try:
        while True:
            distance = read_distance(serial_port)
            print(f"Distance: {distance}")

    except KeyboardInterrupt:
        serial_port.close()