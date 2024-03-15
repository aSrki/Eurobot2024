from regulation_controller.path import Path
from regulation_controller.position_regulation import PositionRegulation
# from skart.pozicija_distanca import PositionDistana
import data
import time
from data import Sensors
import math


class Moving:
    DEBUG_FOR_GO = False
    DEBUG_FOR_WHILE = False

    def __init__(self):
        self.position = PositionRegulation()
        self.position.maxon_left.rotate_with_rpm(0)
        self.position.maxon_right.rotate_with_rpm(0)
        self.distance_error = 0
        self.current_distance = 0

        pass

    def start(self):
        self.position.start()


# -------------------------------PARAMETRI ZA REGULACIJU KOD RAZLICITIH KRETANJA-------------------------------------


    def rotation_parameters(self):
        self.position.W_F_s = self.position.W_F
        # PARAMETRI:
        # za zeljenu duzinu
        self.position.W_d = 0
        self.position.D = 0

        # za pid parametre
        self.position.integral_K = 0
        self.position.integral_R = 0
        self.position.dif_K = 0
        self.position.dif_R = 0
        self.position.en_K = 0
        self.position.en_R = 0
        self.position.es_K = 0
        self.position.es_R = 0
        self.position.pidRstaro = 0
        self.position.pidKstaro = 0

        # za oznacavanje vrste pid regulacije,(semafor)potvrda slanja
        self.position.sending_rot = True
        self.position.sending = True  # msm da ne treba ali ajde
        self.position.sending_trans = False

        data.budz = False

# ----------------------------------------------------------------------------------------------------------------

    def translation_parameters(self):
        # PARAMETRI:
        # za zeljenu duzinu
        self.position.D = 0

        # za pid parametre
        self.position.integral_K = 0
        self.position.integral_R = 0
        self.position.dif_K = 0
        self.position.dif_R = 0
        self.position.en_K = 0
        self.position.en_R = 0
        self.position.es_K = 0
        self.position.es_R = 0
        self.position.TiRConst = 2
        self.position.pidRstaro = 0
        self.position.pidKstaro = 0

        # za oznacavanje vrste(stanje) pid regulacije,(semafor)potvrda slanja
        self.position.sending_rot = False
        self.position.sending_trans = True
        self.position.sending = True

        data.budz = False

# ----------------------------------------VRSTE KRETANJA----------------------------------------------------------

    def go_using_coordinates(self, __x, __y, direction_is_forward, offset):

        # ***************************************************************************************
        # ********************************** ROTATION ****************************************
        # **************************************************************************************
        sensors = data.sensors
        lidar = data.lidar

        data.sensors = Sensors.ALL_OFF
        data.lidar = Sensors.ALL_OFF
        # Pravi objekat path i ugao rotacije(za pozitivan pravac)
        path = Path(data.x_current, data.y_current, data.f_current)
        rotation = path.rotate(__x, __y)

        # Menja dobijeni ugao rotacije ako treba da ide unazad,negativan pravac
        if not direction_is_forward:
            if self.DEBUG_FOR_GO:
                print("menja ugao usled direkcije")
            if rotation >= 0:
                rotation -= 180
            else:
                rotation += 180

        if self.DEBUG_FOR_GO:
            print("ugao koji saljem je   =  ", rotation)

        # Salje rotaciju regulaciji i postavlja pocetne parametre regulaciji
        self.rotation_parameters()
        self.position.W_F = rotation

        # petlja koja pauzira dok se rotacija  ne zavrsi
        self.while_rotation(rotation)

        if self.DEBUG_FOR_GO:
            print("\n\nIZASAO  JE IZ ROTACIJE\n\n")

    # ***************************************************************************************
    # ********************************** TRANSLATION ****************************************
    # **************************************************************************************
        data.sensors = sensors
        data.lidar = lidar

        if __y < 0:
            x = __x - math.sin(math.radians(data.f_current))*offset
            y = __y + math.cos(math.radians(data.f_current))*offset
            if direction_is_forward:
                x = __x + math.sin(math.radians(data.f_current))*offset
                y = __y - math.cos(math.radians(data.f_current))*offset
        else:
            x = __x + math.sin(math.radians(data.f_current))*offset
            y = __y - math.cos(math.radians(data.f_current))*offset
            if not direction_is_forward:
                x = __x - math.sin(math.radians(data.f_current))*offset
                y = __y + math.cos(math.radians(data.f_current))*offset
        # Definisemo zeljenu distancu
        distance = path.distance(x, y)

        # Menja smer ako ide unazad negativnom smeru
        if not direction_is_forward:
            distance = -distance

        if self.DEBUG_FOR_GO:
            print('\nSALJE regulaciji distancu = ', distance, "\n")
            print(f'\n KOORDINATE:{x}, {y}\n')
            # data.log.add_info_message(f'OFFSET: {offset}')
            # data.log.add_info_message(f'\n KOORDINATE:{x}, {y}\n')

        # Salje regulaciji zeljenu distancu i postavlja regulacione parametre
        self.translation_parameters()
        self.position.W_d = distance

        # petlja koja pauzira dok se translacija ne zavrsi
        self.while_translate(distance, x, y, True)

        if self.DEBUG_FOR_GO:
            print("\n   IZLAZI IZ TRANSLACIJE    \n")

# ----------------------------------------------------------------------------------------------------------------

    def go_using_rotation(self, __f):
        if self.DEBUG_FOR_GO:
            print("ugao koji saljem je   =  ", __f)

        # Salje rotaciju regulaciji i postavlja pocetne parametre regulaciji
        self.rotation_parameters()
        self.position.W_F = __f

        # petlja koja pauzira dok se rotacija  ne zavrsi
        self.while_rotation(__f)

        print("\n\nIZASAO  JE IZ CISTE ROTACIJE\n\n")

# ----------------------------------------------------------------------------------------------------------------

    def go_using_distance_angle(self, distance, angle, direction_is_forward):
        # ***************************************************************************************
        # ********************************** ROTATION ****************************************
        # **************************************************************************************

        # zadaje zeljeni ugao rotacije(u kom uglu zelimo da robot bude) i filtriramo za opseg od 0 do 360
        rotation = angle+data.f_current
        if rotation < 0:
            rotation = abs(rotation) % 360
            rotation = -rotation
        else:
            rotation = rotation % 360

        # Menja dobijeni ugao rotacije ako treba da ide unazad,negativan pravac
        if not direction_is_forward:
            if self.DEBUG_FOR_GO:
                print("menja ugao usled direkcije")
            if rotation >= 0:
                rotation = rotation - 180
            else:
                rotation = rotation + 180

        if self.DEBUG_FOR_GO:
            print("ugao koji saljem je   =  ", rotation)

        # Salje rotaciju regulaciji i postavlja pocetne parametre regulaciji
        self.rotation_parameters()
        self.position.W_F = rotation

        # petlja koja pauzira dok se rotacija  ne zavrsi
        self.while_rotation(rotation)

        print("\n\nIZASAO  JE IZ ROTACIJE\n\n")

        # ***************************************************************************************
        # ********************************** TRANSLATION ****************************************
        # **************************************************************************************

        # Menja smer ako ide unazad negativnom smeru
        # if not direction_is_forward:
        #     distance = -distance

        if self.DEBUG_FOR_GO:
            print('\nSALJE poziciji distancu = ', distance, "\n")

        # Salje regulaciji zeljenu distancu i postavlja regulacione parametre
        self.translation_parameters()
        self.position.W_d = distance

        # petlja koja pauzira dok se translacija ne zavrsi
        self.while_translate(distance, data.x_current, data.y_current, False)

        if self.DEBUG_FOR_GO:
            print("\n   IZLAZI IZ TRANSLACIJE    \n")

# ---------------------------------------STOP-----------------------------------------------------------------

    def stop(self):
        f_current = data.f_current
        print("stopping ... ", f_current)
        self.position.stop()
        time.sleep(data.stop_time*(2/3))
        self.position.reset_position()

        self.translation_parameters()
        self.rotation_parameters()
        self.position.W_F = f_current
        time.sleep(data.stop_time*(1/3))

        print('\n  SENSOR  STOP   \n')


# ----------------------------------------------------------------------------------------------------------------
    # ****************************************************************************************
    # **********************************PETLJE CEKANJA TRANSLACIJE I ROTACIJE *****************
    # ******************************************************************************************
# ----------------------------------------------------------------------------------------------------------------


    def while_translate(self, distance, __x, __y, is_coordinate_moving):

        timer = 0
        timer_still_running = True

        # izracunava dozvoljeno vreme
        allowed_time = self.distance_time(distance)
        if allowed_time < 3:
            allowed_time = 3

        while timer_still_running and self.error_distance(distance, __x, __y, is_coordinate_moving) \
                and not data.stop and not data.budz:
            # stoperica
            time.sleep(0.01)
            timer += .1

            if self.DEBUG_FOR_WHILE:
                print("\n\nTIMER translate set on : {} time is : {}\n\n".format(
                    allowed_time, timer))

            # uslov za kraj
            if allowed_time < timer/10 or allowed_time == 0:
                timer_still_running = False

        if not data.stop:
            time.sleep(data.MovingData.pause_when_ending_moving)


# ----------------------------------------------------------------------------------------------------------------


    def while_rotation(self, rotation):

        timer = 0
        timer_still_running = True

        # izracunava dozvoljeno vreme
        allowed_time = self.rotation_time(rotation, data.f_current)
        if allowed_time < 1:
            allowed_time = 1

        while timer_still_running and self.error_angle(rotation, data.f_current) \
                and not data.stop and not data.budz:
            # stoperica
            time.sleep(.01)
            timer += .1

            if allowed_time < timer/10 or allowed_time == 0:
                timer_still_running = False

            if self.DEBUG_FOR_WHILE:
                print("while rotation, time not over passed = ", timer_still_running,
                      "\ntimer =", timer, "\ndozvoljeno vreme = ", allowed_time, "\n")

        if not data.stop:
            time.sleep(data.MovingData.pause_when_ending_moving)


# ----------------------------------------------------------------------------------------------------------------


    def rotation_time(self, wanted_angle, current_angle):
        # vreme u milisekundamo po stepenu
        ms = data.MovingData.ms_one_degre
        # racun za vreme rotacije
        if abs(wanted_angle - current_angle) <= 180:
            rotation_time = (abs(wanted_angle - current_angle)) * ms
            return abs(round(rotation_time))
        else:
            rotation_time = (360 - abs(wanted_angle - current_angle)) * ms
            return abs(rotation_time)

# ----------------------------------------------------------------------------------------------------------------
    def distance_time(self, wanted_distance):
        translation_time = wanted_distance * \
            data.MovingData.robot_speed  # racunam da je u milimetrima
        return abs(translation_time)

# ----------------------------------------------------------------------------------------------------------------
    def error_angle(self, wanted_angle, current_angle):

        # zeljeni ugao
        if wanted_angle < 0:
            wanted_angle = 360+wanted_angle

        # tolerancija
        tolerance = data.MovingData.angle_tolerance

        # greska u uglu,stavlja u opseg 360 do -360
        angle_error = abs(wanted_angle - current_angle)
        if angle_error > 360:
            angle_error -= 360
        elif angle_error < -360:
            angle_error += 360

        if self.DEBUG_FOR_WHILE:
            print('Eror Angle\nTrenutna greska u uglu  = ', angle_error, '\nstvarni ugao = ', current_angle,
                  '   x=', data.x_current, '    y = ', data.y_current, '   zeljeni ugao = ', wanted_angle, "\n\n")

        # uslov za dozvoljenu gresku
        if angle_error <= tolerance or abs(angle_error - 360) <= tolerance:
            return False
        else:
            return True

# ----------------------------------------------------------------------------------------------------------------
    def error_distance(self, wanted_distance, coordinate_x, coordinate_y, is_coordinate_type):

        # tolerancija
        tolerance = data.MovingData.distance_tolerance
        # Gleda da li je je kretanje zatato preko kordinata
        if is_coordinate_type:  # kada se zadaje preko koordinata

            # trenutne kordinate
            xt = data.x_current
            yt = data.y_current

            # trenutna distanca do cilja
            path = Path(xt, yt, 0)
            self.current_distance = path.distance(coordinate_x, coordinate_y)

            if self.DEBUG_FOR_WHILE:
                print('\nEror Distance\nTrenutna greska u distanci  =', self.current_distance, '\nx = ', xt, '\ny = ',
                      yt, '\nxz = ', coordinate_x, '\n    yz = ', coordinate_y, "\n trenutni ugao",
                      data.f_current, "\nkraj greske u distanci\n\n")

            # uslov za izlazenje
            if self.current_distance <= tolerance:
                return False
        else:  # kada se zadaje preko distance

            # trenutne kordinate
            xt = data.x_current
            yt = data.y_current

            # trenutna distanca do cilja
            path = Path(xt, yt, 0)
            self.current_distance = path.distance(coordinate_x, coordinate_y)
            self.distance_error = abs(wanted_distance) - self.current_distance

            if self.DEBUG_FOR_WHILE:
                print('\nEror Distance\ncurrent_distance  =', self.current_distance, '\nx = ', xt, '\ny = ',
                      yt, '\nxz = ', coordinate_x, '\n    yz = ', coordinate_y, "\n trenutni ugao",
                      data.f_current, "\nwanted_distance", wanted_distance, "\nkraj greske u distanci\n\n",)

            # uslov za izlazenje

            if self.distance_error < tolerance:
                return False

        return True
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
    # ****************************************************************************************
    # **********************************dekijev kod*****************
    # ******************************************************************************************
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------

    def stop_distanca(self):
        # while(data.stop==True):

        self.position_distance.W_F = data.f_current
        self.position_distance.W_D = 0
        # time.sleep(1)

    def rotation_distanca(self, __f):

        self.position_distance.W_F = __f
        if (self.DEBUG_FOR_GO):
            print("ugao koji saljem je   =  ", __f)

        # data.error_existing = \
        self.while_rotation(__f)
        # if (data.error_existing == True):
        #     data.event_rot.add.fire()

    def go_distanca(self, __x, __y, direction_is_forward):

        # napravi objekat p
        p = Path(data.x_current, data.y_current, data.f_current)

        # ROTATION

        # salje rotaciju regulaciji
        rotation = p.rotate(__x, __y)

        if (direction_is_forward == False):
            if (self.DEBUG_FOR_GO):
                print("menja ugao usled direkcije")
            if (rotation >= 0):
                rotation = rotation - 180
            else:
                rotation = rotation + 180

        self.position_distance.W_F = rotation
        if (self.DEBUG_FOR_GO):
            print("ugao koji saljem je   =  ", rotation)

        # daje vreme za koje se radnja treba izvrsiti
        # data.error_existing = \
        self.while_rotation(rotation)
        # if (data.error_existing == True):
        #     data.event_rot.add.fire()
        #     return

        # TRANSLATION
        # daje smer
        distance = p.distance(__x, __y)
        if (direction_is_forward == False):
            if (self.DEBUG_FOR_GO):
                print("menja smer")
            distance = -distance

        # distance
        # salje regulaciji distancu

        self.position_distance.W_d = distance
        if (self.DEBUG_FOR_GO):
            print('SALJE FILIPU distancu OVOOO ===   ', distance)

        # daje vreme za koje se radnja treba izvrsiti
        # data.error_existing = \
        self.while_translate(distance, __x, __y, False)
        # if (data.error_existing == True):
        #
        #     data.event_dis.add.fire()
        #     pass

        # *********************************
