from enum import Enum
from data import *


class Action:

    def __init__(self):
        self.type = type

        self.stepperID = -100
        self.servoID = -100

        self.angle = 0
        self.velocity = 0
        self.height = 0
        self.sleep = 0
        self.thread = False
        self.delay_action = 0

    @classmethod
    def wait(cls, sleep=0, delay=0):
        action = cls()
        action.sleep = sleep
        action.type = TypeOfAction.NONE
        action.delay_action = delay
        return action

    @classmethod
    def move_servo(cls, servoID, angle, velocity=100, sleep=0, thread=False, delay=0):
        action = cls()
        action.type = TypeOfAction.SERVO
        action.servoID = servoID
        action.angle = angle
        action.velocity = velocity
        action.sleep = sleep
        action.thread = thread
        action.delay_action = delay
        return action


class Step:

    def __init__(self):

        self.actions = []

        self.x = 3
        self.y = 3

        self.distance = 0
        self.angle = 0

        self.type_of_parameters = TypesOfSendParameters.COORDINATE

        self.sleep = 0
        self.offset = 0

        self.direction_is_forward = True
        self.sensor = Sensors.ALL_OFF
        self.lidar = False

        self.translate_pojacanje = 1
        self.rotate_pojacanje = 1

        self.num_of_attemps = 2
        self.num_of_skips = 1

        self.stop_sleep = 0.5  # sleep pri stajanju kada se desi detekcija
        self.backing_sleep = 0.5  # sleep nakon vracanja u nazad posle detekcije
        self.distance_when_backing = 300  # koliko daleko ce otici u nazad pri detekciji

    @classmethod
    def go_to_XY(cls, x, y, direction=True, gain=1,
                 sleep=0, sensor=Sensors.ALL_OFF, lidar=Sensors.ALL_OFF, stop_sleep=0.5,
                 backing_sleep=0.5, attemps=0, backing=200, num_of_skips=1, offset=0):
        step = cls()
        step.type_of_parameters = TypesOfSendParameters.COORDINATE
        step.x = x
        step.y = y
        step.sleep = sleep
        step.direction_is_forward = direction
        step.translate_pojacanje = gain
        step.sensor = sensor
        step.lidar = lidar
        step.stop_sleep = stop_sleep
        step.backing_sleep = backing_sleep
        step.num_of_attemps = attemps
        step.num_of_skips = num_of_skips
        step.distance_when_backing = backing
        step.offset = offset
        return step

    @classmethod
    def set_distance_angle(cls, distance, angle, sleep=0, sensor=Sensors.ALL_OFF,
                           lidar=False, gain=1, stop_sleep=0.5, backing_sleep=0.5,
                           attemps=2, backing=300, num_of_skips=1):
        step = cls()
        step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
        step.distance = distance
        step.angle = angle
        step.sleep = sleep
        step.sensor = sensor
        step.lidar = lidar
        step.stop_sleep = stop_sleep
        step.backing_sleep = backing_sleep
        step.num_of_attemps = attemps
        step.distance_when_backing = backing
        step.num_of_skips = num_of_skips
        step.translate_pojacanje = gain
        return step

    @classmethod
    def rotate_to(cls, angle, sleep=0, sensor=Sensors.ALL_OFF, lidar=Sensors.ALL_OFF):
        step = cls()
        step.type_of_parameters = TypesOfSendParameters.ANGLE
        step.angle = angle
        step.sleep = sleep
        step.sensor = sensor
        step.lidar = lidar
        return step


class TimeCheck:

    def __init__(self, time=0, flag=0):
        self.time = time
        self.skip_to_flag = flag


class CheckObject:

    def __init__(self):
        pass


class Skip:

    def __init__(self):
        self.skip_to_flag = 1
        self.is_start = False


class End:

    def __init__(self):
        pass


class Points:

    def __init__(self, type, points):
        self.type = type
        self.points = points
