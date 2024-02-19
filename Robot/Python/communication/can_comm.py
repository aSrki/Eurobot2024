import can
import subprocess
import sys
import threading


if __name__ == "__main__":
    sys.path.append("..")

import data
from regulation_controller.position import Position


class CAN_COMM:
    def __init__(self):
        subprocess.run(["sudo", "/sbin/ip", "link", "set", "can0",
                       "up", "type", "can", "bitrate", "500000"])
        subprocess.run(["sudo", "ip", "link", "set", "can0",
                       "type", "can", "restart-ms", "500"])
        self.can0 = can.interface.Bus(
            channel='can0', bustype='socketcan')  # socketcan_native
        data.running.set()
        self.thread = None

        self.pos = Position()

    def receive(self):
        first_time = True
        enc1_old = 0
        enc2_old = 0
        while True:
            msg = self.can0.recv(10.0)
            if len(msg.data) == 4:
                enc1_new = int(msg.data[1] << 8 | msg.data[0])
                enc2_new = int(msg.data[3] << 8 | msg.data[2])

                if first_time:
                    enc1_old = enc1_new
                    enc2_old = enc2_new
                    first_time = False

                enc1 = enc1_new - enc1_old
                enc2 = enc2_new - enc2_old

                if enc1 > 32767:
                    enc1 -= 65535

                elif enc1 < -32767:
                    enc1 += 65535

                if enc2 > 32767:
                    enc2 -= 65535

                elif enc2 < -32767:
                    enc2 += 65535

                enc1_old = enc1_new
                enc2_old = enc2_new
                # if enc1 > 10000:
                #     enc1 -= 65536

                enc1 *= -data.OdometryData.faktor_razlike

                # if enc2 > 10000:
                #     enc2 -= 65536

                # data.enc_left = enc1
                # data.enc_right = enc2

                data.sum_encoder_left += enc1
                data.sum_encoder_right += enc2

                self.pos.calculate_position()

            if msg is None:
                print('Timeout occurred, no message.')

    def start(self):
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()


if __name__ == "__main__":
    sys.path.append("..")

    comm = CAN_COMM()
    comm.receive()
