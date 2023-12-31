from XL430 import *
import time
from math import *
import threading
import sys


class Sima:
    curr_x = 0
    curr_y = 0
    curr_theta = 0
    curr_angle = 0
    d_r = 0
    d_l = 0
    b = 0
    speed_l = 0
    speed_r = 0
    going = False
    thread = None
    flag = 1

    def __init__(self, curr_x, curr_y, curr_theta, curr_angle, d_r, d_l, b):
        '''self, curr_x, curr_y, curr_theta, curr_angle, d_r, d_l, b'''
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.curr_theta = curr_theta
        self.curr_angle = curr_angle
        self.d_r = d_r
        self.d_l = d_l
        self.b = b

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

        print(f"Angle after math: {angle}")
        print(f"Goal angle after math: {goal_angle}")        
        print(f"Current angle: {self.curr_angle}")
        print(f"Current theta: {self.curr_theta}")        

        if (abs(goal_angle - self.curr_angle) > pi - 0.1 and abs(goal_angle - self.curr_angle) < pi + 0.1):
            # DISTANCE
            self.flag = 0
            while abs(sqrt((goal_y - self.curr_y)**2 + (goal_x - self.curr_x)**2)) > 15:
                self.speed_l = 100
                self.speed_r = 100
                if self.going == False:
                    send_velocity_multiple([4, 1], [-100, 98.5])
                    self.going = True
                time.sleep(0.001)
            self.speed_l = 0
            self.speed_r = 0
            send_velocity_multiple([4, 1], [0, 0])
            self.going = False
        else:
            # ANGLE
            self.flag = 1
            if angle > 0:
                while abs((goal_angle - self.curr_angle)) > 0.01:
                    print(f"Current angle {self.curr_angle}")
                    self.speed_l = -100
                    self.speed_r = 100
                    if self.going == False:
                        send_velocity_multiple([4, 1], [-98.5, -100])
                        self.going = True
                    time.sleep(0.0005)
                self.speed_l = 0
                self.speed_r = 0
                send_velocity_multiple([4, 1], [0, 0])
                self.going = False
            else:
                while abs((goal_angle - self.curr_angle)) > 0.01:
                    print(f"Current angle: {self.curr_angle}")
                    self.speed_l = 100
                    self.speed_r = -100
                    if self.going == False:
                        send_velocity_multiple([4, 1], [98.5, 100])
                        self.going = True
                    time.sleep(0.0005)
                self.speed_l = 0
                self.speed_r = 0
                send_velocity_multiple([4, 1], [0, 0])
                self.going = False

            # DISTANCE
            while abs(sqrt((goal_y - self.curr_y)**2 + (goal_x - self.curr_x)**2)) > 15:
                self.speed_l = 100
                self.speed_r = 100
                if self.going == False:
                    send_velocity_multiple([4, 1], [100, -98.5])
                    self.going = True
                time.sleep(0.001)
            self.speed_l = 0
            self.speed_r = 0
            send_velocity_multiple([4, 1], [0, 0])
            self.going = False
            
        print(f"Self current_x{self.curr_x}")
        print(f"Self current_y{self.curr_y}")     



    def update_odometry(self):
        while True:
            # delta distance factor 1.32 , new factor for distance 900mm
            delta_dist = ((((self.speed_r/100) * 1.05 * pi * self.d_r) +
                          ((self.speed_l/100) * 1.05 * pi * self.d_l))/2.0)*0.0005
            delta_ang = ((((self.speed_r/100) * 1.2 * pi * self.d_r) -
                         ((self.speed_l/100) * 1.2 * pi * self.d_l))/self.b)*0.0005
            # print(f"Delta angle {delta_ang}")
            if self.flag == 1:
                self.curr_x += delta_dist * cos(self.curr_theta + 0.5*delta_ang)
                self.curr_y += delta_dist * sin(self.curr_theta + 0.5*delta_ang)
                self.curr_theta += delta_ang
            else:
                self.curr_x -= delta_dist * cos(self.curr_theta + 0.5*delta_ang)
                self.curr_y -= delta_dist * sin(self.curr_theta + 0.5*delta_ang)
                self.curr_theta -= delta_ang
            # self.curr_theta += delta_ang
            
            if self.curr_theta < -pi:
                self.curr_angle = 2*pi + self.curr_theta
            elif self.curr_theta > pi:
                self.curr_angle = self.curr_theta - 2*pi
            else:
                self.curr_angle = self.curr_theta
           
        
            time.sleep(0.0005)

    def run_odom(self):
        self.thread = threading.Thread(target=self.update_odometry)
        self.thread.start()

    def stop(self):
        self.speed_l = 0
        self.speed_r = 0
        send_velocity_multiple([4, 1], [0, 0])
        print("STOPPED")
        sys.exit()

# try:
#     sima = Sima(100, 100, 0, 86, 86, 119)
#     sima.run_odom()
#     sima.go_to_XY(1100, 100)

# except KeyboardInterrupt:
#     sima.stop()
