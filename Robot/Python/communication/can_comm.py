import can
import subprocess
import data
import threading
import math
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
        while True:
            msg = self.can0.recv(10.0)

            if len(msg.data) == 4:
                enc1 = int(msg.data[1] << 8 | msg.data[0])
                enc2 = int(msg.data[3] << 8 | msg.data[2])

                if enc1 > 10000:
                    enc1 -= 65535

                enc1 *= -1

                if enc2 > 10000:
                    enc2 -= 65535

                data.enc_left = enc1
                data.enc_right = enc2

                data.sum_encoder_left += enc1
                data.sum_encoder_right += enc2

                self.pos.calculate_position()

            if msg is None:
                print('Timeout occurred, no message.')

    def start(self):
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()


if __name__ == "__main__":
    comm = CAN_COMM()
    comm.receive()
