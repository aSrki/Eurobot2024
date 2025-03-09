from roboclaw_python.roboclaw_3 import Roboclaw
import time


port = "/dev/tty_TTLroboclaw"
baud = 38400

try:
    roboclaw = Roboclaw(port, baud)
    print(f"Opening roboclaw port at {port}")
    roboclaw.Open()
except:
    print(f"Error opening roboclaw port at {port}")
    exit()

encoder_1_count = roboclaw.SetEncM1(0x80, 0)
encoder_2_count = roboclaw.SetEncM2(0x80, 0)

print(encoder_1_count)
print(encoder_2_count)
max_speed = 1_600_000
procenat_brzine = 80
brzina = max_speed * procenat_brzine/100

brzina = 200000
# broj_krugova = 3.5
impulsi_jedan_krug= 106496



# SpeedDistanceM1(address,speed,distance,buffer)
# roboclaw.SetM1PositionPID(0x80, 70, 2, 5000, 25768, 0, 0, 2000000)

# print("SpeedAccelDeccelPositionM1")
# roboclaw.SpeedAccelDeccelPositionM1(0x80, 9000000, brzina, 10000000, broj_krugova * impulsi_jedan_krug, 1)

print("SpeedAccelDeccelPositionM2")
pos = 0
broj_krugova = 2
pos += round(broj_krugova * impulsi_jedan_krug)
print(f"POZICIJAAAAA {pos}")
roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
time.sleep(5)

# broj_krugova = 1
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)

# MOTOR 2

# broj_krugova = 2
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)


# broj_krugova = 0.5
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)


# broj_krugova = 3.5
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)

# broj_krugova = 0.6
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)

# broj_krugova = 0.6
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM2(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)




# MOTOR 1
# broj_krugova = 2
# pos += round(broj_krugova * impulsi_jedan_krug)
# print(f"POZICIJAAAAA {pos}")
# roboclaw.SpeedAccelDeccelPositionM1(0x80, 1000000000, brzina, 10000000, round(broj_krugova * impulsi_jedan_krug), 1)
# time.sleep(5)






































#***Before using this example the motor/controller combination must be
#***tuned and the settings saved to the Roboclaw using IonMotion.
#***The Min and Max Positions must be at least 0 and 50000

# import time
# from roboclaw_python.roboclaw_3 import Roboclaw

# # Windows comport name
# # rc = Roboclaw("COM3",115200)
# # Linux comport name
# rc = Roboclaw("/dev/ttyACM0", 38400)

# def displayspeed():
#     enc1 = rc.ReadEncM1(address)
#     enc2 = rc.ReadEncM2(address)
#     speed1 = rc.ReadSpeedM1(address)
#     speed2 = rc.ReadSpeedM2(address)

#     print("Encoder1:", end=" ")
#     if(enc1[0]==1):
#         print(enc1[1], format(enc1[2],'02x'), end=" ")
#     else:
#         print("failed", end=" ")

#     print("Encoder2:", end=" ")
#     if(enc2[0]==1):
#         print(enc2[1], format(enc2[2],'02x'), end=" ")
#     else:
#         print("failed", end=" ")

#     print("Speed1:", end=" ")
#     if(speed1[0]):
#         print(speed1[1], end=" ")
#     else:
#         print("failed", end=" ")

#     print("Speed2:", end=" ")
#     if(speed2[0]):
#         print(speed2[1])
#     else:
#         print("failed")

# rc.Open()
# address = 0x80

# version = rc.ReadVersion(address)
# if version[0]==False:
#     print("GETVERSION Failed")
# else:
#     print(repr(version[1]))

# while(1):
#     rc.SpeedAccelM1(address,120000,12000)
#     rc.SpeedAccelM2(address,120000,-12000)
#     for i in range(0,200):
#         displayspeed()
#         time.sleep(0.01)

#     rc.SpeedAccelM1(address,120000,-12000)
#     rc.SpeedAccelM2(address,120000,12000)
#     for i in range(0,200):
#         displayspeed()
#         time.sleep(0.01)