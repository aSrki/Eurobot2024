from enc import *
import threading
import time
# ID_1 MOTOR RIGHT
# ID_4 MOTOR LEFT
class Odom:
    curr_x = 0
    curr_y = 0
    curr_theta = 0      #
    curr_angle = 0      #
    enc_r = 0           # new enc_r
    enc_r_old = 0       # old enc_r -> enc_r[t-1]
    enc_l = 0           # new enc_l
    enc_l_old = 0       # old enc_l -> enc_l[t-1]
    speed_r = 0
    speed_l = 0
    d_r = 86            # diameter
    d_l = 86            # diameter
    b = 119             # distance between the wheels

    thread = None
    
    PI = 3.141592653589793238462643383279502884197
    ENC_MAX_INC = 4096
    INC_2_RAD = (2*PI/ENC_MAX_INC)

    def __init__(self, curr_x, curr_y, curr_theta, curr_angle, d_r = 86, d_l = 86, b = 119):
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.curr_theta = curr_theta
        self.curr_angle = curr_angle
        self.d_r = d_r
        self.d_l = d_l
        self.b = b
        self.enc_r_old, self.enc_l_old = read_positions((1,4))      # enc -> t = 0
        print(self.enc_r_old, self.enc_l_old)

    def odom_update(self):
        while True:
            try:
                self.enc_r, self.enc_l = read_positions((1,4))              # enc -> t = t + 1
            except TypeError:
                print("Cannot unpack non-iterable NoneType object")

            # discard read = 0
            if self.enc_r == 0:
                self.enc_r = self.enc_r_old
            if self.enc_l == 0:
                self.enc_l = self.enc_l_old
                

            self.deltaR = self.enc_r - self.enc_r_old
            self.deltaL = self.enc_l - self.enc_l_old

            # print(f"DELTA R = {self.deltaR}, ENC_R = {self.enc_r}, ENC_R_OLD = {self.enc_r_old}")
            # print(f"DELTA L = {self.deltaL}, ENC_L = {self.enc_l}, ENC_L_OLD = {self.enc_l_old}")

            # overFlow/underFlow
            # 0 - 65535 => 0 - (2^16)-1
            if self.deltaR < -40000:
                self.deltaR = (65535 - self.enc_r_old) + self.enc_r     # counting up
            elif self.deltaR > 40000:
                self.deltaR = (-65535 - self.enc_r_old) + self.enc_r     # counting down            

            if self.deltaL < -40000:
                self.deltaL = (65535 - self.enc_l_old) + self.enc_l     # counting up
            elif self.deltaL > 40000:
                self.deltaL = (-65535 - self.enc_l_old) + self.enc_l     # counting down    

            print(f"DELTA R = {self.deltaR}, ENC_R = {self.enc_r}, ENC_R_OLD = {self.enc_r_old}")
            print(f"DELTA L = {self.deltaL}, ENC_L = {self.enc_l}, ENC_L_OLD = {self.enc_l_old}")


            self.enc_r_old = self.enc_r     # update
            self.enc_l_old = self.enc_l     # update

            # return self.deltaR, self.deltaL

            time.sleep(0.01)

    def run_odom(self):
        self.thread = threading.Thread(target=self.odom_update)
        self.thread.start()

    def stop_odom(self):
        self.thread.join()  # TODO: add stop
        print("STOPPED")
        sys.exit()






    



        

