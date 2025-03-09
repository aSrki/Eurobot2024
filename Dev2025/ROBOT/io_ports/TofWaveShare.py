import serial
import time
import sys

TOF_length = 16
# 0x57, 0x00, 0xff
TOF_header = (87, 0, 255)

ser = serial.Serial('/dev/ttyS0', 115200)
ser.flushInput()

def verifyCheckSum(data, length): 
    TOF_check = 0
    for k in range(0, length - 1):
        TOF_check += data[k]
    TOF_check = TOF_check % 256
    
    if TOF_check == data[length - 1]:
        return 1
    else:
        return 0


def read_tof(command):
    ser.write(command)
    #time.sleep(0.05)
    response = ser.read(16)
    # print(f"RESOPONSEEE VELICINAAAAAAAAAAAAAAAAAAAAAAAAAAAA {len(response)}")
    return response

max_count = 0
prev_time = time.time()

command = [bytes([0x57, 0x10, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0x63]),     # command Tof_ID = 0
            bytes([0x57, 0x10, 0xFF, 0xFF, 0x01, 0xFF, 0xFF, 0x64]),    # command Tof_ID = 1
            bytes([0x57, 0x10, 0xFF, 0xFF, 0x02, 0xFF, 0xFF, 0x65])     # command Tof_ID = 2
]
flag = 0
while True:

    curr_time = time.time()
    time_diff = (curr_time - prev_time)
    # print(time_diff)
    TOF_data = []

    

    for i in range(len(command)):
        TOF_data = read_tof(command[i])
        # print(' '.join(hex(x)[2:].zfill(2) for x in TOF_data))
        print(TOF_data.hex(' '))

        if len(TOF_data) == 16:
            if (TOF_data[0] == TOF_header[0] 
            and TOF_data[1] == TOF_header[1]
            and TOF_data[2] == TOF_header[2]
            and verifyCheckSum(TOF_data, TOF_length)):
            
                
                max_count+=1
                
                signal_val = (TOF_data[12]) | (TOF_data[13] << 8)
                if signal_val == 0:
                    print("\rOut of range!",)
                else:
                    print(f"ID {TOF_data[3]}")
                    TOF_distance = (TOF_data[8]) | (TOF_data[9] << 8) | (TOF_data[10] << 16)
                    print(f"TOF distance is: {TOF_distance} mm")
                    if 12 < TOF_distance < 300:
                        # print("Smeta mi laser AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        flag = 1
                    sys.stdout.flush()
    # if flag == 1:
    #     break
        
    
    if time_diff > 1:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(f"COUNT U 1 sekundi {max_count/ len(command)}")
        print(time_diff)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        prev_time = curr_time
        max_count = 0