from sima import *

sima = Sima(100, 100, 0, 86, 86, 119)
sima.run_odom()

try:
    sima.go_to_XY(500, 100)
    sima.go_to_XY(500, 500)
    sima.go_to_XY(100, 500)
    sima.go_to_XY(100, 100)

except KeyboardInterrupt:
    sima.stop()
