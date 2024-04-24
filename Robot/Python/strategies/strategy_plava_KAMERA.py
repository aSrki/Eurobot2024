from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy_plava_KAMERA = Strategy()

strategy_plava_KAMERA.rotate_to(0)

strategy_plava_KAMERA.back_sensors_on()
strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(195, -790, False, ts=0.5)  # rotira panele
strategy_plava_KAMERA.activate_triangle()
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
strategy_plava_KAMERA.add_sequence(prepare_back_arm())
strategy_plava_KAMERA.deactivate_triangle()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.add_points("unload", 15)  # ispisuje poene za panele

strategy_plava_KAMERA.check_cam([4, 1, 2, 3, 5, 6])
strategy_plava_KAMERA.check_cam([1, 3, 2, 5, 6, 4])

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1000, -1500, False, at=2, b=100)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.go_to_XY(1000, -600, False, at=2, b=50)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1800, -780, False, at=100, b=50, bs=1)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.rotate_to(90)

strategy_plava_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_plava_KAMERA.set_distance_angle(-50, 0)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_bez_limova())
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.set_distance_angle(100, 0, at=100, b=50)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1382, -700, at=100, b=50)
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.go_to_XY(1382, -200, at=100, b=200)  # 185
strategy_plava_KAMERA.start_step_actions()  # podize ruku
strategy_plava_KAMERA.rotate_to(0)
# ostavlja biljke u drugi plenter
strategy_plava_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.set_distance_angle(-100, 0)

strategy_plava_KAMERA.check_cam([2, 3, 5, 6, 1, 4])
strategy_plava_KAMERA.check_cam([5, 3, 6, 1, 4, 2])

strategy_plava_KAMERA.go_to_XY(562, -2300, at=100, b=50)

strategy_plava_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_plava_KAMERA.go_to_XY(562, -2800, at=100, b=50)
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.move_back_arm(210, v=15)
# ostavlja prednje u planter bez saksija
strategy_plava_KAMERA.move_mechanism(340)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_plava_KAMERA.set_distance_angle(-100, 0)
strategy_plava_KAMERA.go_to_XY(562, -2730, False)

strategy_plava_KAMERA.move_mechanism(260)
strategy_plava_KAMERA.move_back_arm(190, v=15)
strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.move_mechanism(180)

# strategy_plava_KAMERA.set_skip_flag("KRADJA")
# strategy_plava_KAMERA.check_cam([1,2,3,4,5,6])

# strategy_plava_KAMERA.end()

# ==================KRADJA===================================

# strategy_plava_KAMERA.skip_to_flag("KRADJA")

strategy_plava_KAMERA.go_to_XY(1389, -2400, False)
strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1389, -2870, False)
strategy_plava_KAMERA.move_back_arm(210)
strategy_plava_KAMERA.move_mechanism(20)
strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.move_back_arm(173, v=15)
strategy_plava_KAMERA.grip_back()
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.move_mechanism(180)

# =========timeout=======================
strategy_plava_KAMERA.skip_to_flag("timeout")

strategy_plava_KAMERA.end()
