from enc import *
import threading
import time
from math import *
from XL430 import *
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
    d_r = 93.45           # diameter 91.7           93.45
    d_l = 93.5           # diameter 93.9            93.9              radi  93.5
    b = 115.9            # distance between the wheels 124.7    measure 117.7     115
    v = 0
    w = 0

    thread = None
    
    ENC_MAX_INC = 4096
    INC_2_RAD = (2*pi/ENC_MAX_INC)

    time_old = 0
    time_curr = 0
    delta_time = 0

    flag = 0 # forward
    going = False

    def __init__(self, curr_x, curr_y, curr_theta, curr_angle):
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.curr_theta = curr_theta
        self.curr_angle = curr_angle
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

            # print(f"DELTA R = {self.deltaR}, ENC_R = {self.enc_r}, ENC_R_OLD = {self.enc_r_old}")
            # print(f"DELTA L = {self.deltaL}, ENC_L = {self.enc_l}, ENC_L_OLD = {self.enc_l_old}")


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
            if self.flag == 0:
                # FORWARD
                self.curr_x -= self.v * cos(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
                self.curr_y -= self.v * sin(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
                self.curr_theta -= self.w * self.delta_time    
                # print(f"X -> COS -> f{cos(self.curr_theta + self.w * self.delta_time / 2.0)}")
                # print(f"X -> SIN -> f{sin(self.curr_theta + self.w * self.delta_time / 2.0)}")
            else:
                # BACKWARD
                self.curr_x -= self.v * cos(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
                self.curr_y -= self.v * sin(self.curr_theta + self.w * self.delta_time / 2.0) * self.delta_time
                self.curr_theta -= self.w * self.delta_time                

            if self.curr_theta < -pi:
                self.curr_angle = 2*pi + self.curr_theta
            elif self.curr_theta > pi:
                self.curr_angle = self.curr_theta - 2*pi
            else:
                self.curr_angle = self.curr_theta

            # print(f"LINEAR SPEED: {self.v}")
            # print(f"ANGULAR SPEED: {self.w}")
            # print(f"CURRENT X: {self.curr_x}")
            # print(f"CURRENT Y: {self.curr_y}") 
            print(f"CURRENT THETA: {self.curr_theta}")
            print(f"CURRENT ANGLE: {self.curr_angle}") 


            time.sleep(0.001)

    def run_odom(self):
        self.thread = threading.Thread(target=self.odom_update)
        self.thread.start()

    def stop_odom(self):
        send_velocity_multiple([1, 4], [0, 0])
        self.thread.join()  # TODO: add stop
        print("STOPPED")
        sys.exit()


    def go_to_XY(self, goal_x, goal_y):
        print("_________________GO TO XY_________________")
        angle = atan2(goal_y - self.curr_y, goal_x - self.curr_x)
        goal_angle = angle
        print(f"Goal angle {goal_angle}, angle {angle}")
        angle -= self.curr_angle

        if goal_angle < -pi:
            goal_angle = 2*pi + goal_angle
        elif goal_angle > pi:
            goal_angle = goal_angle - 2*pi

        if angle < -pi:
            angle = 2*pi + angle
        elif angle > pi:
            angle = angle - 2*pi

        # BUDZ
        # if goal_angle < 1.745329252:
        #     goal_angle = goal_angle * 0.775     # 0.775
        # elif goal_angle < pi:
        #     goal_angle = goal_angle * 0.888     # 0.8778

        print(f"Angle after math: {angle}")
        print(f"Goal angle after math: {goal_angle}")        
        print(f"Current angle: {self.curr_angle}")
        print(f"Current theta: {self.curr_theta}")
       
        if (abs(goal_angle - self.curr_angle) > pi - 0.1 and abs(goal_angle - self.curr_angle) < pi + 0.1):
            # DISTANCE
            self.flag = 1   # backward
            while abs(sqrt((goal_y - self.curr_y)**2 + (goal_x - self.curr_x)**2)) > 50:
                print(f"CURRENT X: {self.curr_x}")
                print(f"CURRENT Y: {self.curr_y}")
                if self.going == False:
                    send_velocity_multiple([1, 4], [100, -100])    # backward
                    print(f"FLAG {self.flag}")
                    self.going = True
                time.sleep(0.0001)
            send_velocity_multiple([1, 4], [0, 0])
            self.going = False
        else:
            # ANGLE
            self.flag = 0   # forward
            if angle > 0:
                while abs((goal_angle - self.curr_angle)) > 0.05:
                    print(f"Current angle {self.curr_angle}, goal angle {goal_angle}")
                    if self.going == False:
                        send_velocity_multiple([1, 4], [-41.5, -40.5]) # rotation +      -71.5, -70.5
                        self.going = True
                    time.sleep(0.0001)
                print(f"Izasao iz WHILE.... USLOV  angle > 0: {abs((goal_angle - self.curr_angle))}")
                send_velocity_multiple([1, 4], [0, 0])
                self.going = False
            else:
                while abs((goal_angle - self.curr_angle)) > 0.05:
                    print(f"Current angle {self.curr_angle}, goal angle {goal_angle}")
                    if self.going == False:
                        send_velocity_multiple([1, 4], [20.5, 21.5]) # rotation -
                        self.going = True
                    time.sleep(0.0001)
                print(f"Izasao iz WHILE.... USLOV angle < 0: {abs((goal_angle - self.curr_angle))}")
                send_velocity_multiple([1, 4], [0, 0])
                self.going = False

            # DISTANCE
            while abs(sqrt((goal_y - self.curr_y)**2 + (goal_x - self.curr_x)**2)) > 50:
                print(f"CURRENT X: {self.curr_x}, CURRENT Y: {self.curr_y}")               
                if self.going == False:
                    send_velocity_multiple([1, 4], [-97.5, 98.5])    # forward -97.5, 98.5
                    print(f"FLAG {self.flag}")
                    self.going = True

                time.sleep(0.0001)
            send_velocity_multiple([1, 4], [0, 0])
            self.going = False
            
        print(f"GO TO XY        Self current_x{self.curr_x}")
        print(f"GO TO XY        Self current_y{self.curr_y}")     




    



        

