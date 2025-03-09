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

    object_detection = False

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

    def end_parallel(self, s=0):
        # s - sleep
        self.thread = False
        action = Action.wait(s)

        if self.add_to_step:
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)
#nove za izbaciti?
    def set_skip_flag(self, flag):
        skip = Skip()
        skip.skip_to_flag = flag
        skip.is_start = True
        self.operations.append(skip)
#bilo set_plant_flag
    def set_object_sensor(self):
        plantflag = SkipPlant()
        plantflag.plant_flag = True
        self.operations.append(plantflag)

    def clear_object_sensor(self):
        plantflag = SkipPlant()
        plantflag.plant_flag = False
        self.operations.append(plantflag)

    def skip_to_flag(self, flag):
        skip = Skip()
        skip.skip_to_flag = flag
        skip.is_start = False
        self.operations.append(skip)

    def end(self):
        end = End()
        # self.rotate_to(data.f_current)
        self.operations.append(end)

    def start_step_actions(self):
        self.add_to_step = True

    def end_step_actions(self):
        self.add_to_step = False

    def check_time(self, time, flag=None):
        check = TimeCheck(time, flag)
        self.operations.append(check)

    def check_object(self):
        # data.set_flag = flag
        check = CheckObject()
        self.operations.append(check)

    def check_cam(self, priorities=None):
        cam = Cam()
        cam.priorities = priorities
        self.operations.append(cam)

    def add_sequence(self, sequence):
        '''sequence - lista operacija'''
        if self.add_to_step:
            for s in sequence:
                self.operations[-1].actions.append(s)
        else:
            for s in sequence:
                self.operations.append(s)

######################## MOJE STRATEGIJE ########################

    ## umesto ID, napraviti klasu sa magnetima, pa njih pozivati, ali mogu preko move_servo vrv ali ID preko 40 ili 60
    # def magnets_on(self, v=50, s=0.1, da=0):
    #     # '''a = ne prosledjuje mu se ugao samo pozivas funkciju sa odgovarajucim imenom'''
    #     # action = Action.move_servo(IDS.id_trougao.value, angle=0,
    #     #                            velocity=v, sleep=s, thread=self.thread)
    #     # if self.add_to_step:
    #     #     action.delay_action = da
    #     #     self.operations[-1].actions.append(action)
    #     # else:
    #     #     self.operations.append(action)
        
    

    # funkcija sluzi za rotiranje ruke oko z-ose
    def rotate_right_hand(self, a, v=50, s=0.1, da=0):
        # 180 start -> max pos 90    ID 8
        '''a = pocetni: 180, desno: 125, max: 90 ; v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_right_lower_hand.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    # funkcija sluzi za rotiranje ruke oko z-ose
    def rotate_left_hand(self, a, v=50, s=0.1, da=0):
        # levo dole 90 start -> max pos 180   ID 10
        '''a = pocetni: 90, levo: 145, max: 180 ; v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_left_lower_hand.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    #funkcija sluzi za obrtanje ruke/konzerve na dasku
    def flip_right_hand(self, a, v=50, s=0.1, da=0):
        # desno gore 270 start -> max pos 90    ID 1
        '''a = pocetni: 270, flip: 180, max: 90 ; v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_right_upper_hand.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    #funkcija sluzi za obrtanje ruke/konzerve na dasku
    def flip_left_hand(self, a, v=50, s=0.1, da=0):
        # levo gore 90 start -> max pos 270   ID 5
        '''a: pocetni-> 90, srednji-> 180, max: 270 ; v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_left_upper_hand.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def ram(self, a = 250, v=50, s=0.1, da=0):
        # ID 4
        '''a = pocetni: 325, krajnji: 250 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_rammer.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)
    
    def release(self, a = 325, v=50, s=0.1, da=0):
        # ID 4
        '''a = pocetni: 325, krajnji: 250 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_servo(IDS.id_rammer.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def move_back_wall(self, a, v=100, s=0.1, da=0):
        # ID 55
        '''a = pocetni: 0, krajnji: 250 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_maxon_wall(IDS.id_back_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def move_front_wall(self, a, v=100, s=0.1, da=0):
        # ID 56
        '''a = pocetni: 0, krajnji: 140 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.move_maxon_wall(IDS.id_front_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def left_arm_on(self, a = 1, v=50, s=0.1, da=0):
        # ID = 57
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_left_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def left_arm_off(self, a = 0, v=50, s=0.1, da=0):
        # ID = 57
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_left_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def right_arm_on(self, a = 1, v=50, s=0.1, da=0):
        # ID = 58
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_right_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def right_arm_off(self, a = 0, v=50, s=0.1, da=0):
        # ID = 58
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_right_arm.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def front_wall_on(self, a = 1, v=50, s=0.1, da=0):
        # ID = 59
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_front_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def front_wall_off(self, a = 0, v=50, s=0.1, da=0):
        # ID = 59
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_front_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def back_wall_on(self, a = 1, v=50, s=0.1, da=0):
        # ID = 60
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_back_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)

    def back_wall_off(self, a = 0, v=50, s=0.1, da=0):
        # ID = 60
        '''a = iskljucen: 0, ukljucen: 1 , v - velocity, s - sleep time, da - delay action in step'''
        action = Action.relay_wall_arm(IDS.id_relay_back_wall.value, angle=a,
                                   velocity=v, sleep=s, thread=self.thread)
        if self.add_to_step:
            action.delay_action = da
            self.operations[-1].actions.append(action)
        else:
            self.operations.append(action)




    def go_to_XY(self, x, y, d=True, g=1, s=0, ss=data.stop_time, bs=data.backing_time, at=data.num_of_attemps, b=data.distance_when_backing, ns=data.num_of_skips, off=0, ts=data.top_speed):
        '''d - direction, g - gain, s - sleep, ss - sleep after detection, bs - sleep after backing, at - number of avoidance attemps, b - distance when backing, ns - number of steps to skip if detected without flags, ts - top speed gain'''
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
            backing_sleep=bs, num_of_skips=ns, offset=off, top_speed=ts
        )
        self.operations.append(step)

    def set_distance_angle(self, d, a, g=1, s=0, ss=data.stop_time, bs=data.backing_time, at=data.num_of_attemps, b=data.distance_when_backing, ns=data.num_of_skips, ts=data.top_speed):
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
            backing_sleep=bs, num_of_skips=ns, top_speed=ts
        )
        self.operations.append(step)

    def rotate_to(self, a, s=0):
        '''a - angle, s - sleep'''

        step = Step.rotate_to(angle=a, sleep=s)
        self.operations.append(step)
