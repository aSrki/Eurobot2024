import can
import subprocess
import sys
import threading

import struct


if __name__ == "__main__":
    sys.path.append("..")

import data


class CAN_COMM:
    def __init__(self):
        self.can0 = can.interface.Bus(
            channel='can0', interface='socketcan')  # socketcan_native
        data.running.set()
        self.thread = None
        self.DEBUG = False 
        self.d_ukupno = 0

# na stmu 
# TxHeader.DLC = 4; -> TxHeader.DLC = 8;
# TxMailBox uint32 -> uint64
# Ubaceni ID poruka1 i ID poruka2
    def receive(self):

        while True:
            # print("PRE RECV")
            msg = self.can0.recv(10.0)
            # print("POSLE RECV")
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
                        #print(f"X coord : {data.x_current}")
                        #print(f"Y coord : {data.y_current}")
                    if msg.arbitration_id == 0x101:
                        # d - predjeni put u instanci vremena(trenutni) -> treba za position_regulation.regulation
                        stm_f, data.d_current= struct.unpack('<ff', bytes(msg.data))
                        data.f_current = data.f_start + stm_f
                        data.d_ukupno += data.d_current
            

                        #print(f"F angle : {data.f_current}")
                        # print(f"d - put u instanci vremena : {data.d_current}")
            if msg is None:
                print('Timeout occurred, no message.')

    def start(self):
        print("CAN COMM - START THREAD")
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()


if __name__ == "__main__":
    # sys.path.append("..")
    print("KRENUO")
    comm = CAN_COMM()
    comm.start()
