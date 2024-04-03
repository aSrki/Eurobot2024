from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QTransform
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import threading
import time
import sys
import os
import subprocess
sys.path.append("/home/robot/Eurobot2024/Robot/Python")
from main import Main
import data
from servo.servo_moving import Servo_Moving
import socket

class Payload():
    def __init__(self):
        self.color = None
        self.type_of_strategy = None
        self.table = None

gamePayload = Payload()
count_time = 0

class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen1.ui", self)

        self.showMaximized()

        self.button_init_yellow.clicked.connect(self.on_click_init_yellow)
        self.button_init_yellow.setStyleSheet(
            "background-color: transparent;")
        
        self.button_init_blue.clicked.connect(self.on_click_init_blue)
        self.button_init_blue.setStyleSheet(
            "background-color: transparent;")
        
        self.button_sto2.clicked.connect(self.on_click_sto2)
        self.button_sto2.setStyleSheet(
            "background-color: transparent;")

    def on_click_init_yellow(self):
        Servo_Moving().init_yellow()

    def on_click_init_blue(self):
        Servo_Moving().init_blue()

    def on_click_sto2(self):
        self.gotoScreen2()

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()


class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen2.ui", self)

        self.button_zuta.clicked.connect(self.on_click_zuta)
        self.button_plava.clicked.connect(self.on_click_plava)
        self.button_back.clicked.connect(self.gotoScreen1)

        self.button_zuta.setStyleSheet(
            "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
        self.button_plava.setStyleSheet(
            "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")

    def on_click_zuta(self):
        gamePayload.color = 'yellow'
        # gamePayload.printPayload()
        self.gotoScreen5()

    def on_click_plava(self):
        gamePayload.color = 'blue'
        # gamePayload.printPayload()
        self.gotoScreen5()

    def gotoScreen1(self):
        screen1 = Screen1()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

    def gotoScreen5(self):
        screen5 = Screen5()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()


class Screen3(QDialog):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen3.ui", self)

        self.button_back_3.clicked.connect(self.gotoScreen2)
        self.button_glhf.clicked.connect(self.glhf)
        self.label.setText("Izabrana boja tanjira: " + str(gamePayload.color) + "\n"
                           "Da li si siguran da zelis da nastavis?")
        
        print(f"COLOR: " + str(gamePayload.color) + "\n TABLE: " + str(gamePayload.table)  + "\n STRATEGY: " + str(gamePayload.type_of_strategy))
        
        self.sima_1_label.setStyleSheet("background-color: red;")
        self.sima_2_label.setStyleSheet("background-color: red;")
        self.sima_3_label.setStyleSheet("background-color: red;")   
    
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_simas)
        self.timer.start(700)

    def update_simas(self):

        res1 = os.popen('ping -c 1 -W 0.2 192.168.1.143').read()
        res2 = os.popen('ping -c 1 -W 0.2 192.168.1.212').read()
        res3 = os.popen('ping -c 1 -W 0.2 192.168.1.192').read()

        if "1 received" in res1:
            self.sima_1_label.setStyleSheet("background-color: green;")        
        elif "0 received" in res1:
            self.sima_1_label.setStyleSheet("background-color: red;")        

        if "1 received" in res2:
            self.sima_2_label.setStyleSheet("background-color: green;")        
        elif "0 received" in res2:
            self.sima_2_label.setStyleSheet("background-color: red;") 

        if "1 received" in res3:
            self.sima_3_label.setStyleSheet("background-color: green;")        
        elif "0 received" in res3:
            self.sima_3_label.setStyleSheet("background-color: red;") 

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.button_glhf.hide()
        self.close()

    def glhf(self):
        # data.color = gamePayload.color
        screen4 = Screen4()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()


class Screen4(QDialog):
    def __init__(self):

        super(Screen4, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen4.ui", self)
        data.color = gamePayload.color
        data.type_of_strategy = gamePayload.type_of_strategy
        data.table = gamePayload.table
        self.label.setText("Points: " + str(0) + "\nTime: " +
                           str(data.elapsed_time) + "s")
        self.kill_all_button.clicked.connect(self.kill_all)
        self.kill_all_button.setStyleSheet(
            "background-color: red; border: none;")

        main = Main()
        self.main_thread = threading.Thread(target=main.start)
        self.main_thread.start()

        self.sima_1_label_screen4.setStyleSheet("background-color: red;")
        self.sima_2_label_screen4.setStyleSheet("background-color: red;")
        self.sima_3_label_screen4.setStyleSheet("background-color: red;")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

        self.sima_timer = QtCore.QTimer()
        self.sima_timer.timeout.connect(self.update_simas_screen4)
        self.sima_timer.start(700)

    def update_simas_screen4(self):

        res1 = os.popen('ping -c 1 -W 0.2 192.168.1.143').read()
        res2 = os.popen('ping -c 1 -W 0.2 192.168.1.212').read()
        res3 = os.popen('ping -c 1 -W 0.2 192.168.1.192').read()

        if "1 received" in res1:
            self.sima_1_label_screen4.setStyleSheet("background-color: green;")        
        elif "0 received" in res1:
            self.sima_1_label_screen4.setStyleSheet("background-color: red;")        

        if "1 received" in res2:
            self.sima_2_label_screen4.setStyleSheet("background-color: green;")        
        elif "0 received" in res2:
            self.sima_2_label_screen4.setStyleSheet("background-color: red;") 

        if "1 received" in res3:
            self.sima_3_label_screen4.setStyleSheet("background-color: green;")        
        elif "0 received" in res3:
            self.sima_3_label_screen4.setStyleSheet("background-color: red;") 

    def update_label(self):
        if data.cinc != 1:
            ispis = str("WAITING FOR CINC \n" + "Strategy:" + str(data.color))
        else:
            time_el = data.elapsed_time
            if time_el > 100:
                time_el = 100
            ispis = str("Points: " + str(data.points) + "\n" + "TIME : " + str(int(time_el)))
        self.label.setText(ispis)

    def kill_all(self):
        data.running.clear()
        self.main_thread.join()
        print("KILLING MAIN THREAD")
        # time.sleep(0.2)
        # widget.setCurrentIndex(widget.currentIndex() + 1)
        # self.close()

class Screen5(QDialog):
    def __init__(self):
        super(Screen5, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen5.ui", self)

        self.button_agressive.clicked.connect(self.on_click_agressive)
        self.button_passive.clicked.connect(self.on_click_passive)
        self.button_nazad.clicked.connect(self.on_click_nazad)

        if gamePayload.color == "yellow":
            self.button_agressive.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
            self.button_passive.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
            
        else:
            self.button_agressive.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")
            self.button_passive.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")


    def on_click_agressive(self):
        gamePayload.type_of_strategy = 'agressive'
        self.gotoScreen6()

    def on_click_passive(self):
        gamePayload.type_of_strategy = 'passive'
        self.gotoScreen6()

    def on_click_nazad(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

    def gotoScreen6(self):
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

class Screen6(QDialog):
    def __init__(self):
        super(Screen6, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen6.ui", self)

        self.button_sto_uski.clicked.connect(self.on_click_sto_uski)
        self.button_sto_siroki.clicked.connect(self.on_click_sto_siroki)
        self.button_back.clicked.connect(self.gotoScreen5)

        if gamePayload.color == "yellow":
            self.button_sto_uski.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
            self.button_sto_siroki.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
            
        else:
            self.button_sto_uski.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")
            self.button_sto_siroki.setStyleSheet(
                "background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")

      
    def on_click_sto_uski(self):
        gamePayload.table = 'uski'
        self.gotoScreen3()

    def on_click_sto_siroki(self):
        gamePayload.table = 'siroki'
        self.gotoScreen3()

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

    def gotoScreen5(self):
        screen5 = Screen5()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

if __name__ == '__main__':
    # import data
    # from main import Main

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()
    widget.resize(719, 480)

    screen1 = Screen1()

    widget.addWidget(screen1)
    widget.showMaximized()

    sys.exit(app.exec_())
