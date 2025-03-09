import numpy as np
import matplotlib.pyplot as plt
import scipy.special

class CurveGenerator:
    # Function to calculate 4-point Bezier path
    @staticmethod
    def calc_4points_bezier_path(sx, sy, syaw, ex, ey, eyaw, offset):
        """
        Compute control points and path given start and end position.

        :param sx: (float) x-coordinate of the starting point
        :param sy: (float) y-coordinate of the starting point
        :param syaw: (float) yaw angle at start
        :param ex: (float) x-coordinate of the ending point
        :param ey: (float) y-coordinate of the ending point
        :param eyaw: (float) yaw angle at the end
        :param offset: (float)
        :return: (numpy array, numpy array)
        """
        dist = np.hypot(sx - ex, sy - ey) / offset
        control_points = np.array(
            [[sx, sy],
             [sx + dist * np.cos(syaw), sy + dist * np.sin(syaw)],
             [ex - dist * np.cos(eyaw), ey - dist * np.sin(eyaw)],
             [ex, ey]])

        path = CurveGenerator.calc_bezier_path(control_points, n_points=200)

        return path, control_points

    # Function to calculate the Bezier path from control points
    @staticmethod
    def calc_bezier_path(control_points, n_points=100):
        """
        Compute bezier path (trajectory) given control points.

        :param control_points: (numpy array)
        :param n_points: (int) number of points in the trajectory
        :return: (numpy array)
        """
        traj = []
        for t in np.linspace(0, 1, n_points):
            traj.append(CurveGenerator.bezier(t, control_points))

        return np.array(traj)

    # Function to calculate one point on the Bezier curve
    @staticmethod
    def bezier(t, control_points):
        """
        Return one point on the bezier curve.

        :param t: (float) number in [0, 1]
        :param control_points: (numpy array)
        :return: (numpy array) Coordinates of the point
        """
        n = len(control_points) - 1
        return np.sum([CurveGenerator.bernstein_poly(n, i, t) * control_points[i] for i in range(n + 1)], axis=0)

    # Function for Bernstein polynomial
    @staticmethod
    def bernstein_poly(n, i, t):
        """
        Bernstein polynom.

        :param n: (int) polynom degree
        :param i: (int)
        :param t: (float)
        :return: (float)
        """
        return scipy.special.comb(n, i) * t ** i * (1 - t) ** (n - i)

# Define the start and end points
# start_x = 0.0
# start_y = 0.0
# start_yaw = np.radians(0.0)

# end_x = 1000.0
# end_y = 1000.0
# end_yaw = np.radians(0.0)

# # Define the offset (affects the control points)
# offset = 3.0

# # Generate the Bezier curve and control points
# path, control_points = CurveGenerator.calc_4points_bezier_path(
#     start_x, start_y, start_yaw, end_x, end_y, end_yaw, offset)
# [data.x_current, data.y_current] = 0, 0
points = np.array([[0, 0],[100,100], [500,500], [800,800], [0,1200]])
a = CurveGenerator()
path = a.calc_bezier_path(points) # vraca np.array
np.set_printoptions(suppress=True, precision=2)
print(path)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot the Bezier curve
plt.plot(path[:, 0], path[:, 1], label='Bezier Curve', color='blue')

# Plot the control points
# plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')

# Annotate the start and end points
plt.scatter(path[0], path[-1], color='green', label='Start/End Points', zorder=5)
plt.text(path[0,0], path[0, 1], 'Start', fontsize=10, color='green')
plt.text(path[-1, 0],path[-1, 1], 'End', fontsize=10, color='green')

plt.title('Bezier Curve with Control Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
