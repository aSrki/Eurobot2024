from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QTransform
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import threading
import time
import sys
import os, subprocess
sys.path.append("/home/robot/Eurobot2024/Robot/Python")
from main import Main
import data
class Payload():
    def __init__(self):
        self.color = None

gamePayload = Payload()
count_time = 0


class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        loadUi("/home/robot/Eurobot2024/Robot/Python/run/screen1.ui", self)

        self.showMaximized()

        self.button_sto1.clicked.connect(self.on_click_sto1)
        self.button_sto1.setStyleSheet(
            "background-color: transparent; border: none;")
        self.button_sto2.clicked.connect(self.on_click_sto2)
        self.button_sto2.setStyleSheet(
            "background-color: transparent; border: none;")
       

    def on_click_sto1(self):
        self.gotoScreen1()

    
    def on_click_sto2(self):
        # gamePayload.printPayload()
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
        
        self.button_zuta.setStyleSheet("background-image : url(/home/robot/Eurobot2024/Robot/Python/run/zuto.png);")
        self.button_plava.setStyleSheet("background-image : url(/home/robot/Eurobot2024/Robot/Python/run/plavo.png);")

    def on_click_zuta(self):
        gamePayload.color = 'yellow'
        # gamePayload.printPayload()
        self.gotoScreen3()

    def on_click_plava(self):
        gamePayload.color = 'blue'
        # gamePayload.printPayload()
        self.gotoScreen3()

    def gotoScreen1(self):
        screen1 = Screen1()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
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
        self.label.setText("Points: " + str(0) + "\nTime: " + str(data.elapsed_time) + "s")
        self.kill_all_button.clicked.connect(self.kill_all)
        self.kill_all_button.setStyleSheet("background-color: red; border: none;")


        main = Main()
        self.main_thread = threading.Thread(target=main.start)
        self.main_thread.start()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)
    

    def update_label(self):
        if data.cinc != 1:
            ispis = str("WAITING FOR CINC \n" + "Strategy:" + str(data.color))
        else:
            ispis = str("Points: " + str(data.points))
        self.label.setText(ispis)

    def kill_all(self):
        data.running.clear()
        self.main_thread.join()
        print("KILLING MAIN THREAD")
        # time.sleep(0.2)
        # widget.setCurrentIndex(widget.currentIndex() + 1)
        # self.close()

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
