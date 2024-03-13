from enum import Enum
import threading

# *****IZBOR STRATEGIJE*********
chosen_strategy = None
# color = "yellow"
color = "blue"

time_strategy_type = 95000

debug = True

running = threading.Event()

points = 0

SERVO_PORT = "/dev/ttyUSB0"

elapsed_time = 0
start_time = 0

SENSORS_ENABLED = True

ENKODERI = False

budz = False  # NE DIRATI!

# =========================================
# trenutne koordinate
# =========================================
x_current = 0
y_current = 0
f_current = 0

# initial_translate_pojacanje = .62
# initial_rotate_pojacanje = .8
translate_pojacanje = 1
translate_rot_pojacanje = 1
rotate_pojacanje = 1  # bilo 1.2

operations = []

enc_left = 0
enc_right = 0

prev_enc_sum_left = 0
prev_enc_sum_right = 0

# parametri za stajanje
stop = False
end_of_match = False

# parametri za detekciju

lidar_view = 450

distance_when_backing = 100
num_of_attemps = 2
is_front = None
is_back = None
is_detection_front = None
stop_time = 1  # kada staje
backing_time = 1  # kada se vraca nazad

offset = 0

skip_to = None
num_of_skips = 0

sum_encoder_left = 0.0
sum_encoder_right = 0.0

last_MVL = 0
last_MVR = 0


class TypesOfSendParameters(Enum):
    COORDINATE = 0
    ANGLE = 1
    DISTANCE_ANGLE = 3
# -------------------------------


class TypeOfAction(Enum):
    SERVO = 0
    NONE = 3
# -------------------------------


class MovingData:
    '''used primerely in moving.py for tracing correctly moving'''
    # brzina pri kretanju
    ms_one_degre = 0.02  # 0.0084
    robot_speed = 5/1000

    pause_when_ending_moving = 0.1  # 0.3 # 0.15

    tim_chedova = False

    angle_tolerance = 3  # dozvoljene greska
    distance_tolerance = 10  # 20


class OdometryData:
    # rodo chnge var to english
    faktor_razlike = 0.997
    inc = 20480.0
    poluprecnik_tocka = 35.72  # 35.75
    polurastojanje_ose_tockova = 152.53  # 152.8  # 152.8  # 151.9  # 152.76
    inc_R = (inc * polurastojanje_ose_tockova) / poluprecnik_tocka
    inc_deg = 360.0 / inc_R  # Inkremenata po stepenu
    inc_mm = (2.0 * poluprecnik_tocka * 3.1416) / \
        inc  # 1687 #Inkremenata po mm

# --------------------------------


class IDS(Enum):
    # id_bldc = 51
    id_centar = 12  # 355 napred # 5 nazad # 180 centar
    id_gripper_front_1 = 11  # otvoren 140; zatvoren 230
    id_gripper_front_2 = 2  # otvoren 140; zatvoren 230
    id_gripper_front_3 = 8  # otvoren 140; zatvoren 230
    id_gripper_back_1 = 9  # otvoren 140; zatvoren 230
    id_gripper_back_2 = 7  # otvoren 140; zatvoren 230
    id_gripper_back_3 = 3  # otvoren 140; zatvoren 230
    id_trougao = 6  # donja - 0, gornja - 340
    id_front_arm = 41  # spustena skroz - 60, podignuta 120
    id_back_arm = 52  # spustena - 150, podignuta - 210
    id_grtalica_prednja_leva = 5
    id_grtalica_prednja_desna = 10
    id_grtalica_zadnja_leva = 1
    id_grtalica_zadnja_desna = 4
    # id_doser = 7  # load - 1, unload - 359


sleep = False
cinc = 0

x_veliki = 0
y_veliki = 0
f_veliki = 0

sensor_front_left = 0
sensor_front_right = 0
sensor_back_left = 0
sensor_back_right = 0

front_lidar_detection = False
back_lidar_detection = False

cake_sensor = 0


class Sensors(Enum):
    FRONT_ON = 0
    BACK_ON = 1
    ALL_OFF = 4


sensors = Sensors.ALL_OFF
lidar = Sensors.ALL_OFF

TIMEOUT_FOR_LAST_STEPS = False
