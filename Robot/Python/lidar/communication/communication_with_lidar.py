import threading
import os
import sys
import time
import data


class Communication_with_lidar:
    inc = 0
    # !!!!!!! WRITES TO LIDAR DIRECTLY FROM REGULATION !!!!!!!!!!
    def __init__(self):
        self.info = ""
        self.lidar_obstacle_detected = False

    def start(self):
        # pass
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        print('\n\n*******LIDAR COMMUNICATION************\n\n')
        data.log.add_info_message("*******LIDAR COMMUNICATION************")

        while not data.STOP_REGULATION_THREAD:
            self.lidar_obstacle_detection()
            if self.inc % 25 == 0:
                print(f'lidar sensors f{data.frontLidarDetection} , b{data.backLidarDetection} '
                      f' , {data.sensors}')
                data.log.add_info_message(f'lidar sensors f{data.frontLidarDetection} , b{data.backLidarDetection} '
                      f' , {data.sensors}')

            self.inc += 1
            time.sleep(.07)

    def lidar_obstacle_detection(self):
        """ vraca da li je detektovao """
        # print("Pocinje",data.fd_read1)

        if not os.isatty(data.fd_read1) and not  data.STOP_REGULATION_THREAD:
            # print("pokusava")

            read_pipe = os.read(data.fd_read1, 1024)
            read_pipe = read_pipe.decode()
            # print('recived: '+ read_pipe)
            recived_data = read_pipe.split(';')
            f = False
            b= False
            for d in recived_data:
                if len(d):
                    if d[0]=='f':
                        f = d[1:] == "True"
                    elif d[0]=='b':
                        b = d[1:] == "True"

            if data.sensors == data.Sensors.FRONT_ON:
                data.frontLidarDetection = f
                data.backLidarDetection = False
            elif data.sensors == data.Sensors.BACK_ON:
                data.frontLidarDetection = False
                data.backLidarDetection = b
            elif data.sensors == data.Sensors.ALL_ON:
                data.frontLidarDetection = f
                data.backLidarDetection = b
            else:
                data.frontLidarDetection = False
                data.backLidarDetection = False


    def get_lidar_obstacle_detected(self) -> bool:
        # return False
        return self.lidar_obstacle_detected

    def set_lidar_obstacle_detected(self, lidar_obstacle_detected):
        self.lidar_obstacle_detected = lidar_obstacle_detected

    def get_info(self):
        return self.info  # distance, angle

    def write(self,msg : str):
        # print("SENDING TO LIDAR : ",msg,data.fd_write2)
        os.write(data.fd_write2, (str(msg).encode()))
