from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy_zuta_KAMERA = Strategy()

strategy_zuta_KAMERA.rotate_to(0)

strategy_zuta_KAMERA.set_skip_flag(1)

strategy_zuta_KAMERA.front_sensors_on()
strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(
    180, 1800, ts=0.5, at=0, b=100, bs=0.5)  # rotira panele
strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.activate_triangle()
strategy_zuta_KAMERA.deactivate_prednja_grtalca()
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
# strategy_zuta_KAMERA.add_sequence(prepare_front_arm())
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.skip_to_flag(1)
strategy_zuta_KAMERA.deactivate_triangle()

strategy_zuta_KAMERA.add_points("unload", 15)  # ispisuje poene za panele

strategy_zuta_KAMERA.check_cam([4, 1, 5, 6, 2, 3])
strategy_zuta_KAMERA.check_cam([1, 5, 6, 3, 2, 4])

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1000, 1500, at=2, b=100)
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.go_to_XY(1000, 600, at=2, b=50)

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1800, 810, at=100, b=50, bs=1)
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.rotate_to(-90)

strategy_zuta_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_KAMERA.set_distance_angle(30, 0)
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_bez_limova())
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(1600, 810, False, at=100, b=50)

strategy_zuta_KAMERA.start_step_actions()
# strategy_zuta_KAMERA.go_to_XY(1382, 700, False, at=100, b=50)
strategy_zuta_KAMERA.go_to_XY(1382, 230, False, at=100, b=200)  # 185
strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.end_step_actions()

# strategy_zuta_KAMERA.start_step_actions()  # podize ruku
strategy_zuta_KAMERA.rotate_to(0)
# ostavlja biljke u drugi plenter
# strategy_zuta_KAMERA.end_step_actions()
strategy_zuta_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.set_distance_angle(200, 0)

strategy_zuta_KAMERA.set_skip_flag("KRADJA PREDNJA")
strategy_zuta_KAMERA.check_cam([2, 3, 5, 6, 1, 4])
strategy_zuta_KAMERA.set_skip_flag("KRADJA ZADNJA")
strategy_zuta_KAMERA.check_cam([5, 3, 6, 1, 4, 2])

strategy_zuta_KAMERA.go_to_XY(562, 2300, False, at=100, b=50)

strategy_zuta_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_KAMERA.go_to_XY(562, 2800, False, at=100, b=50)
strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.move_front_arm(120, v=15)
# ostavlja prednje u planter bez saksija
strategy_zuta_KAMERA.move_mechanism(20)
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_zuta_KAMERA.set_distance_angle(100, 0)
strategy_zuta_KAMERA.go_to_XY(562, 2730)

strategy_zuta_KAMERA.move_mechanism(100)
strategy_zuta_KAMERA.move_front_arm(100, v=15)
strategy_zuta_KAMERA.ungrip_front()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

# strategy_zuta_KAMERA.set_skip_flag("KRADJA")
# strategy_zuta_KAMERA.check_cam([1,2,3,4,5,6])

strategy_zuta_KAMERA.end()

# ==================KRADJA===================================

strategy_zuta_KAMERA.skip_to_flag("KRADJA PREDNJA")

strategy_zuta_KAMERA.go_to_XY(1302, 2400)
strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1302, 2870)
strategy_zuta_KAMERA.move_front_arm(120)
strategy_zuta_KAMERA.move_mechanism(340)
strategy_zuta_KAMERA.ungrip_front()
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.move_front_arm(83, v=15)
strategy_zuta_KAMERA.grip_front()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

# =========timeout=======================
strategy_zuta_KAMERA.skip_to_flag("timeout")

strategy_zuta_KAMERA.end()
