import serial
import time
import sys 
def read_distance(serial_port):
    # SlaveAddr, FuncNumb, RegisterHighAddr, RegisterLowAddr, DataHigh, DataLow, CRC_CheckLow, CRC_CheckHigh
    serial_port.write([0x00,0x03,0x00,0x10,0x00,0x01,0x84,0x1E])
    # serial_port.write([0x01,0x03,0x00,0x10,0x00,0x01,0x85,0xCF]) # Read distance 
    # serial_port.write([0x02,0x03,0x00,0x10,0x00,0x01,0x85,0xFC])
    # serial_port.write([0x03,0x03,0x00,0x10,0x00,0x01,0x84,0x2D])
    # serial_port.write([0x04,0x03,0x00,0x10,0x00,0x01,0x85,0x9A])
    # serial_port.write([0x05,0x03,0x00,0x10,0x00,0x01,0x84,0x4B])
    # serial_port.write([0x06,0x03,0x00,0x10,0x00,0x01,0x84,0x78])

    # --------------------------------------------------------------------#
    # serial_port.write([0x01, 0x06, 0x00, 0x01, 0xAA, 0x55, 0x8E, 0X66]) # Restore default parameter
    # --------------------------------------------------------------------#
    # serial_port.write([0x00, 0x06, 0x00, 0x02, 0x00, 0x05, 0xC3, 0XE9])

    read = serial_port.read(7) # response 7 bytes: SlaveAddr, FuncNumb, NumOfDataBytes, DataHigh, DataLow, ... , CRC_CheckLow, CRC_CheckHigh
    # 3. BYTE HIGH DATA REGISTER 4. BYTE LOW DATA REGISTER
    print(read)
    print(sys.getsizeof(read))
    if sys.getsizeof(read) == 24:
        return (read[3]<<8) + read[4]
    else:
        return None

if __name__ == "__main__":
    print("CODE STARTED")
    serial_port = serial.Serial(port ='/dev/ttyS0', baudrate = 115200, bytesize = 8, parity = 'N', stopbits = 1, timeout = 1)

    try:
        while True:
            distance = read_distance(serial_port)
            print("Distance:", distance)
            print("while")
            # time.sleep(0.1)

    except KeyboardInterrupt:
        serial_port.close()