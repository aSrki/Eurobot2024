import sys
import time
if __name__ == "__main__":
    sys.path.append("/home/robot/robot")

import threading
import time
import data
import math


class Position:

    def __init__(self):
        self.cur_encoder_right = 0
        self.cur_encoder_left = 0

        self.delay = 0.002  # svakih 2 milisekundi

    def start(self):
        #     thread = threading.Thread(target=self.run)
        #     thread.start()
        print("Position started")

    # def run(self):
    #     print("Position running")
    #     while data.running.is_set():
    #         self.calculate_position()
    #         time.sleep(self.delay)

    def calculate_position(self):
        # Trenutne kordinate
        x = data.x_current
        y = data.y_current
        f = data.f_current

        # Suma inkrimenta na levom i desnom enkoderu se ucitavaju

        # encoder_left = data.enc_left
        # encoder_right = data.enc_right

        # print(f"POSITION:   INC1: {data.enc_left} INC2: {data.enc_right}")

        curr_sum_enc_left = data.sum_encoder_left
        encoder_left = curr_sum_enc_left - data.prev_enc_sum_left

        curr_sum_enc_right = data.sum_encoder_right
        encoder_right = curr_sum_enc_right - data.prev_enc_sum_right

        data.prev_enc_sum_left = curr_sum_enc_left
        data.prev_enc_sum_right = curr_sum_enc_right

        print(
            f"POSITION:   ENC1: {encoder_left} ENC2: {encoder_right}")

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

        if data.debug:
            self.print_position()
        return d

    def print_position(self):
        # print('X osa:\t\t\t{:.0f} mm'.format(data.x_current))
        # print('Y osa:\t\t\t{:.0f} mm'.format(data.y_current))
        # print('UGAO osa:\t\t{:.0f}'.format(data.f_current), ' \n')
        return
        # print('d duzina:\t\t\t{:.0f}'.format(d))


if __name__ == "__main__":
    pos = Position()
    pos.start()
