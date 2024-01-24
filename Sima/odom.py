from enc import *
import threading
import time
from math import *
# ID_1 MOTOR RIGHT
# ID_4 MOTOR LEFT
class Odom:
    curr_x = 0
    curr_y = 0
    curr_theta = 0      #
    curr_angle = 0      #
    enc_r = 0           # new enc_r
    enc_r_old = 0       # old enc_r -> enc_r[t-1]
    deltaR = 0
    enc_l = 0           # new enc_l
    enc_l_old = 0       # old enc_l -> enc_l[t-1]
    deltaL = 0
    v_r = 0
    w_r = 0
    v_l = 0
    w_l = 0
    d_r = 86.0           # diameter
    d_l = 86.0           # diameter
    b = 119.0            # distance between the wheels
    v = 0
    w = 0

    thread = None
    
    ENC_MAX_INC = 4096
    INC_2_RAD = (2*pi/ENC_MAX_INC)

    time_old = 0
    time_curr = 0
    delta_time = 0


    def __init__(self, curr_x, curr_y, curr_theta, curr_angle, d_r = 86.0, d_l = 86.0, b = 119.0):
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.curr_theta = curr_theta
        self.curr_angle = curr_angle
        self.d_r = d_r
        self.d_l = d_l
        self.b = b
        self.enc_r_old, self.enc_l_old = read_positions((1,4))      # enc -> t = 0
        print(self.enc_r_old, self.enc_l_old)
        self.time_old = time.time()

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

            # update time
            self.time_curr = time.time()
            self.delta_time = self.time_curr - self.time_old
            self.time_old = self.time_curr
            # print(f"DELTA TIME {self.deltatime}")

            # if self.delta_time != 0:
            self.w_r = self.deltaR * self.INC_2_RAD / self.delta_time
            self.w_l = self.deltaL * self.INC_2_RAD / self.delta_time

            self.v_r = self.w_r * (self.d_r / 2.0)
            self.v_l = self.w_l * (self.d_l / 2.0)
            
            # check the sign
            # forward v_r > 0 , v_l < 0          
            self.v = (self.v_r - self.v_l) / 2.0
            self.w = (self.v_r + self.v_l) / self.b

            # approximation average value
            # FORWARD
            self.curr_x -= self.v * cos(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
            self.curr_y -= self.v * sin(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
            self.curr_theta -= self.w * self.delta_time
            # TODO: BACKWARD ... FLAG etc..

            if self.curr_theta < -pi:
                self.curr_angle = 2*pi + self.curr_theta
            elif self.curr_theta > pi:
                self.curr_angle = self.curr_theta - 2*pi
            else:
                self.curr_angle = self.curr_theta

            print(f"LINEAR SPEED: {self.v}")
            print(f"ANGULAR SPEED: {self.w}")
            print(f"CURRENT X: {self.curr_x}")
            print(f"CURRENT Y: {self.curr_y}") 
            print(f"CURRENT THETA: {self.curr_theta}") 


            time.sleep(0.01)

    def run_odom(self):
        self.thread = threading.Thread(target=self.odom_update)
        self.thread.start()

    def stop_odom(self):
        self.thread.join()  # TODO: add stop
        print("STOPPED")
        sys.exit()






    



        

