import sys
import time
if __name__ == "__main__":
    sys.path.append("/home/mali/robot")

import threading
import time
import data
import math
from communication.driver_communication import DriverCommunication

class Position:

    def __init__(self, maxon:DriverCommunication):
        self.cur_encoder_right = 0
        self.cur_encoder_left = 0
        self.maxon = maxon

        self.delay = 0.0005  # svakih .5 milisekundi

    def start(self):
        # data.running.set()
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        while data.running.is_set():
            self.calculate_position()
            time.sleep(self.delay)

        return

    def update_inc(self):

        data.sum_encoder_left, data.sum_encoder_right = self.maxon.get_encoders_left_right()
        # print('\n\nLevi enkoder:\t{}'.format(data.sum_encoder_left ))
        # print('Desni enkoder:\t{}'.format(data.sum_encoder_right))

    def calculate_position(self):
        self.update_inc()

        # Trenutne kordinate
        x = data.x_current
        y = data.y_current
        f = data.f_current

        # Suma inkrimenta na levom i desnom enkoderu se ucitavaju

        sum_left = data.sum_encoder_left
        sum_right = data.sum_encoder_right

        # Trenutna inkrementacija
        encoder_right = self.cur_encoder_right
        encoder_left = self.cur_encoder_left

        encoder_left = sum_left - encoder_left
        encoder_right = sum_right - encoder_right

        self.cur_encoder_right = sum_right
        self.cur_encoder_left = sum_left

        # predjeni put u instanci vremena(trenutni)
        d = ((encoder_left + encoder_right) / 2) * \
            data.OdometryData.inc_mm  # inc_mm

        # ugao u instanci vremena
        g = -((encoder_left - encoder_right) / 2) * data.OdometryData.inc_deg

        # ukupan ugao
        f += g

        rad = math.radians(90 - f)

        # promena(diferencijal) x i y kordinate
        dx = -d * math.cos(rad)
        dy = d * math.sin(rad)

        # Trenutne kordinate posle promene
        x += dx
        y += dy

        # Trenutni ugao racuna
        if f < 0:
            f = abs(f) % 360
            f = -f

        else:
            f = f % 360

        # Nova trenutna pozicija
        data.x_current = x
        data.y_current = y
        data.f_current = f
        #self.print_position()
        return d

    def print_position(self):
        print('\n\n\nLevi enkoder:\t{}'.format(data.sum_encoder_left))
        print('Desni enkoder:\t{}'.format(data.sum_encoder_right))
        # print('Levi trenutna vrednost enkoder:\t{}'.format(encoder_left))
        # print('Desni trenutna vrednost enkoder:\t{}'.format(encoder_right))
        print('X osa:\t\t\t{:.0f} mm'.format(data.x_current))
        print('Y osa:\t\t\t{:.0f} mm'.format(data.y_current))
        print('UGAO osa:\t\t{:.0f}'.format(data.f_current), ' \n\n\n')
        # # print('d duzina:\t\t\t{:.0f}'.format(d))


if __name__ == "__main__":
    pos = Position()
    pos.start()
