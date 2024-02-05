import numpy as np
import sympy as sym
from sympy import Matrix, cos, sin
import time


class TransformMatrix:

    def __init__(self, offset):
        self.m = offset

        self.transform_matrix = self.get_matrix()

    def get_matrix(self):
        alpha = sym.Symbol("alpha")
        theta = sym.Symbol("theta")
        d = sym.Symbol("d")
        m = sym.Symbol("m")
        x = sym.Symbol("x")
        y = sym.Symbol("y")

        # Rotacija za 90 oko z-ose
        Hlr_z_rot = Matrix([  
            [ 0, -1, 0, 0],
            [1, 0, 0, 0],
            [ 0, 0, 1, 0],
            [ 0, 0, 0, 1] 
        ])

        # Rotacija za 180 oko y-ose
        Hlr_y_rot = Matrix([  
            [-1, 0,  0, 0],
            [ 0, 1,  0, 0],
            [ 0, 0, -1, 0],
            [ 0, 0,  0, 1] 
        ])

        # Translacija za m po y-osi
        Hlr_y_trans = Matrix([
            [1, 0, 0,  0],
            [0, 1, 0,  m],
            [0, 0, 1,  0],
            [0, 0, 0,  1]
        ])

        Hrs_rot = Matrix([
            [cos(theta), -sin(theta), 0, 0],
            [sin(theta),  cos(theta), 0, 0],
            [          0,            0, 1, 0],
            [          0,            0, 0, 1]
        ])

        Hrs_trans = Matrix([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1,  0],
            [0, 0, 0,  1]
        ])

        H = Hrs_trans * Hrs_rot * Hlr_y_trans * Hlr_y_rot * Hlr_z_rot

        Pl = Matrix([
            [d*cos(alpha)],
            [d*sin(alpha)],
            [0],
            [1]
        ])

        Ps = H*Pl
        Ps = sym.simplify(Ps)
        print(Ps)
        return Ps

    def lidar2table(self, x_cur, y_cur, distance, lidar_angle, robot_angle):
        alpha = np.deg2rad(lidar_angle)
        theta = np.deg2rad(robot_angle)

        table_x = distance*np.sin(alpha - theta) - self.m*np.sin(theta) + x_cur
        table_y = distance*np.cos(alpha - theta) + self.m*np.cos(theta) + y_cur
 
        return table_x, table_y

if __name__ == "__main__":
    matrix = TransformMatrix(50)

    point = matrix.lidar2table(500, 500, 200, 180, -90)
    print(point)
