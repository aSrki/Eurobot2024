import can
import subprocess
import sys
import threading
import struct

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

    # stari stm kod
    # def receive(self):
    #     first_time = True
    #     enc1_old = 0
    #     enc2_old = 0

    #     while True:
    #         msg = self.can0.recv(10.0)
    #         if len(msg.data) == 4:
    #             enc1_new = int(msg.data[1] << 8 | msg.data[0])
    #             enc2_new = int(msg.data[3] << 8 | msg.data[2])

    #             if first_time:
    #                 enc1_old = enc1_new
    #                 enc2_old = enc2_new
    #                 first_time = False

    #             enc1 = enc1_new - enc1_old
    #             enc2 = enc2_new - enc2_old

    #             if enc1 > 32767:
    #                 enc1 -= 65535

    #             elif enc1 < -32767:
    #                 enc1 += 65535

    #             if enc2 > 32767:
    #                 enc2 -= 65535

    #             elif enc2 < -32767:
    #                 enc2 += 65535

    #             enc1_old = enc1_new
    #             enc2_old = enc2_new
    #             # if enc1 > 10000:
    #             #     enc1 -= 65536

    #             enc1 *= -(1.0/data.OdometryData.faktor_razlike)

    #             # if enc2 > 10000:
    #             #     enc2 -= 65536

    #             # data.enc_left = enc1
    #             # data.enc_right = enc2

    #             data.sum_encoder_left += enc1
    #             data.sum_encoder_right += enc2

    #             # self.pos.calculate_position()

    #         if msg is None:
    #             print('Timeout occurred, no message.')

    # nov stm kod
    def receive(self):

        while True:
            # print("PRE RECV")
            msg = self.can0.recv(10.0)
            # print("POSLE RECV")
            # print(len(msg))
            if msg is not None:
                if msg.arbitration_id == 0x69: # handshake poruka (ID 69, 0x6969)
                    print("STM je startovan")
                    data.STM_UP = True
                #print("MSG IS NOT NONE")
                #print(f"MSG SIZE {len(msg.data)}")
                # if len(msg.data) == 12:
                if len(msg.data) == 8:
                    if msg.arbitration_id == 0x100:
                        stm_x, stm_y = struct.unpack('<ff', bytes(msg.data))
                        data.x_current = data.x_start + stm_x
                        data.y_current = data.y_start + stm_y
                        # print(f"X coord : {data.x_current}")
                        # print(f"Y coord : {data.y_current}")
                    if msg.arbitration_id == 0x101:
                        # d - predjeni put u instanci vremena(trenutni) -> treba za position_regulation.regulation
                        stm_f, data.d_current= struct.unpack('<ff', bytes(msg.data))
                        data.f_current = data.f_start + stm_f
                        data.d_ukupno += data.d_current
            

                        # print(f"F angle : {data.f_current}")
                        # print(f"d - put u instanci vremena : {data.d_current}")
            if msg is None:
                print('Timeout occurred, no message.')

    def start(self):
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()


if __name__ == "__main__":
    sys.path.append("..")

    comm = CAN_COMM()
    comm.start()
