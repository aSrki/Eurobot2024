from enc import *
# ID_1 MOTOR RIGHT
# ID_4 MOTOR LEFT
class odom:
    curr_x = 0
    curr_y = 0
    curr_theta = 0
    curr_angle = 0
    enc_r = 0
    enc_r_default = 0
    enc_l = 0
    enc_l_default = 0
    speed_r = 0
    speed_l = 0
    d_r = 86
    d_l = 86
    b = 119
    def __init__(self, curr_x, curr_y, curr_theta, curr_angle, d_r = 86, d_l = 86, b = 119):
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.curr_theta = curr_theta
        self.curr_angle = curr_angle
        self.d_r = d_r
        self.d_l = d_l
        self.b = b
        self.enc_r_default, self.enc_l_default = read_positions((1,4))

    def delta_inc()
        self.enc_r, self.enc_l = read_positions((1,4))
        self.deltaR = self.enc_r - self.enc_r_default
        self.deltaL = self.enc_l - self.enc_l_default
        self.enc_r_default = self.enc_r
        self.enc_l_default = self.enc_l

    



        

