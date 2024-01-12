from Sima import *

sima = Sima(0, 0, 0, 0, 86, 86, 119)
sima.run_odom()

try:
    sima.go_to_XY(500, 0)
    sima.go_to_XY(500, -500)
    sima.go_to_XY(0, -500)
    sima.go_to_XY(0, 0)

except KeyboardInterrupt:
    sima.stop()
