import data
from strategies.choose_strategy import choose_strategy
from servo.servo_moving import Servo_Moving
import time
from sensors import SensorsDetection
import socket
from lidar.lidar_detection import LidarDetection

DEBUG = True

# PROMENITI OVAJ IP NA SIMIN
# PROMENITI U LINIJI 69, heh, BOJU POCETNU
# za menjanje stratrgije na simi i prebacivanje putanja je /home/sima1/sima/Dynamixel-XL430-W250
# fajl sa koordinatama je strategy.py
sima1_IP = '192.168.1.143'
sima2_IP = '192.168.1.212'
sima3_IP = '192.168.1.192'


def custom_print(msg):
    if DEBUG:
        print(msg)
    # data.log.add_info_message(str(msg))


class Main:
    debug = True
    start_time = 0
    first_basket = True

    def start(self):
        try:
            custom_print("STARTING")

            # kada se clearuje prekida sve niti koje se izvrsavaju nezavisno
            data.running.set()

            data.elapsed_time = 0
            data.points = 0
            data.start_time = 0

            # client = Client()
            # client.start()

            # server = Server()
            # server.start()

            # izbor strategije u zavisnosti od data.chosen_strategy_small
            data.operations = choose_strategy().copy()

            # pokretanje senzora za detekciju
            sensors = SensorsDetection()
            sensors.start()

            # ================================================INIT SERVOA
            # self.servo = Servo_Moving()
            # self.servo.home()
            # ===========================================================

            # a = input("Press ENTER to start: ")

            from execute import Execute

            # pokretanje execute threada
            self.execute = Execute()
            # self.execute.start()

            self.lidar = LidarDetection()

            # self.basket_comm = BasketCommunication()

            # =================sima==============

            try:
                host = sima1_IP
                port = 12345

                s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                s1.settimeout(1)

                s1.connect((host, port))

                print("Sima se povezao")

            except Exception as e:
                print(f"Sima 1 nije na mrezi: {e}")
                pass

            try:
                host = sima2_IP
                port = 12345

                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                s2.settimeout(1)

                s2.connect((host, port))

                print("Sima se povezao")

            except Exception as e:
                print(f"Sima 2 nije na mrezi: {e}")
                pass

            try:
                host = sima3_IP
                port = 12345

                s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                s3.settimeout(1)

                s3.connect((host, port))

                print("Sima se povezao")

            except Exception as e:
                print(f"Sima 3 nije na mrezi: {e}")
                pass

            # =================kraj sima==============

            # a = input("Press ENTER OPET to start: ")

            print("Waiting for CINC")
            while data.cinc == 0:
                continue

            try:
                s1.sendall(data.color.encode())
                s2.sendall(data.color.encode())
                s3.sendall(data.color.encode())

                print("Simama je poslato")
            except Exception as e:
                print(f"nije poslato jer: {e}")

            s1.close()
            s2.close()
            s3.close()

            data.start_time = time.time()

            self.lidar.start()
            self.execute.start()

            # main thread proverava sve vreme da li je kraj meca
            while True:
                if not data.running.is_set():
                    break

                data.elapsed_time = time.time() - data.start_time

                if data.elapsed_time > 101:

                    # zaustavlja sve ako je vreme meca isteklo pre nego sto je zavrsio sve korake
                    data.running.clear()
                    break
                elif data.elapsed_time > data.time_strategy_type and not data.end_of_match:
                    # prekida izvrsavanje strategije ako je doslo vreme da se vraca u bazu
                    data.TIMEOUT_FOR_LAST_STEPS = True

                time.sleep(.1)

            if ((data.x_current > 1450) and (-550 < data.y_current < 550)) or ((650 < data.x_current < 1350) and ((-3000 < data.y_current < -2400) or (2400 < data.y_current < 3000))):
                data.points += 10
            self.stop()

            return

        except (KeyboardInterrupt, SystemExit):
            self.stop()

    def stop(self):
        data.elapsed_time = time.time() - data.start_time

        data.running.clear()

        custom_print('\n')
        custom_print('*'*100)
        custom_print(f"TRAJANJE MECA JE::: {data.elapsed_time}")
        custom_print(f"POENI::: {data.points}")
        custom_print('*'*100)
        custom_print('\n')

        try:
            self.execute.moving.position.maxon_left.rotate_with_rpm(0)
            self.execute.moving.position.maxon_right.rotate_with_rpm(0)

            time.sleep(1)

            self.execute.moving.position.maxon_left.disable_driver()
            self.execute.moving.position.maxon_right.disable_driver()
            time.sleep(0.1)
        except Exception as e:
            custom_print(f"ESP ERROR: {str(e)}")
        try:
            custom_print("Gasim lidar")
            # self.lidar.stop()
            # if self.lidar.lidar_thread.is_alive():
            #    self.lidar.lidar_thread.join()
        except Exception as e:
            custom_print(f"LIDAR ERROR: str{e}")


if __name__ == "__main__":
    main = Main()
    main.start()
