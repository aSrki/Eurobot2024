from data import IDS
from data import Sensors
import data
from strategies.steps import *
from servo.XL430 import parallel_rotate


class Strategy:
    front_sensors = False
    back_sensors = False
    front_lidar = False
    back_lidar = False

    def __init__(self):
        self.operations = []
        self.thread = False
        self.add_to_step = False
        # self.rotate_to(data.f_current)

    def add_points(self, type, points):
        task_points = Points(type, points)
        self.operations.append(task_points)

    def all_off(self):
        Strategy.front_sensors = False
        Strategy.front_lidar = False
        Strategy.back_sensors = False
        Strategy.back_lidar = False

    def front_all_on(self, lidar_view=data.lidar_view):
        Strategy.front_sensors = True
        Strategy.front_lidar = True
        data.lidar_view = lidar_view

    def front_all_off(self):
        Strategy.front_sensors = False
        Strategy.front_lidar = False

    def back_all_on(self, lidar_view=data.lidar_view):
        Strategy.back_sensors = True
        Strategy.back_lidar = True
        data.lidar_view = lidar_view

    def back_all_off(self):
        Strategy.back_sensors = False
        Strategy.back_lidar = False

    def front_sensors_on(self):
        Strategy.front_sensors = True

    def front_sensors_off(self):
        Strategy.front_sensors = False

    def back_sensors_on(self):
        Strategy.back_sensors = True

    def back_sensors_off(self):
        Strategy.back_sensors = False

    def front_lidar_on(self, lidar_view=data.lidar_view):
        Strategy.front_lidar = True
        data.lidar_view = lidar_view

    def front_lidar_off(self):
        Strategy.front_lidar = False

    def back_lidar_on(self, lidar_view=data.lidar_view):
        Strategy.back_lidar = True
        data.lidar_view = lidar_view

    def back_lidar_off(self):
        Strategy.back_lidar = False

    def start_parallel(self):
        self.thread = True

    def end_parallel(self, sleep=0):
        self.thread = False
        action = Action.wait(sleep)

        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def set_skip_flag(self, flag):
        skip = Skip()
        skip.skip_to_flag = flag
        skip.is_start = True
        self.operations.append(skip)

    def skip_to_flag(self, flag):
        skip = Skip()
        skip.skip_to_flag = flag
        skip.is_start = False
        self.operations.append(skip)

    def end(self):
        end = End()
        self.rotate_to(data.f_current)
        self.operations.append(end)

    def start_step_actions(self):
        self.add_to_step = True

    def end_step_actions(self):
        self.add_to_step = False

    def check_time(self, time, flag=None):
        check = TimeCheck(time, flag)
        self.operations.append(check)

    # def check_cake(self):
    #     check = CheckCakes()
    #     self.operations.append(check)

    def add_sequence(self, sequence):
        '''sequence - lista operacija'''
        if self.add_to_step:
            for s in sequence:
                self.operations[-1].actions.append(s)
        else:
            for s in sequence:
                self.operations.append(s)

    def move_mechanism(self, a, v=100, s=0.1, da=0):
        '''a = napred: 315, nazad: 5, centar: 180, v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_centar.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def move_front_arm(self, a, v=50, s=0.1, da=0):
        '''a - gore: 120, dole: 60, v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_front_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def move_back_arm(self, a, v=50, s=0.1, da=0):
        '''a - gore: 210, dole: 150, v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_back_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def grip_front(self, a1, a2, a3, v=100, s=0.1, da=0):
        '''1: zatvoren 180, otvoren 90,
           2: zatvoren 180, otvoren 90,
           3: zatvoren 270, otvoren 180,
           v - velocity, s - sleep time, da - delay action in step'''
        # action = parallel_rotate([IDS.id_gripper_front_1.value, IDS.id_gripper_front_2.value, IDS.id_gripper_front_3.value], [a1, a2, a3])
        # if self.add_to_step:
        #     action.delay_action = da
        #     self.operations[-1].actions.append(action)
        # else:
        #     self.operations.append(action)
        action = Action.move_servo(
            IDS.id_gripper_front_1.value, angle=a1, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        action = Action.move_servo(
            IDS.id_gripper_front_2.value, angle=a2, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        action = Action.move_servo(
            IDS.id_gripper_front_3.value, angle=a3, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        if not self.thread:
            action = Action.wait(s)

            if self.add_to_step:
                action.delay_action = da
                self.operations[-1].actions.append(action)
            else:
                self.operations.append(action)

    def grip_back(self, a1, a2, a3, v=100, s=0.1, da=0):
        '''1: zatvoren 180, otvoren 90,
           2: zatvoren 180, otvoren 90,
           3: zatvoren 90, otvoren 0,
           v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(
            IDS.id_gripper_back_1.value, angle=a1, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        action = Action.move_servo(
            IDS.id_gripper_back_2.value, angle=a2, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        action = Action.move_servo(
            IDS.id_gripper_back_3.value, angle=a3, velocity=v, sleep=s, thread=True
        )
        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

        if not self.thread:
            action = Action.wait(s)

            if self.add_to_step:
                action.delay_action = da
                self.operations[-1].actions.append(action)
            else:
                self.operations.append(action)

    def activate_triangle(self, v=100, s=0.1, da=0):
        '''a = ne prosledjuje mu se ugao samo pozivas funkciju sa odgovarajucim imenom'''
        action = Action.move_servo(IDS.id_trougao.value, angle=0,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def deactivate_triangle(self, v=100, s=0.1, da=0):
        '''a = ne prosledjuje mu se ugao samo pozivas funkciju sa odgovarajucim imenom'''
        action = Action.move_servo(IDS.id_trougao.value, angle = 0,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def go_to_XY(self, x, y, d=True, g=1, s=0, ss=data.stop_time, bs=data.backing_time, at=data.num_of_attemps, b=data.distance_when_backing, ns=data.num_of_skips, off=0):
        '''d - direction, g - gain, s - sleep, ss - sleep after detection, bs - sleep after backing, at - number of avoidance attemps, b - distance when backing, ns - number of steps to skip if detected without flags'''
        if Strategy.front_sensors:
            sensors = Sensors.FRONT_ON
        elif Strategy.back_sensors:
            sensors = Sensors.BACK_ON
        else:
            sensors = Sensors.ALL_OFF

        if Strategy.front_lidar:
            lidar = Sensors.FRONT_ON
        elif Strategy.back_lidar:
            lidar = Sensors.BACK_ON
        else:
            lidar = Sensors.ALL_OFF

        step = Step.go_to_XY(
            x, y, direction=d, gain=g, sleep=s, sensor=sensors,
            lidar=lidar, backing=b, attemps=at, stop_sleep=ss,
            backing_sleep=bs, num_of_skips=ns, offset=off
        )
        self.operations.append(step)

    def set_distance_angle(self, d, a, g=1, s=0, ss=data.stop_time, bs=data.backing_time, at=data.num_of_attemps, b=data.distance_when_backing, ns=data.num_of_skips):
        '''d - distance, a - angle, g - gain, s - sleep, ss - after detection sleep, bs - after backing sleep, at - number of avoidance attemps, b - distance when backing, ns - number of steps to skip if detected without flags'''
        if Strategy.front_sensors:
            sensors = Sensors.FRONT_ON
        elif Strategy.back_sensors:
            sensors = Sensors.BACK_ON
        else:
            sensors = Sensors.ALL_OFF

        if Strategy.front_lidar:
            lidar = Sensors.FRONT_ON
        elif Strategy.back_lidar:
            lidar = Sensors.BACK_ON
        else:
            lidar = Sensors.ALL_OFF

        step = Step.set_distance_angle(
            distance=d, angle=a, gain=g, sleep=s, sensor=sensors,
            lidar=lidar, backing=b, attemps=at, stop_sleep=ss,
            backing_sleep=bs, num_of_skips=ns
        )
        self.operations.append(step)

    def rotate_to(self, a, s=0):
        '''a - angle, s - sleep'''

        step = Step.rotate_to(angle=a, sleep=s)
        self.operations.append(step)
