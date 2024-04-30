import cv2
import numpy as np
import socket
from math import *
import sys

def get_markers_centers(frame):
    ret_centers = [0, 0, 0, 0]

    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict,parameters=arucoParams)
    if len(corners) > 0:
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            if 23>=int(markerID)>=20:
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
                cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
                cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
                cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

                center_x = int((int(topRight[0]) + int(bottomRight[0]) + int(bottomLeft[0]) + int(topLeft[0]))/4)
                center_y = int((int(topRight[1]) + int(bottomRight[1]) + int(bottomLeft[1]) + int(topLeft[1]))/4)

                ret_centers[int(markerID)-20] = (center_x, center_y)

                cv2.putText(frame, str(markerID),(center_x,center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        return frame, ret_centers

def find_matrix(frame, input_array):
    matrix = None

    if len(input_array) < 4:
        return matrix
    
    for item in input_array:
        if item == 0:
            return matrix

    height, width = frame.shape[:2]
    input_array = np.float32(input_array)
    output_array = np.float32([(150, 150), (width-150, 150), (150, height-150), (width-150, height-150)])
    matrix = cv2.getPerspectiveTransform(input_array, output_array)
    return matrix

def get_green(frame, x_min, x_max, y_min, y_max):
    y_off = (y_max + y_min)/2
    x_off = (x_max +  x_min)/2
    r = (x_max - x_min)/2

    color_r = 0
    color_g = 0
    color_b = 0
    sum = 0

    for x in range(x_min, x_max + 1):
        A = r**2 - y_off**2 - x**2 + 2*x_off*x - x_off**2
        y2 = int(y_off + sqrt(4*(y_off**2) + 4*A)/2)
        y1 = int(y_off - sqrt(4*(y_off**2) + 4*A)/2)
        for y in range(y1, y2 + 1):
            tmp = frame[x, y]
            # color_b += tmp[0]
            color_g += tmp[1]
            # color_r += tmp[2]
            # frame[x, y] = (100, 50, 0)
            sum += 1
    # return int(color_b/sum), int(color_g/sum), int(color_r/sum)
    return 0, int(color_g/sum), 0

debug_arg = False

try:
    debug_arg = sys.argv[1]

    if debug_arg == "True" or debug_arg == "true":
        debug_arg = True

    elif debug_arg == "False" or debug_arg == "false":
        debug_arg = False

    else:
        debug_arg = False
    
    print(debug_arg)

except:
    pass


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
arucoParams = cv2.aruco.DetectorParameters()

matrix = None
matrix_found = False

host = '192.168.1.100'
port = 12345

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.settimeout(1)

if not debug_arg:
    s1.connect((host, port))

try:
    while True:
        ret, frame = cap.read()

        height, width = frame.shape[:2]

        if not matrix_found:
            frame, markers_centers = get_markers_centers(frame)
            print(markers_centers)
            matrix = find_matrix(frame, markers_centers)
            print(type(matrix))

            if matrix is not None: 
                matrix_found = True
                print("Nasao matrix")


        if matrix_found:
            frame = cv2.warpPerspective(frame, matrix, (width, height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            green_mask = cv2.inRange(frame, (15, 0, 0), (100, 255, 255))

            #isecanje zelenila
            imask = green_mask>0
            green = np.zeros_like(frame, np.uint8)
            green[imask] = frame[imask]

            frame = green
            frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

            b1, g1, r1 = get_green(frame, 93, 226, 580, 713)
            b2, g2, r2 = get_green(frame, 180, 313, 880, 1080)
            b3, g3, r3 = get_green(frame, 456, 590, 880, 1080)
            b4, g4, r4 = get_green(frame, 543, 676, 580, 713)
            b5, g5, r5 = get_green(frame, 456, 590, 200, 400)
            b6, g6, r6 = get_green(frame, 180, 313, 200, 400)

            # red_detected = [r1, r2, r3, r4, r5, r6]
            # blue_detected = [b1, b2, b3, b4, b5, b6]
            green_detected = [g1, g2, g3, g4, g5, g6]
            # print("\n=============================")
            # print(f"R: {red_detected}")
            # print(f"G: {green_detected}")
            # print(f"B: {blue_detected}")
            # print("=============================\n")

            res = ""
            for i in range(6):
                if green_detected[i]>15:
                    res += '1'
                else:
                    res += '0'
            
            if not debug_arg:
                s1.sendall(str(res).encode())
            print(res)
            # cv2.imshow('frame', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
    s1.close()
