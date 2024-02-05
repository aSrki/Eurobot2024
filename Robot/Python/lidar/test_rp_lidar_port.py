import time

from data_scaner import DataScaner, lidar  # process_scan,lidar_measurments,lidar_scans,lidar
try:
    print("\nTEST USB DEVICE PATHS:\n\n\n")
    dataScaner = DataScaner()
    for scan in dataScaner.lidar_scans(lidar):
        pass
except:
    print("\nTTY USB DEVICE DEV PATH INCORRECT\n")
    lidar.set_pwm(0)
    lidar.stop()
    lidar.disconnect()
    while True:
        time.sleep(.2)

print("\nDEV PATHS GOOD\n")
lidar.set_pwm(0)
lidar.stop()
lidar.disconnect()