from Sima import *

sima = Sima(100, 100, 0, 86, 86, 119)
sima.run_odom()

try:
    sima.go_to_XY(0, 100)

except KeyboardInterrupt:
    sima.stop()
