import sys
if __name__ == '__main__':
    sys.path.append("..")

import serial
import time
import data


# MAX_INPUT_SPEED = 14400
# MIN_INPUT_SPEED = -14400


class MaxonCommunication:
    def __init__(self):
        self.serial = serial.Serial(
            port=data.STM_PORT,
            baudrate=256000,
            timeout=0.001,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)

        self.debug = True
        self.delay = 0.00001
        time.sleep(self.delay)

    def init_motors_communication(self):
        # zbog toga kako radi stm mora da bude 14 karaktera poslato
        self.serial.write("S".encode('ascii'))

        if self.debug:
            print("Sent S")

        time.sleep(self.delay)

    def stop_motors_communication(self):

        self.serial.write("+00000,+00000;".encode('ascii'))
        time.sleep(self.delay)
        self.serial.write("RRRRRRRRRRRRRR".encode('ascii'))

        if self.debug:
            print("Sent Reset")

        time.sleep(self.delay)

    def set_motor_velocities(self, motor1_vel, motor2_vel):
        output = ""
        # sign1, sign2 = 1, 1
        # if motor1_vel < 0:
        #     sign1 = 1
        # else:
        #     sign1 = -1

        # if motor2_vel < 0:
        #     sign2 = 1
        # else:
        #     sign2 = -1

        # if abs(motor1_vel) < 1200:
        #     motor1_vel = 1200*sign1

        # if abs(motor2_vel) < 1200:
        #     motor2_vel = 1200*sign2

        if motor1_vel < 0:  # LEVI
            output = "-" + str(abs(int(motor1_vel))).zfill(5) + ","
        else:
            output = "+" + str(int(motor1_vel)).zfill(5) + ","

        if motor2_vel < 0:  # DESNI
            output += "-" + str(abs(int(motor2_vel))).zfill(5) + ";"
        else:
            output += "+" + str(int(motor2_vel)).zfill(5) + ";"

        if self.debug:
            print(f"PWM : {output}")
            print(f"Length : {len(output)}")

        self.serial.write(output.encode('ascii'))
        time.sleep(self.delay)


if __name__ == "__main__":
    try:
        # ser = serial.Serial(
        #     port='/dev/ttyACM_STM',
        #     baudrate=256000,
        #     timeout=0.001,
        #     parity=serial.PARITY_NONE,
        #     stopbits=serial.STOPBITS_ONE,
        #     bytesize=serial.EIGHTBITS)

        # ser.reset_output_buffer()
        # ser.write("STARTTTTTTTTTT".encode('ascii'))
        # ser.reset_output_buffer()
        # ser.write("+02000,+02000;".encode('ascii'))
        # ser.reset_output_buffer()
        # ser.write("STOPPPPPPPPPPP".encode('ascii'))

        maxon = MaxonCommunication()
        time.sleep(.1)
        maxon.init_motors_communication()

        # maxon.set_motor_velocities(2000, 2000)
        # time.sleep(2)
        # maxon.set_motor_velocities(0, 0)
        # time.sleep(2)
        # maxon.set_motor_velocities(-2000, -2000)
        # time.sleep(2)
        #maxon.set_motor_velocities(0, 0)

        while True:
            # output = input("message: ")
            # for i in range(2):
            #     maxon.serial.reset_output_buffer()
            #     maxon.serial.write(bytes(output, 'ascii'))
            input_speed1 = int(input("input speed1: "))
            input_speed2 = int(input("input speed2: "))
            maxon.set_motor_velocities(input_speed1, input_speed2)
    except(KeyboardInterrupt, SystemExit):
        maxon.stop_motors_communication()
