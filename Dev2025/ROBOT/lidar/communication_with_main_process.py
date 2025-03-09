import threading
import os
import global_var
import sys
import time


class Communication:
    # !!!!!!! WRITES TO MAIN DIRECTLY FROM RP-LIDAR !!!!!!!!!!
    def __init__(self):
        self.info = ""
        self.debug_comm = False

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        print("**Communication with main initalize**")

        while True:

            is_read, info = self.read_from_main()
            self.info = info

            if "END" in info:
                global_var.RUN_THREADS = False

            time.sleep(.1)

    def read_from_main(self):
        if not os.isatty(int(sys.argv[1])):
            read_pipe = os.read(int(sys.argv[1]), 1024)
            read_pipe = read_pipe.decode()

            if read_pipe:
                return True, read_pipe
        return False, " "

    # WRITES TO MAIN
    def write_to_main(self, msg):
        # print('sending: '+ msg)
        # print(sys.argv)
        os.write(int(sys.argv[2]), (str(msg).encode()))
