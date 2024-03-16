from servo.servo_moving import Servo_Moving
from servo.XL430 import parallel_rotate
# from strategies.timeout.timeout_strategies import get_last_steps
import threading
from regulation_controller.moving import Moving
from strategies.tasks import *
from strategies.steps import *
import data
import time

DEBUG = True


def custom_print(msg):
    if DEBUG:
        print(msg)


class Execute:

    def __init__(self):
        self.servo = Servo_Moving()
        self.servo.home()
        self.moving = Moving()

        # Inicijalno salje nula na motore ako esp nastavi nesto da salje
        self.moving.position.maxon_right.rotate_with_rpm(0)
        self.moving.position.maxon_left.rotate_with_rpm(0)

        self.servo_threads = []
        self.bldc_thread = threading.Thread()
        self.step_actions_thread = threading.Thread()

        self.debug = True
        self.operation = None

        # True ako treba da izvrsi izbegavanje odlaskom unazad/napred i onda da preskoci stepove
        self.inserted_step = 0
        self.backing = False  # ako je trenutno u backingu
        self.num_of_detections = 0  # da li je u trenutnom stepu doslo do detekcije

        self.skipping = False
        self.last_angle = 0

        self.last_flag = None

        self.raised_timeout = False

    def start(self):
        # Pokretanje execute threada
        self.moving.start()

        threading.Thread(target=self.run).start()

    def run(self):
        custom_print("EXECUTING")

        while True:
            if len(data.operations) and not data.stop:
                # provera da li je kod zaustavljen
                if not data.running.is_set():
                    break

                if data.TIMEOUT_FOR_LAST_STEPS and not self.raised_timeout:
                    custom_print(f"TIMEOUT: {data.elapsed_time}")

                    data.TIMEOUT_FOR_LAST_STEPS = False
                    data.end_of_match = True

                    # preskace do pretposlednjeg skip flaga
                    data.skip_to = "timeout"
                    self.skipping = True
                    self.moving.stop()

                # citanje sledece operacije
                self.operation = data.operations.pop(0)

                custom_print(self.operation)
                custom_print(data.skip_to)

                if isinstance(self.operation, End) and not self.skipping:
                    # data.running.clear()
                    data.operations.clear()
                    continue

                elif isinstance(self.operation, Skip):
                    if self.operation.is_start and not self.skipping:
                        data.skip_to = self.operation.skip_to_flag
                    elif data.skip_to == self.operation.skip_to_flag and not self.operation.is_start:
                        custom_print(f"DONE SKIPPING FLAG {data.skip_to}")

                        data.skip_to = None

                        self.skipping = False

                    # za reset flaga
                    elif not self.skipping:
                        data.skip_to = None
                    continue

                # Provera da li treba da skipuje u zavisnosti od vremena
                elif isinstance(self.operation, TimeCheck) and not self.skipping:
                    if self.operation.skip_to_flag == "timeout":
                        data.skip_to = "timeout"
                        self.raised_timeout = True
                        self.skipping = True
                        print(f"TIMEOUT TIME: {data.elapsed_time}")

                    elif self.operation.time < data.elapsed_time:
                        self.skipping = True

                    continue

                # TODO: preimenovati imena flagova na relevantne
                elif isinstance(self.operation, Points) and not self.skipping:
                    if self.operation.type == "sort":
                        data.points += self.operation.points
                    elif self.operation.type == "unload":
                        data.points += self.operation.points

                # Ako je preskakao do flaga
                if data.skip_to != None and self.skipping:
                    if self.inserted_step:
                        self.inserted_step -= 1
                        data.sensors = self.operation.sensor
                        data.lidar = self.operation.lidar
                        self.choose_type_of_moving(self.operation)
                    else:
                        self.backing = False

                    custom_print(f"SKIPPING TO FLAG {data.skip_to}")

                    continue
                # Ako je preskakao zeljeni broj
                elif self.skipping:
                    if self.inserted_step:
                        self.inserted_step -= 1
                        data.sensors = self.operation.sensor
                        data.lidar = self.operation.lidar
                        self.choose_type_of_moving(self.operation)
                    elif isinstance(self.operation, Step):
                        if data.num_of_skips > 0:
                            data.num_of_skips -= 1
                            custom_print(
                                f"SKIPPING {data.num_of_skips} MORE STEPS")
                            continue
                        else:
                            self.skipping = False
                            custom_print("DONE SKIPPING STEPS")
                    else:
                        custom_print("SKIPPING OPERATION NOT STEP")
                        continue

                custom_print(
                    f"Current position: \nx={data.x_current} y={data.y_current} angle={data.f_current}")

                # provera kog tipa je operacija
                if isinstance(self.operation, Action):
                    data.sensors = Sensors.ALL_OFF
                    data.lidar = Sensors.ALL_OFF

                    self.execute_action(self.operation)
                    time.sleep(self.operation.sleep)

                elif isinstance(self.operation, Step):
                    # ako u toku stepa treba da se izvrse neke akcije one se stavljaju u poseban thread

                    if len(self.operation.actions) != 0:
                        self.thread_step_actions(self.operation)

                    if not self.backing:
                        data.stop_time = self.operation.stop_sleep  # u metodama kretanja parametar ss
                        # u metodama kretanja parametar bs
                        data.backing_time = self.operation.backing_sleep
                        # u metodama kretanja parametar d
                        data.distance_when_backing = self.operation.distance_when_backing
                        # u metodama kretanja parametar ns
                        data.num_of_skips = self.operation.num_of_skips

                    data.sensors = self.operation.sensor
                    data.lidar = self.operation.lidar

                    custom_print(f"SENSORS: {self.operation.sensor}")
                    custom_print(f"LIDAR: {self.operation.lidar}")
                    custom_print(f"IN BACKING: {self.backing}")

                    # izvrsavanje stepa u zavisnosti kako je zadato pomeranje
                    self.choose_type_of_moving(self.operation)

                    if not data.stop and not self.backing:
                        time.sleep(self.operation.sleep)

                        if self.step_actions_thread.is_alive():
                            self.step_actions_thread.join()
                    elif not data.stop and self.backing:
                        custom_print("KRAJ DETEKCIJE")
                        self.backing = False

            elif data.stop:
                self.last_angle = data.f_current
                self.moving.stop()

                # TODO: proveriti jer je jako sus
                if data.is_front != None:
                    self.get_steps_for_detection()
                elif data.is_back != None:
                    self.get_steps_for_detection()

        custom_print("END")
        return

    def get_steps_for_detection(self):
        custom_print(
            f"Trying again {self.operation.num_of_attemps - self.num_of_detections} times")

        # Ako ima jos pokusaja izbegavanja treba da ode u nazad/napred i nastavi normalno sa strategijom
        # Ako je prethodno izbegavao ne treba da doda prethodni step ponovo
        if self.num_of_detections < self.operation.num_of_attemps and not self.backing:
            self.num_of_detections += 1
            data.operations.insert(0, self.operation)
        # Ako nema vise pokusaja izbegavanja treba da preskoci sve taskove i stepove do sledeceg flaga
        elif not self.backing:
            self.num_of_detections = 0

            if data.skip_to != None:
                custom_print(f"SKIPPING TO: {data.skip_to}")
            else:
                custom_print(f"SKIPPING TO {data.num_of_skips} STEP")

            self.skipping = True
            self.inserted_step = 2
        elif self.operation.num_of_attemps >= 100:
            custom_print("100 ATTEMPTS")
            self.num_of_detections = 0
            data.operations.insert(0, self.operation)
        else:
            custom_print("DETECTED WHILE BACKING")
            self.num_of_detections = 0

        if data.is_front:
            custom_print("FRONT DETECTED")

            steps = backing_steps(
                self.operation.distance_when_backing, 0, self.operation.backing_sleep, self.last_angle)

        elif data.is_back:
            print("BACK DETECTED")

            steps = forward_steps(
                self.operation.distance_when_backing, 0, self.operation.backing_sleep, self.last_angle)

        # korekcija
        data.operations.insert(0, steps[1])
        # backing step
        data.operations.insert(0, steps[0])

        data.sensors = Sensors.ALL_OFF
        data.lidar = Sensors.ALL_OFF

        self.backing = True
        data.is_front = None
        data.stop = False

    def execute_action(self, operation):
        # prekida izvrsavanje akcije ako je kod zaustavljen
        if not data.running.is_set():
            return

        # izvrsava akciju u zavisnosti koji motor treba da se upali
        if operation.type is TypeOfAction.SERVO:
            custom_print(
                f"SERVO : {operation.servoID}, {operation.angle}, {operation.velocity}")

            # ako treba da se izvrsi paralelno sa sledecom operacijom
            if operation.thread:
                self.servo_threads.append(operation)
            else:
                self.servo.operation(
                    operation.servoID, operation.angle, operation.velocity)
        else:
            custom_print("WAITING")

            # pokrecu se svi servoi koji treba da se izvrse paralelno
            if len(self.servo_threads):
                IDs = []
                angles = []
                for servo in self.servo_threads:
                    IDs.append(servo.servoID)
                    angles.append(servo.angle)

                parallel_rotate(IDs, angles)

            self.servo_threads.clear()

            # ceka da se sve zapocete akcije servoa koje se izvrsavaju paralelno zavrse
            time.sleep(operation.sleep)

    def execute_step_actions(self, step):
        # pokrecu se jedna po jedna akcija koje treba da se izvrse u toku stepa
        for action in step.actions:
            # prekida izvrsavanje ako je kod zaustavljen
            if not data.running.is_set():
                break

            if action.thread:
                self.execute_action(action)
            else:
                while self.moving.current_distance > action.delay_action and \
                        action.delay_action != 0 and \
                        not self.skipping:
                    custom_print("WAITING TO DO ACTION IN STEP")
                    time.sleep(.05)

                self.execute_action(action)

        return

    def choose_type_of_moving(self, step):
        data.translate_pojacanje = step.translate_pojacanje
        data.rotate_pojacanje = step.rotate_pojacanje

        # TODO: ZNAJ DA OVO POSTOJI. JAKO.
        if step.translate_pojacanje < .5:
            data.translate_rot_pojacanje = 1.2
        elif step.translate_pojacanje < .7:
            data.translate_rot_pojacanje = 1.1
        else:
            data.translate_rot_pojacanje = 1

        # Vrste slanja komandi kretanja
        if step.type_of_parameters == data.TypesOfSendParameters.COORDINATE:
            custom_print(
                f"\n\nCordinates->   x='{step.x} ';   step y =' {step.y} ';  step f =' {step.angle} \n\n")
            self.moving.go_using_coordinates(step.x, step.y,
                                             step.direction_is_forward, step.offset)
        elif step.type_of_parameters == data.TypesOfSendParameters.ANGLE:
            custom_print(f"Rotation->   {step.angle} \n\n")
            self.moving.go_using_rotation(step.angle)
        elif step.type_of_parameters == data.TypesOfSendParameters.DISTANCE_ANGLE:
            custom_print(
                "distance_angle -> distance {} , angle {}\n\n".format(step.distance, step.angle))
            self.moving.go_using_distance_angle(
                step.distance, step.angle, step.direction_is_forward)

    def thread_step_actions(self, step):
        self.step_actions_thread = threading.Thread(target=self.execute_step_actions,
                                                    args=(step, ))
        self.step_actions_thread.start()
