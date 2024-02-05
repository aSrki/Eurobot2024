from math import atan, degrees


class Path:
    TOLERANCE = 0

    # trenutne kordinate x, y, f ugao
    def __init__(self, x, y, f):  # TODO moguca greske zato sto se trenutne greske salju pri stvaranju objekta
        self.x = x
        self.y = y
        self.f = f

    # saljemo zeljene kordinate
    def distance(self, x, y):
        z = ((self.x - x) ** 2 + (self.y - y) ** 2) ** (1 / 2)
        return z

    # saljemo  zeljene kordinate
    def rotate(self, wanted_x, wanted_y):

        # u slucaju da je delta x ==0 da ne bude error u racunu
        if wanted_x - self.x == 0:
            wanted_x += 0.001

        # razlika zeljenih i trenutnih kordinata
        delta_x = wanted_x - self.x
        delta_y = wanted_y - self.y

        # RACUN UGLA
        f = degrees(atan(abs(delta_y) / abs(delta_x)))
        # print("ugao f je = ",f)

        # PRVI kvadrant
        if delta_x > self.TOLERANCE and delta_y > self.TOLERANCE:  # Uslovi gledaju stanje zeljene kordinate,ne njegovo
            f = 90 - f
            print('PRVI kvadrant', f)

        # DRUGI kvadrant
        elif delta_x < self.TOLERANCE and delta_y > self.TOLERANCE:
            f = f - 90
            print('DRUGI kvadrant', f)

        # TRECI kvadrant
        elif delta_x < self.TOLERANCE and delta_y < self.TOLERANCE:
            f = 270 - f
            print('TRECI kvadrant', f)

        # CETVRTI kvadrant
        elif delta_x > self.TOLERANCE and delta_y < self.TOLERANCE:
            f = f + 90
            print('CETVRTI kvadrant', f)

        elif delta_y >= 0:
            f = 0
            print('ugao koji je izracunao  = ', f)
        else:
            f = 180
            print('ugao koji je izracunao  = ', f)

        f *= -1

        # filter da ugao rotacije bude manji od 180

        # PRVI kvadrant

        # if 90 >= f > 0:  # Uslovi gledaju stanje zeljene kordinate,ne njegovo
        #     f = 90 - f
        #     print('PRVI kvadrant', f)
        #
        # # DRUGI kvadrant
        # elif 180 >= f > 90:
        #     f = f - 90
        #     print('DRUGI kvadrant', f)
        #
        # # TRECI kvadrant
        # elif 270 >= f > 180:
        #     f = 270 - f
        #     print('TRECI kvadrant', f)
        #
        # # CETVRTI kvadrant
        # else:
        #     f = f + 90
        #     print('CETVRTI kvadrant', f)

        if f > 180:
            f -= 360
        elif f < -180:
            f += 360

        return f

# p = Path(3,4,0)
# distance = p.go(4,3)
# print('Distanca je: {}'.format(distance))
# rotation = p.rotate(4,3)
# print('Rotacija: {:.2f}'.format(rotation))
