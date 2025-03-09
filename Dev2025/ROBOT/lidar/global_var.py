from enum import Enum
from math import cos, sin, pi, floor, sqrt, degrees, atan
import sys

RUN_THREADS = True
UPPER_BOUNDERY = 2800
LOWER_BOUNDERY = 200
LIDAR_ANGLE = 360
path = [0, 0]  # [0]-ugao , [1]-distanca
main_path = [0, 0]  # [0]-distanca ,[1]-ugao



display_lidar = False

scanned_data = [0] * 360

class RobotDimenssions:
    width = 300
    length = 200

class StoppingArea:
    width = 300
    length = 390

class Shape(Enum):
    CIRCLE = 2
    LINE = 1
    RECTANGLE = 3


class SearchDirection(Enum):  # za rekurziju ne pravac skeniranje
    CLOCKWISE = 1
    ANTICLOCKWISE = 2


def radianss(angle):
    return angle * pi / 180.000


def get_x_y(angle, distance):
    rad = radianss(angle)
    x = distance * cos(rad)
    y = distance * sin(rad)

    return x, y


def absolute_diference(x, y):
    return abs(x - y)


def get_smaller_angle(b1,b2):
    b1 = abs(b1)
    b2 = abs(b2)

    d1 = absolute_diference(path[0], b1)
    d2 = absolute_diference(b2, path[0])

    if d1 > 180:
        d1 -=360
    if d2 > 180:
        d2 -=360

    d1 = abs(d1)
    d2 = abs(d2)
    print(f"\n\n******************  {str(d1)}   ,   {str(d2)}   ****************\n\n",b1,b2,path[0])
    if d1 < d2:
        print("d1")
        return True
    print("d2")
    return False

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, C


def point_line_distance(p1, p2, x, y, k, n):  # p1,p2 koordinate tacaka kroz koje linija prolazi, x,y-koordinate tacke
    yi = (k * x + n)

    if (yi > y and yi > 0) or (yi < y and yi < 0):
        A, B, C = line(p1, p2)
        d = (abs(A * x + B * y + C)) / sqrt((A ** 2 + B ** 2) + .00000001)
        # print("p1 {} ".format(p1[0],p1[1]))
        # print("p2 {} ".format(p2[0], p2[1]))
        # print("x,y {} ".format(x, y))
        # print("racuna = ",d)
        return d
    return 0


def line_line_intersection(xp, xq, yp, yq, x0, y0, r):
    point = Point(x0, y0)
    circle = point.buffer(r).boundary
    line = LineString([(xp, yp), (xq, yq)])
    i = circle.intersection(line)


def path_rectangle(path):
    ROBOT_WIDTH_temp =365
    rad = radianss(path[0] + 90)
    x, y = get_x_y(path[0], path[1])

    x1 = ROBOT_WIDTH_temp * cos(rad) / 2 / 2
    y1 = ROBOT_WIDTH_temp * sin(rad) / 2 / 2
    x2 = - ROBOT_WIDTH_temp * cos(rad) / 2 / 2
    y2 = - ROBOT_WIDTH_temp * sin(rad) / 2 / 2
    x3 = x + ROBOT_WIDTH_temp * cos(rad) / 2
    y3 = y + ROBOT_WIDTH_temp * sin(rad) / 2
    x4 = x - ROBOT_WIDTH_temp * cos(rad) / 2
    y4 = y - ROBOT_WIDTH_temp * sin(rad) / 2

    return 0, x1, y1, x2, y2, x3, y3, x4, y4


def create_coordinates(angle, distance):
    rec_path = path_rectangle([angle, distance])

    return ([
        (rec_path[1], rec_path[2]),
        (rec_path[3], rec_path[4]),
        (rec_path[7], rec_path[8]),
        (rec_path[5], rec_path[6])

    ])


def placem():
    angle_in_radians = atan(k)
    angle = int(degrees(angle_in_radians) - 90)

    if yp > 0:
        kvadrant = 1
    else:
        kvadrant = -1
    xp2 = xp + d_max * cos(radianss(angle)) * kvadrant
    yp2 = yp + d_max * sin(radianss(angle)) * kvadrant

    if yq > 0:
        kvadrant = 1
    else:
        kvadrant = -1
    xq2 = xq + d_max * cos(radianss(angle)) * kvadrant
    yq2 = yq + d_max * sin(radianss(angle)) * kvadrant
    arr = [Shape.RECTANGLE, xp, yp, xq, yq, xp2, yp2, xq2, yq2, start_angle, end_angle]
    obstacles.append(arr)
    # print("pravugaonik\nbr.", i, " dmax = ", d_max, "\n")
