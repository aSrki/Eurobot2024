from Sima import *

'''curr_x, curr_y, curr_theta, curr_angle, d_r, d_l, b'''
sima = Sima(100, 100, 0, 0, 86, 86, 119)
# sima = Sima(300, 100, 0, 0, 86, 86, 119)
# sima.run_odom()

try:
    # #square
    sima.run_odom()
    # sima.go_to_XY(300, 100)
    # sima.go_to_XY(300, 300)
    # sima.go_to_XY(100, 300)
    # sima.go_to_XY(100, 100)

    # # #forward backward - x
    sima.go_to_XY(900,100)
    sima.go_to_XY(100,100)
    #forward backward - y
    sima.go_to_XY(100,500)
    sima.go_to_XY(100,100)

except KeyboardInterrupt:
    sima.stop()
