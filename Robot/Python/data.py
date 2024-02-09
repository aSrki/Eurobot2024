from enum import Enum
import threading

# *****IZBOR STRATEGIJE*********
chosen_strategy = None
plate = None
color = None

time_strategy_type = 95000

debug = True

running = threading.Event()

points = 0

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
is_detection_front = None
stop_time = 1  # kada staje
backing_time = 1  # kada se vraca nazad

offset = 0

skip_to = None
num_of_skips = 0

sum_encoder_left = 0
sum_encoder_right = 0

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
    ms_one_degre = 0.01  # 0.0084
    robot_speed = 5 #0.74/1000

    pause_when_ending_moving = 0.3  # 0.05

    tim_chedova = False

    angle_tolerance = 3  # dozvoljene greska
    distance_tolerance = 10  # 20


class OdometryData:
    # rodo chnge var to english
    inc = 20480
    poluprecnik_tocka = 35.750 #35.756
    polurastojanje_ose_tockova = 152.76
    inc_R = (inc * polurastojanje_ose_tockova) / poluprecnik_tocka
    inc_deg = 360 / inc_R  # Inkremenata po stepenu
    inc_mm = (2 * poluprecnik_tocka * 3.1416) / inc  # 1687 #Inkremenata po mm


# --------------------------------

class IDS(Enum):
    id_bldc = 51
    id_pusher = 1  # 90 zatvoren # 530 otvoren
    id_gripper = 15  # otvoren 48; zatvoren 60
    id_lift = 11  # donja - 0, gornja - 340
    id_vacuum = 41  # 41 za XM  # sredina - 325, na desno manji ugao, na levo veci ugao
    id_reservoir_door = 6  # zatvoren - 160, otvoren - 210
    id_doser = 7  # load - 1, unload - 359
    id_cherry_pipe = 4  # zatvoren - 1, otvoren - 190


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
