import sys
import threading
import socket
import data


class CAM_COMM:

    def __init__(self):
        host = '0.0.0.0'
        port = 12345

        # print("aaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAa")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(1)

        self.com_res = ''

        self.cam_arr = [1, 1, 1, 1, 1, 1]

    def receive(self):
        conn, addr = self.s.accept()
        while True:

            self.com_res = ''
            while self.com_res == '':
                # print("OVDE sam 1")
                # print("OVDE sam 1.5")
                self.com_res = conn.recv(1024).decode()
                # print("OVDE sam 2")

                for i in range(6):
                    self.cam_arr[i] = int(self.com_res[i])
                # print("OVDE sam 3")
                # print(self.cam_arr)
                data.cam_arr = self.cam_arr

    def start(self):
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()


if __name__ == "__main__":
    sys.path.append("..")

    comm = CAM_COMM()
    comm.receive()
