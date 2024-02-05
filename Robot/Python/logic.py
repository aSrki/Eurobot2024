import data
import threading
from strategies.choose_strategy import chooses_strategy
from strategies.timeout.timeout_strategies import get_last_steps
from strategies.steps import *
import time
from communication.communication_with_lidar import Communication_with_lidar
from lidar.obstacle_detector import initialize_lidar

# from align import Align


class Logic:
    budz2 = True  # srle ne diraj ovo <3
    initialize_lidar()
    lidar = Communication_with_lidar()
    lidar.start()

    def __init__(self):
        self.Chose_strategy = chooses_strategy()
        self.chosen_strategy = []

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        print("*** LOGIC *** ")

        self.chosen_strategy = self.Chose_strategy.chosen_steps

        self.adding()

        while True:
            # print(data.data_skip_step)
            # print(not data.detection.is_stopped , self.are_sensors_detected())
            if data.TIMEOUT_FOR_LAST_STEPS and self.budz2:
                self.budz2 = False
                data.stop_time = 0
                data.stop = True
                self.get_last_steps()

            elif not data.detection.is_stopped and self.are_sensors_detected():
                # print("\n\t\t!!!DETECTED!!!")
                data.stop = True

            elif data.detection.is_stopped:
                self.set_steps_for_detection()
                data.stop = False
                time.sleep(.2)

            time.sleep(.008)

    def get_last_steps(self):
        print('***************  TIMEOUT GO HOME **************')
        data.log.add_info_message("TIMEOUT GO HOME")
        data.stop_time = 0
        steps = get_last_steps()
        time.sleep(.5)
        data.steps = steps
        time.sleep(.2)
        data.stop = False
        data.detection.restart(type=data.TypeOfDetection.WHILE_MOVING)

    def set_steps_for_detection(self):

        if data.detection.type_of_detection == data.TypeOfDetection.WHILE_MOVING:
            print(
                f"\n\n\t\t*******************!!!WHILE_MOVING{data.sensors}!!!*******************\n\n")

            data.curr_step -= 1
            print('CURR STEP ', data.curr_step)
            if self.are_sensors_detected():
                data.steps.append(self.get_backing_step())
                self.adding()
                data.detection.restart(type=data.TypeOfDetection.WHILE_BACKING)
            else:
                self.adding()
                data.detection.restart(
                    type=data.TypeOfDetection.WHILE_AFTER_BACKING)
            # data.steps.append(self.get_backing_step())
            # self.adding()
            #
            # data.detection.restart(type=data.TypeOfDetection.WHILE_BACKING)

        elif data.detection.type_of_detection == data.TypeOfDetection.WHILE_BACKING:
            print(
                f"\n\n\t\t*******************!!!WHILE_BACKING DEAD{data.sensors}!!!*******************\n\n")
            # data.curr_step -= (1 - data.num_of_jump_steps)
            # print('CURR STEP backing', data.curr_step)
            time.sleep(3)
            data.steps.extend(self.get_steps_for_path_correction())
            data.curr_step -= 1
            self.adding()

            data.detection.restart(
                type=data.TypeOfDetection.WHILE_AFTER_BACKING)

        elif data.detection.type_of_detection == data.TypeOfDetection.WHILE_AFTER_BACKING:
            print(
                f"\n\n\t\t*******************!!!WHILE AFTER_BACKING{data.sensors}!!!*******************\n\n")
            self.skip_steps()
            # data.steps.append(self.get_steps_for_path_correction())
            data.detection.restart(type=data.TypeOfDetection.WHILE_MOVING)

        else:
            print("\n\n\t\t*******************!!! NANIIIIIIII!!*******************\n\n")
            print(data.detection.type_of_detection)

    def skip_steps(self):
        print(f'**************SKIP STEPS {data.use_skip}*************')

        if data.use_skip:
            # data.curr_step -= (1 - data.num_of_jump_steps)
            for x in range(data.curr_step, len(self.chosen_strategy)):
                print(
                    f"Adding step {x} , {self.chosen_strategy[x].skip_flag} , {self.chosen_strategy[x].x}")
                data.curr_step = x
                if self.chosen_strategy[x].skip_flag == data.use_skip:
                    data.curr_step = x
                    break
            print('CURR STEP backing', data.curr_step)
            self.adding()
        else:
            data.curr_step -= (1 - data.num_of_jump_steps)
            print('CURR STEP backing', data.curr_step)
            self.adding()

    def get_steps_for_path_correction(self):
        step = Step()
        step.type_of_parameters = TypesOfSendParameters.NEITHER
        step.angle = data.f_current
        step.sleep = 2

        step2 = Step()
        step2.type_of_parameters = TypesOfSendParameters.NEITHER
        step2.angle = data.f_current
        step.sleep = 1
        return [step, step2]

    def get_backing_step(self):
        step = Step()
        step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE

        step.angle = data.f_current
        # step.distance = -data.distance_when_backing
        if data.detection.is_front:
            step.distance = -data.distance_when_backing
            step.angle = 0  # data.f_current
            # step.direction_is_forward = False
            step.sensor = Sensors.BACK_ON

        else:
            step.distance = data.distance_when_backing
            step.sensor = Sensors.FRONT_ON
        step.inserted = True
        step.sleep = data.backing_time

        return step

    def front_sensors(self):
        if data.sensor_front_left or data.sensor_front_right or data.frontLidarDetection:
            print("front detection")
            data.log.add_info_message("front detection")
            return True
        return False

    def back_sensors(self):
        if data.sensor_back_left or data.sensor_back_right or data.backLidarDetection:
            print("back detection")
            data.log.add_info_message("back detection")
            return True
        return False

    def are_sensors_detected(self):
        return self.back_sensors() or self.front_sensors()

    def adding(self, is_detected=False):
        if is_detected:
            data.curr_step -= 1

        for x in range(data.curr_step, len(self.chosen_strategy)):
            print(f"Adding step {x} ")
            data.steps.append(self.chosen_strategy[x])
