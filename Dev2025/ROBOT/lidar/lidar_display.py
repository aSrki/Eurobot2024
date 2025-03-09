from math import cos, sin, pi, floor, sqrt, degrees, atan
import os
import pygame
from shapely.geometry import LineString , Point
from global_var import *


class LidarDisplay:

    def __init__(self):
        # Screen width & height
        self.W = 640
        self.H = 640

        ########### Za graficki prikaz
        pygame.display.init()
        self.lcd = pygame.display.set_mode((self.W, self.H))
        pygame.mouse.set_visible(False)
        self.lcd.fill((200, 0, 0))
        pygame.display.update()
        #######
        self.radians = 0


        # Set up pygame and the display
        os.putenv('SDL_FBDEV', '/dev/fb1')



        # used to scale data to fit on the screen
        self.max_distance = 1
        print("setovan displej")



    def print_line(self,x1, y1, x2, y2, color1=100, color2=130, color3=100):
        lcd =self.lcd
        pygame.draw.line(lcd, pygame.Color(color1, color2, color3),
                         (int(x1 / self.max_distance * (self.W / 2)) + self.W / 2,
                          int(y1 / self.max_distance * (self.H / 2)) + self.H / 2),
                         (int(x2 / self.max_distance * (self.W / 2)) + self.W / 2,
                          int(y2 / self.max_distance * (self.H / 2)) + self.H / 2))
        
        


    # pylint: disable=redefined-outer-name,global-statement
    def process_data(self,data, obstacles=None):
        lcd =self.lcd
        W=self.W
        H=self.H
        
        # DEF PARAM
        if obstacles is None:
            obstacles = [0][0]
        

        self.lcd.fill((0, 0, 0))
        point = (int(self.W / 2), int(self.H / 2))
        
        # CRTA POZADINU DISPLEJA
        pygame.draw.circle(lcd, pygame.Color(255, 255, 255), point, 10)
        pygame.draw.circle(lcd, pygame.Color(100, 100, 100), point, 100, 1)
        pygame.draw.line(lcd, pygame.Color(100, 100, 100), (0, int(H / 2)), (W, int(H / 2)))
        pygame.draw.line(lcd, pygame.Color(100, 100, 100), (int(self.W / 2), 0), (int(self.W / 2), H))




        self.draw_robot(RobotDimenssions.width, RobotDimenssions.length,)




        # PROLAZI KROZ SCAN DATA I CRTA  TACKE
        for angle in range(360):
            if (360 - LIDAR_ANGLE / 2) <= angle or angle <= LIDAR_ANGLE / 2:

                distance = data[angle]
                # print("D: ", distance)

                if distance > LOWER_BOUNDERY:  # ignore initially ungathered data points

                    self.max_distance = max([min([5000, distance]), self.max_distance])
                    self.radians = angle * pi / 180.0

                    x = RobotDimenssions.length * cos(self.radians)
                    y = RobotDimenssions.length * sin(self.radians)
                    point = (int(self.W / 2) + int(x / self.max_distance * (self.W / 2)),
                             int(self.H / 2) + int(y / self.max_distance * (self.H / 2)))
                    pygame.draw.circle(lcd, pygame.Color(255, 0, 255), point, 1)



                    x = distance * cos(self.radians)
                    y = distance * sin(self.radians)
                    point = (int(self.W / 2) + int(x / self.max_distance * (self.W / 2)),
                             int(self.H / 2) + int(y / self.max_distance * (self.H / 2)))
                    pygame.draw.circle(lcd, pygame.Color(255, 0, 0), point, 2)


        self.draw_scanning_area(RobotDimenssions.width, RobotDimenssions.length)
        # self.draw_us_detection(.RobotDimensions.WIDTH,.RobotDimensions.LENGTH)







        # pygame.draw.line(lcd, pygame.Color(100, 130, 100), (0 +W/2, 0 + H/2),
        #                  (100, 100))
        
        self.process_objects(obstacles)
        pygame.display.update()
        



    def draw_scanning_area(self,x=700,y=1000):
        point_start = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(x/2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(y / self.max_distance * (self.W / 2)),
                     int(self.H / 2) + int(x/2 / self.max_distance * (self.H / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 255, 0), point_start, point_end, 2)


        point_start = (int(self.W / 2) + int(y / self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(x/2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(y / self.max_distance * (self.W / 2)),
                     int(self.W / 2) - int(x/2 / self.max_distance * (self.W / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 255, 0), point_start, point_end, 2)

        point_start = (int(self.W / 2) + int(y / self.max_distance * (self.W / 2)),
                       int(self.H / 2) - int(x/2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
                     int(self.H / 2) - int(x/2 / self.max_distance * (self.H / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 255, 0), point_start, point_end, 2)


    def draw_us_detection(self,x,y):
        y +=100 #todo data nije povezano
        # print("us sensors detection : ",.us_detection)
        # if .us_detection in (.DetectState.BACK_CLOSE, .DetectState.BACK_FAR):
        #     point_start = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
        #                    int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        #     point_end = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
        #                  int(self.W / 2) + int(-x / 2 / self.max_distance * (self.W / 2)))

        #     pygame.draw.line(self.lcd, pygame.Color(250, 0, 0), point_start, point_end, 2)

        # elif .us_detection in (.DetectState.FRONT_FAR, .DetectState.FRONT_CLOSE):
        #     point_start = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
        #                    int(self.H / 2) + int(- x / 2 / self.max_distance * (self.H / 2)))

        #     point_end = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
        #                  int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        #     pygame.draw.line(self.lcd, pygame.Color(250, 0, 0), point_start, point_end, 2)

    def draw_robot(self,x,y):
        point_start = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
                     int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 0, 250), point_start, point_end, 2)

        #-------------------------
        point_start = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
                     int(self.W / 2) + int(-x / 2 / self.max_distance * (self.W / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 0, 250), point_start, point_end, 2)

        # -------------------------
        point_start = (int(self.W / 2) + int(-y / self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(-x / 2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
                     int(self.H / 2) + int(- x / 2 / self.max_distance * (self.H / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 0, 250), point_start, point_end, 2)

        # -------------------------
        point_start = (int(self.W / 2) + int(1/ self.max_distance * (self.W / 2)),
                       int(self.H / 2) + int(- x / 2 / self.max_distance * (self.H / 2)))

        point_end = (int(self.W / 2) + int(1 / self.max_distance * (self.W / 2)),
                     int(self.H / 2) + int(x / 2 / self.max_distance * (self.H / 2)))

        pygame.draw.line(self.lcd, pygame.Color(0, 0, 250), point_start, point_end, 2)

    def process_objects(self,obstacles):
        
        lcd =self.lcd
        W,H = self.W,self.H
        # PRINTA OBJEKTE
        for objects in obstacles:

            if objects[0] == Shape.LINE:  # [0] = 1 - je linija, [1]-xp , [2]-yp , [3]-xq ,[4]-yq
                self.print_line(objects[1], objects[2], objects[3], objects[4])

                # print("for lcd cordinate start   = " + str(objects[1]) + "    " + str(objects[2]))
                # print("for lcd cordinate end   = " + str(objects[3]) + "    " + str(objects[4]))


            elif objects[0] == Shape.RECTANGLE:  # [0] = 1 - je linija, [1]-xp , [2]-yp , [3]-xq ,[4]-yq
                self.print_line(objects[1], objects[2], objects[3], objects[4])
                self.print_line(objects[5], objects[6], objects[7], objects[8])
                self.print_line(objects[1], objects[2], objects[5], objects[6])
                self.print_line(objects[7], objects[8], objects[3], objects[4])



            elif objects[0] == Shape.CIRCLE and objects[3] > 0:  # [0] = 2 - je krug, [1]-x0 , [2]-y0 , [3]-r
                radius = int(objects[3] / self.max_distance * (H / 2))
                if radius <= 1:
                    radius = 2

                pygame.draw.circle(lcd, pygame.Color(200, 200, 120), (
                    int(objects[1] / self.max_distance * (W / 2) + W / 2),
                    int(objects[2] / self.max_distance * (H / 2) + H / 2)),
                                   radius, 1)

        #pygame.draw.circle(lcd, pygame.Color(200, 200, 120),
         #                  (int(1000 / self.max_distance * (W / 2) + W / 2), int(0 / self.max_distance * (H / 2) + H / 2)),
          #                 int(10), 1)

        #pygame.draw.circle(lcd, pygame.Color(100, 200, 120),
         #                  (int(0 / self.max_distance * (W / 2) + W / 2), int(1500 / self.max_distance * (H / 2) + H / 2)),
          #                 int(10), 1)

        if  self.max_distance :
            rec_path = path_rectangle(path)
            self.print_line(rec_path[1], rec_path[2], rec_path[3], rec_path[4],133, 155, 100)
            self.print_line(rec_path[5], rec_path[6], rec_path[7], rec_path[8],133, 155, 100)
            self.print_line(rec_path[1], rec_path[2], rec_path[5], rec_path[6],133, 155, 100)
            self.print_line(rec_path[7], rec_path[8], rec_path[3], rec_path[4],133, 155, 100)
            
            x,y = get_x_y(path[0],path[1])
            pygame.draw.line(lcd, pygame.Color(150, 180, 110),
                             (W / 2,
                              H / 2),
                             (int(x / self.max_distance * (W / 2)) + W / 2,
                              int(y / self.max_distance * (H / 2)) + H / 2),
                             3)

























