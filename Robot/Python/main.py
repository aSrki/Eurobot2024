import data
from strategies.choose_strategy import choose_strategy
import time
from sensors import SensorsDetection
import socket
#from lidar.lidar_detection import LidarDetection

DEBUG = True

# PROMENITI OVAJ IP NA SIMIN
# PROMENITI U LINIJI 69, heh, BOJU POCETNU
# za menjanje stratrgije na simi i prebacivanje putanja je /home/sima1/sima/Dynamixel-XL430-W250
# fajl sa koordinatama je strategy.py 
sima1_IP = '192.168.0.24'


def custom_print(msg):
    if DEBUG:
        print(msg)
    #data.log.add_info_message(str(msg))


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

            from execute import Execute

            # pokretanje execute threada
            self.execute = Execute()
            #self.lidar = LidarDetection()

            #self.basket_comm = BasketCommunication()

            # while data.cinc == 0:
            #     print("Waiting for CINC")
            #     continue

            host = sima1_IP 
            port = 12345

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((host, port))

            data = "blue"
            s.sendall(data.encode())

            s.close()

            data.start_time = time.time()

            #self.lidar.start()
            self.execute.start()

            # main thread proverava sve vreme da li je kraj meca
            while True:
                if not data.running.is_set():
                    break

                data.elapsed_time = time.time() - data.start_time

                if data.elapsed_time > 95 and self.first_basket:
                    #self.basket_comm.start()
                    #self.basket_comm.get_basket_points()
                    self.first_basket = False

                # elif data.elapsed_time > 99.5:
                #     if data.basket_points != None:
                #         data.points += data.basket_points
                #     else:
                #         data.points += data.cherry_points
                #     # zaustavlja sve ako je vreme meca isteklo pre nego sto je zavrsio sve korake
                #     data.running.clear()
                #     continue
                elif data.elapsed_time > data.time_strategy_type and not data.end_of_match:
                    # prekida izvrsavanje strategije ako je doslo vreme da se vraca u bazu
                    data.TIMEOUT_FOR_LAST_STEPS = True

                time.sleep(.1)

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
            #self.lidar.stop()
            #if self.lidar.lidar_thread.is_alive():
            #    self.lidar.lidar_thread.join()
        except Exception as e:
            custom_print(f"LIDAR ERROR: str{e}")


if __name__ == "__main__":
    main = Main()
    main.start()
