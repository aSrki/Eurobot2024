import threading
from time import sleep
import time
import data
# from communication.driver_communication import DriverCommunication
# from regulation_controller.position import Position
from communication.can_comm import *
from communication.maxon_epos_driver import MaxonMotor


class PositionRegulation:
    count = 0
    max_count = 100000 #1000

    # Stanja pida
    sending_trans = False
    sending_rot = False
    sending_stop = False
    # ------------------------

    W_d = 0
    W_F = 0
    W_d_s = 0
    W_F_s = 0
    n = 0
    p = 0
    D = 0
    integral_K = 0
    integral_R = 0

    # moje za razvoj
    w_d_r = 0
    old_speed = 0
    old_rot_speed = 0
    speed = 0
    rot_speed = 0

    TiRConst = 2
    dif_K = 0
    dif_R = 0
    en_K = 0
    en_R = 0
    es_K = 0
    es_R = 0

    min_pid = 0
    max_pid = 3000

    cur_encoder_left = 0
    cur_encoder_right = 0

    speed_left = 0
    speed_right = 0

    RAMP_INCREMENT_START = 100  # ikrimentira se za time: delay #14
    RAMP_INCREMENT_STOP = 200000  # ikrimentira se za time: delay  #12

    ROT_RAMP_UP_INCREMENT = 100  # 12
    ROT_RAMP_DOWN_INCREMENT = 100  # 12

    

    delay = 0.01 #0.03 # speed regulation ~30ms

    def __init__(self):
        self.W_F = data.f_current

        self.MVL = 0
        self.MVR = 0

        # self.maxon = DriverCommunication(
        #     ki=1, kp=2, side='L')

        self.maxon_left = MaxonMotor(
            1, 50000, 50000)
        self.maxon_right = MaxonMotor(
            2, 50000, 50000)

        self.stop_position = False

        print("position")
        # I2i P1p
        self.can_communication = CAN_COMM()
        speed_thread1 = threading.Thread(target=self.send_vel_left)
        speed_thread1.start()
        speed_thread2 = threading.Thread(target=self.send_vel_right)
        speed_thread2.start()

        position_thread = threading.Thread(target=self.get_position)
        position_thread.start()

        

    def start(self):

        self.can_communication.start()
        self.can_communication.pos.start()

        self.is_running = True

        thread = threading.Thread(target=self.running_calculation)
        thread.start()

    def running_calculation(self):
        while data.running.is_set():
            self.calculate_position()
            sleep(self.delay)
            print(f"Vreme3: {time.time()}")

        return
    
    def get_position(self):
        while data.running.is_set():
            self.can_communication.pos.calculate_position()
            sleep(self.can_communication.pos.delay)

    def calculate_position(self):

        debug = True
        if self.count > self.max_count:
            self.count = 0
            debug = False
            # DriverCommunication.debug = False
        self.count += 1

        # Suma inkrimenta na levom i desnom enkoderu se ucitavaju
        # self.position.calculate_position()

        # self.can_communication.pos.calculate_position()

        sum_left = data.sum_encoder_left
        sum_right = data.sum_encoder_right

        # Trenutna inkrementacija
        curr_encoder_right = self.cur_encoder_right
        curr_encoder_left = self.cur_encoder_left

        encoder_left = sum_left - curr_encoder_left
        encoder_right = sum_right - curr_encoder_right

        self.cur_encoder_right = sum_right
        self.cur_encoder_left = sum_left

        # predjeni put u instanci vremena(trenutni)
        d = ((encoder_left + encoder_right) / 2) * data.OdometryData.inc_mm
        f = data.f_current

        if True:
            print(f"INC1: {data.enc_left} INC2: {data.enc_right}")
            print('\n\n\nLevi enkoder:\t{}'.format(data.sum_encoder_left))
            print('Desni enkoder:\t{}'.format(data.sum_encoder_right))
            # print('Levi trenutna vrednost enkoder:\t{}'.format(encoder_left))
            # print('Desni trenutna vrednost enkoder:\t{}'.format(encoder_right))
            print('X-osa:\t\t\t{:.3f} mm'.format(data.x_current))
            print('Y-osa:\t\t\t{:.3f} mm'.format(data.y_current))
            print('UGAO osa:\t\t{:.3f}'.format(f), ' \n\n\n')

            print("enK: {0}, enR: {1}".format(self.en_K, self.en_R))
            # # print('d duzina:\t\t\t{:.0f}'.format(d))

        if self.stop_position:
            # while data.last_MVL > 2000 or data.last_MVR > 2000:
            #     data.last_MVL = int(0.3 * data.last_MVL)
            #     data.last_MVR = int(0.3 * data.last_MVR)
            #     # self.maxon.send_speed_left(data.last_MVL)
            #     # self.maxon.send_speed_right(data.last_MVR)
            #     self.maxon_left.rotate_with_rpm(data.last_MVL)
            #     self.maxon_right.rotate_with_rpm(data.last_MVR)
            #     sleep(.01)

            # self.maxon.send_speed_left(0)
            # self.maxon.send_speed_right(0)
            self.maxon_left.rotate_with_rpm(0)
            self.maxon_right.rotate_with_rpm(0)
        else:
            self.regulation(d, f, debug)

    def translation_ramp(self, w_d, d) -> int:
        if w_d + self.RAMP_INCREMENT_START > self.w_d_r:
            self.w_d_r += self.RAMP_INCREMENT_START
            return self.w_d_r
        elif w_d - self.RAMP_INCREMENT_STOP < self.w_d_r:
            self.w_d_r -= self.RAMP_INCREMENT_STOP
            return self.w_d_r

        return w_d

    def get_new_angle(self):
        angle = abs(self.W_F - self.W_F_s)
        if angle > 180:
            angle -= 180
        return angle

    def stop(self):
        self.stop_position = True

    def reset_position(self):
        self.stop_position = False

    def regulation(self, d, f, debug):
        # ------------------------------------------------------------------------------------------
        # REGULACIJA, FUCK YEAH
        # --------------------------------------------------------------------------------------------

        # ZELJENI PUT I UGAO
        W_F = self.W_F
        W_d = self.W_d  # self.translation_ramp(self.W_d,d)

        # if debug:
        #     print("w_d_r : ****************************  -> ",W_d)

        # PREDJENI PUT
        self.D += d
        D = self.D

        # GRESKA U TRANSLACIJI
        self.en_K = W_d - D
        enK = self.en_K

        self.en_R = W_F - f  # GRESKA U UGLU // U ODNOSU NA APSULUTNI UGAO
        if debug:
            print(f"Self enr: {W_F} - {f} = {self.en_R}")
        if self.en_R > 180:  # UGAO GLEDA BLIZI
            self.en_R = -360 + self.en_R
        elif self.en_R < -180:
            self.en_R = 360 + self.en_R

        ###############################ROTATION###########################
        if self.sending_rot and not self.sending_stop:
            if debug:
                print("ROTATION")
            pojacanje = data.rotate_pojacanje
            rotpoj = 1
            if abs(self.en_R) < self.get_new_angle() * .1:
                # print("naniiii")
                pojacanje *= 1

            # if self.get_new_angle() < 3:
            #     # print("poj do 3")
            #     rotpoj *= 3  # 6.7

            # elif self.get_new_angle() < 10:
            #     # print("poj do 10")
            #     rotpoj *= 2.2

            # elif self.get_new_angle() < 25:
            #     # print("poj do 25")
            #     rotpoj *= 1.8

            # elif self.get_new_angle() < 45:
            #     # print("poj do 45")
            #     rotpoj *= 1.6

            # elif self.get_new_angle() < 90:
            #     # print("poj do 90")
            #     rotpoj *= 1.5

            # elif self.get_new_angle() < 140:
            #     # print("poj do 140")
            #     rotpoj *= 1.4
            # else:
            #     # print("poj do 180")
            #     rotpoj *= 1.2

            KpK = 6 * pojacanje  # 6 #4 #Srdjan_bilo je 5
            KpR = 20 * pojacanje * rotpoj

            TiR = 15000  # 450 # self.TiRConst#1#~60,150
            TiK = 400000000  # ~2000

            TdK = 0  # bilo je 2
            TdR = -3.5  # 2




        #============TRANSlACIJAAAA======================================================================================
        elif self.sending_trans and not self.sending_stop:
            pojacanje = data.translate_pojacanje
            rotpoj = data.translate_rot_pojacanje

            # if abs(W_d) > 1500:
            #     pojacanje *= 0.9
            #     rotpoj *= 1
            #     self.max_pid = 10000
            # elif abs(W_d) > 1000:
            #     pojacanje *= 1
            #     rotpoj *= 1

            # elif abs(W_d) > 600:
            #     pojacanje *= 1.1
            #     rotpoj *= 1

            # elif abs(W_d) > 400:
            #     pojacanje *= 1.8  # 1.7
            #     rotpoj *= 1

            if abs(W_d) <= 300:
                pojacanje *= 0.75  # 1.15
                # rotpoj *= 0.5  # 0.85

            # else:
            #     pojacanje *= 2  # 1.3
            #     rotpoj *= 0.6  # 1

            # if (abs(W_d) * 0.05 > abs(enK) and W_d != 0):
            #     pojacanje *= 1.3
            #     rotpoj *= .4
            # elif (abs(W_d) * 0.2 > abs(enK) and W_d != 0):
            #     pojacanje *= 1.3
            #     rotpoj *= .8

            # elif (abs(W_d) * 0.35 > abs(enK) and W_d != 0):
            #     pojacanje *= 1
            #     rotpoj *= .85

            # elif (abs(W_d) * 0.9 < abs(enK) and W_d != 0):
            #     pojacanje *= .75
            # elif (abs(W_d) * 0.8 < abs(enK) and W_d != 0):
            #     pojacanje *= .9

            #============TRANSlACIJAAAA======================================================================================
            if debug:
                print("TRANSLATE")

            # if d < 250:
            #     rotpoj = 0.2

            KpK = 12 * pojacanje  #7.2 !!!! 6 - 16 u zavisnosti stabilnosti i brzine koju hcete
            KpR = 30 * pojacanje * rotpoj  # 75 bilo

            TiR = 660000000  #6600 # 200
            TiK = 10000 #5200

            TdK = 3 # 1
            TdR = -5  # 3

        else:
            if debug:
                print("STOP")

            pojacanje = 1

            KpK = 2   # (0.85 * pojacanje  )/1.2#1
            KpR = 2   # (2 * pojacanje * 10)/2#40 ... 90

            TiR = 1000000  # self.TiRConst#1#~60,150
            TiK = 1000000  # ~2000

            TdK = 0  # 3
            TdR = 0  # 3

        # PID TRANSLACIJA________________________
        esK = self.es_K  # sTARA GRESKA
        # FILTRIRANA STARA I NOVA GRESKA ZA INTEGRALNO,I STARU GRESKU
        efK = 0.1 * enK + 0.9 * esK
        self.integral_K = self.integral_K + enK  # *  # INTEGRALIMO
        difK = efK - esK  # DIFERENCIJAL FILTRIRANOG I STAROG T6J NOVOG I STAROG
        integralK = self.integral_K
        self.es_K = efK  # STARA GRESKA JE FILTRIRANA
        # ----------------------------------------------------------------------

        # PID ROTACIJA_________________________
        enR = self.en_R  # NOVA GRESKA U UGLU
        esR = self.es_R  # STARA GRESKA U UGLU
        # FILTRIRANA STARA I NOVA GRESKA ZA INTEGRALNO,I STARU GRESKU
        efR = 0.1 * enR + 0.9 * esR
        self.integral_R = self.integral_R + enR  # *  # INTEGRALIMO
        difR = efR - esR  # DIFERENCIJAL FILTRIRANOG I STAROG T6J NOVOG I STAROG
        integralR = self.integral_R
        self.es_R = efR  # STARA GRESKA JE FILTRIRANA

        # ----------------------------------------------------------------------------

        # PID RACUNICA
        Kp = KpK * enK  # efK
        Ki = KpK * (1 / TiK) * integralK
        Kd = KpK * TdK * difK
        pid_K = Kp + Ki + Kd

        Rp = KpR * enR
        Ri = KpR * (1 / TiR) * integralR
        Rd = KpR * TdR * difR
        pid_R = Rp + Ri + Rd
        # ----------------------------------------

        if debug:
            print('KpK *******************  === ', KpK)
            print('w d  = ', W_d, '    D = ', self.D, '        w f = ', W_F)
            print('\ncist enr  == ', enR)
            print('cist enk  == ', enK)
            print('\ncist pid k  == ', pid_K)
            print('cist pid r  == ', pid_R)

            print("\nKp", Kp)
            print("Ki", Ki)
            print("Kd", Kd)

            print("\nRp", Rp)
            print("Ri", Ri)
            print("Rd", Rd)

            print('======================pid_R ===========================', pid_R)
            print('======================pid_K===========================', pid_K)

        # # MIN PID_R
        # if -10 > pid_K > -self.min_pid_K:
        #     pid_K = -self.min_pid_K
        # elif 10 < pid_K < self.min_pid_K:
        #     pid_K = self.min_pid_K
        # # -----------------------------------

        # RAMP FOR TRANSLATION
        dif_speed = pid_K - self.old_speed
        if self.sending_trans:
            if W_d >= 0:
                if dif_speed < -self.RAMP_INCREMENT_STOP:
                    if debug:
                        print("RAMP DOWN TRANSLATION")
                    self.speed -= self.RAMP_INCREMENT_STOP
                elif dif_speed > self.RAMP_INCREMENT_START:
                    if debug:
                        print("RAMP UP TRANSLATION")
                    self.speed += self.RAMP_INCREMENT_START
                else:
                    self.speed = pid_K
            else:
                if dif_speed < -self.RAMP_INCREMENT_START:
                    self.speed -= self.RAMP_INCREMENT_START
                    if debug:
                        print("RAMP UP TRANSLATION")
                elif dif_speed > self.RAMP_INCREMENT_STOP:
                    self.speed += self.RAMP_INCREMENT_STOP
                    if debug:
                        print("RAMP DOWN TRANSLATION")
                else:
                    self.speed = pid_K
        else:
            self.speed = pid_K
        self.old_speed = self.speed

        # RAMP FOR ROTATION NOT DONE YET
        if self.sending_rot:
            dif_rot_speed = pid_R - self.old_rot_speed

            if self.en_R > 0:
                if dif_rot_speed < -self.ROT_RAMP_DOWN_INCREMENT:
                    # print("RAMP DOWN ROTATION")
                    self.rot_speed -= self.ROT_RAMP_DOWN_INCREMENT
                elif dif_rot_speed > self.ROT_RAMP_UP_INCREMENT:
                    # print("RAMP UP ROTATION")
                    self.rot_speed += self.ROT_RAMP_UP_INCREMENT
                else:
                    self.rot_speed = pid_R
            else:
                if dif_rot_speed < -self.ROT_RAMP_UP_INCREMENT:
                    self.rot_speed -= self.ROT_RAMP_UP_INCREMENT
                    # print("RAMP UP ROTATION")
                elif dif_rot_speed > self.ROT_RAMP_DOWN_INCREMENT:
                    self.rot_speed += self.ROT_RAMP_DOWN_INCREMENT
                    # print("RAMP DOWN ROTATION")
                else:
                    self.rot_speed = pid_R
        else:
            self.rot_speed = pid_R
        self.old_rot_speed = self.rot_speed

        if debug:
            print("speed : ****************************  -> ", self.speed)
        # -----------------------------------------

        if abs(self.rot_speed) > abs(self.speed) / 5 and self.rot_speed and self.sending_trans:
            self.rot_speed = abs(self.speed) / 5 * \
                (self.rot_speed / abs(self.rot_speed))
            if debug:
                print("ANTI WINDUP ZA ODNOS SPEED I self.rot_speed  ->",
                      self.rot_speed)

        elif abs(self.rot_speed) / 6 < abs(self.speed) and self.speed and self.sending_rot:
            self.speed = abs(self.rot_speed) / 6 * \
                (self.speed / abs(self.speed))
            if debug:
                print("ANTI WINDUP ZA ODNOS self.rot_speed I speed  ->",
                      self.rot_speed)

        # ANTI WINDUP
        if self.speed > self.max_pid:
            self.speed = self.max_pid
        elif self.speed < -self.max_pid:
            self.speed = -self.max_pid

        # if MVR > self.max_pid:
        #     MVR = self.max_pid
        # elif MVR < -self.max_pid:
        #     MVR = -self.max_pid

        MVL = int(self.speed - self.rot_speed)
        MVR = int(self.speed + self.rot_speed)

        self.MVL = MVL
        self.MVR = MVR

        # # ANTI WINDUP down
        # if 0 > MVL > -self.min_pid:
        #     MVL = -self.min_pid
        # elif 0 < MVL < self.min_pid:
        #     MVL = self.min_pid
        #
        # if 0 > MVR > -self.min_pid:
        #     MVR = -self.min_pid
        # elif 0 < MVR < self.min_pid:
        #     MVR = self.min_pid

        # SKALER
        # MVL += self.min_pid * (abs(MVL) / (MVL + .0000000000001))
        # MVR += self.min_pid * (abs(MVR) / (MVR + .0000000000001))

        # MVL = input("MVL  : ")
        #
        # MVR = input("MVR  : ")

        if (enK >= -3) and (enK <= 3) and (-.5 <= enR <= .5):
            data.budz = True
            # self.maxon.send_speed_left(0)
            # self.maxon.send_speed_right(0)

            self.maxon_left.rotate_with_rpm(0)
            self.maxon_right.rotate_with_rpm(0)

            self.integral_K = 0
            self.integral_R = 0
            # self.W_d = D
            # self.W_F = f
            # self.W_F_s = W_F
            # self.W_d_s = W_d
            self.sending_stop = True

            if debug:
                print('======================STOP===========================', MVL)
                print('======================STOP===========================', MVR)
                print("\n")

        else:
            if debug:
                print('======================MVL===========================', MVL)
                print('======================MVR===========================', MVR)
                print("\n")

            # MVL = 2000
            # MVR = 2000

            # self.maxon.send_speed_left(MVL)  # CHANAL 1 MVL
            # self.maxon.send_speed_right(MVR)  # CHANAL2 MVR
                
            # self.maxon_right.rotate_with_rpm(-MVR)
            # print(f"Vreme2: {time.time()}")
            # self.maxon_left.rotate_with_rpm(MVL)
            # print(f"Vreme1: {time.time()}")

            data.last_MVL = MVL
            data.last_MVR = MVR

            self.sending_stop = False

        # if debug:
        #     print(self.motor.get_read())
            
          
    def send_vel_left(self):
        while data.running.is_set():
            self.maxon_left.rotate_with_rpm(self.MVL)
            # print(f"Vreme1: {time.time()}")
            time.sleep(self.delay)
    def send_vel_right(self):
        while data.running.is_set():
            self.maxon_right.rotate_with_rpm(-self.MVR)
            # print(f"Vreme2: {time.time()}")
            time.sleep(self.delay)
    


# position = Position()
# position.start()
