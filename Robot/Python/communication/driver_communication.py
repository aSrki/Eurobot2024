import serial
import time
if '__main__' == __name__:
    import sys
    sys.path.append("/home/mali/robot/")
import data


class DriverCommunication:
    debug = False

    def __init__(self, ki=0.0, kp=0.0, side: str = "N"):

        self.side = side
        self.enc_left = 0
        self.enc_right = 0

        self.counter = 5

        self.serial = serial.Serial(
            port= data.ESP32_PORT,
            # port='COM5',
            baudrate=250000,
            # parity=serial.PARITY_NONE,
            # stopbits=serial.STOPBITS_ONE,
            # bytesize=serial.EIGHTBITS,
            timeout=1

        )
        self.serial.flush()
        time.sleep(.1)
        if side != "N":
            self.set_speed_regulation_pi(ki, kp)

    def set_speed_regulation_pi(self, ki, kp):
        # i = -10
        # while i < 0:
        msg = "I" + str(ki) + "i" + "P" + str(kp) + "p"
        time.sleep(.01)
        print("sent : ", msg)
        self.serial.write(bytes(msg, 'utf-8'))
        time.sleep(0.01)
        self.serial.write(bytes(msg, 'utf-8'))
        time.sleep(0.01)
        self.serial.write(bytes(msg, 'utf-8'))
        time.sleep(0.01)
        self.serial.write(bytes(msg, 'utf-8'))
        time.sleep(0.01)
        self.serial.write(bytes(msg, 'utf-8'))
        time.sleep(0.01)
        time.sleep(.01)
        # i += 1

        print("Recived PI : ", self.get_read())



    def send_speed(self, msg):
        if msg >= 0:
            msg = str(abs(msg))
            msg = "S" + self.side + '0' * (5 - len(msg)) + msg + "E"
        else:
            msg = str(abs(msg))
            msg = "S" + self.side + "-" + '0' * (5 - len(msg)) + msg + "E"
        # print(f"sent : {msg}")
        self.serial.write(bytes(msg, 'utf-8'))

    def send_speed_left(self, msg: int):
        # return

        if msg >= 0:
            msg = str(abs(msg))
            msg = "S" + "L" + '+' + '0' * (5 - len(msg)) + msg + "E"
        else:
            msg = str(abs(msg))
            msg = "S" + "L" + "-" + '0' * (5 - len(msg)) + msg + "E"
        # print(f"sent : {msg}")
        self.serial.write(bytes(msg, 'utf-8'))

    def send_speed_right(self, msg: int):
        # return

        if msg >= 0:
            msg = str(abs(msg))
            msg = "S" + "R" + '+' + '0' * (5 - len(msg)) + msg + "E"
        else:
            msg = str(abs(msg))
            msg = "S" + "R" + "-" + '0' * (5 - len(msg)) + msg + "E"

        # print(f"sent : {msg}")
        self.serial.write(bytes(msg, 'utf-8'))

    def get_read(self):

        try:

            # while self.serial.inWaiting() == 0:
            #     time.sleep(.1)
            if self.serial.inWaiting() > 0:

                msg = self.serial.read_all().decode('utf-8').rstrip()
                # msg = msg.decode()

                # self.serial.flushInput()
                my_str = f"{msg}"

                return my_str[-200:-1]
            #return "empty"
        except:
            return "error"

    def get_encoders_left_right(self,delay = 0):
        try:
            if self.serial.inWaiting() > 0:
                time.sleep(.0009)
                msg = self.serial.read_all().decode('utf-8').rstrip()
                my_str = f"{msg}"
                index_t = my_str.rfind("T")
                index_s = my_str[:index_t].rfind("S")
                index_e = my_str[:index_t].rfind("E")

                if DriverCommunication.debug or data.ENKODERI:
                    DriverCommunication.debug = False
                    print("...........\nYou sent me : \n" + my_str + "\n............\n")




                if index_t > -1 and index_s >-1 and index_e > -1:
                    enc_right, enc_left = -int(my_str[index_s + 1:index_e]), -int(my_str[index_e + 1:index_t])                    

                    self.enc_left = -enc_left
                    self.enc_right = -enc_right

                return self.enc_left,self.enc_right
            # print("empty")
            return self.enc_left,self.enc_right
        except Exception as e:
            print("ERROR recive : ")
            print(e)
            return self.enc_left,self.enc_right


    #todo bolja seriska kasnije
    def get_encoders_left_right2(self,delay = 0.002):
        # try:
        #     if self.serial.inWaiting():
        #         time.sleep(delay)
        #
        #         while self.serial.inWaiting():
        #             ch = self.serial.read().decode('utf-8').rstrip()
        #
        #             if ch == "S":
        #                 enc = True
        #             msg += ch
        #
        #             if ch == "T":
        #                 enc = False
        #
        #             if not enc:
        #                 break
        #
        #
        #         my_str = f"{msg}"
        #         index_t = my_str.rfind("T")
        #         index_s = my_str[:index_t].rfind("S")
        #         index_e = my_str[:index_t].rfind("E")
        #
        #         tmp = self.serial.read().decode('utf-8').rstrip()
        #         if DriverCommunication.debug:
        #             DriverCommunication.debug = False
        #             print("\nyou sent me : \n" + tmp + "\n............\n")
        #
        #
        #         if index_t > -1 and index_s >-1 and index_e > -1:
        #             enc_left = -int(my_str[index_s + 1:index_e])
        #             enc_right = -int(my_str[index_e + 1:index_t])
        #
        #             self.enc_left = enc_left
        #             self.enc_right = enc_right
        #
        #         return self.enc_left,self.enc_right
        #     #print("empty")
        #     return self.enc_left,self.enc_right
        # except:
        #     print("ERROR")
            return self.enc_left,self.enc_right


if __name__ == "__main__":
    l = DriverCommunication(.01,.01,side = "L")
    # r = DriverCommunication("R")

    while 1:
        # l.read()
        # r.read()
        #
        # d = input("left send ")
        # l.send_speed_left(0)
        # l.send_speed_right(0)
        # l.send_speed(200)
        # time.sleep(0.1)
        #
        # l.read()

        # r.read()
        #
        # d = input("right send ")

        # r.send_speed(200)
        #
        print(l.get_encoders_left_right())
        time.sleep(.1)
        # r.read()
