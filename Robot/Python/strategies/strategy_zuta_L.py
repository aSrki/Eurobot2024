from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, 4 seta biljaka zbog plus 5 na simu

strategy_zuta_L = Strategy()

strategy_zuta_L.rotate_to(0)
strategy_zuta_L.back_all_on()
strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(700, 2000, False, off=120, b=0,
                         at=100)  # rotira panele #y = 750
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.activate_zadnja_grtalca()
strategy_zuta_L.add_sequence(prepare_back_arm())
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_mechanism(100)
strategy_zuta_L.add_sequence(grip_back_plant())

# strategy_zuta_L.set_skip_flag(1)

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(700, 1000, off=120, b=0, at=100)
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.activate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_mechanism(260)
strategy_zuta_L.add_sequence(grip_front_plant())  # -20 #110

# strategy_zuta_L.set_skip_flag(2)

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1000, 1500, False, at=100, b=100)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_step_actions()

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu
# strategy_zuta_L.set_skip_flag(3)

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1550, 450, at=100, b=0)  # dolazi ispred plantera
strategy_zuta_L.move_front_arm(130)  # ovo samo ja smem
strategy_zuta_L.activate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.add_points("unload", 6)

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1350, 762, False, at=100, b=0)

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_L.go_to_XY(1850, 762)
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(270)  # ostavlja prednje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_front_arm(85, v=15)
strategy_zuta_L.ungrip_front()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)
# =================================================

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()
strategy_zuta_L.go_to_XY(1382, 762, False, at=100, b=0)  # ??????

# =============================================

strategy_zuta_L.start_step_actions()  # podize ruku
strategy_zuta_L.go_to_XY(1382, 185, False, at=100, b=200)  # -285
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_back_arm(175, v=15)
strategy_zuta_L.ungrip_front()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.back_sensors_off()
strategy_zuta_L.front_sensors_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1500, 1500, off=120, b=0, at=100)
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.activate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_mechanism(260)
strategy_zuta_L.add_sequence(grip_front_plant())  # -20 #110

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(500, 1500, False, off=120, b=0,
                         at=100)  # rotira panele #y = 750
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.activate_zadnja_grtalca()
strategy_zuta_L.add_sequence(prepare_back_arm())
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_mechanism(100)
strategy_zuta_L.add_sequence(grip_back_plant())

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(195, 280, False, at=100, b=0)
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.rotate_to(0)

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(195, 1850, g=0.4)  # rotira panele #y = 750
strategy_zuta_L.activate_triangle()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.add_points("unload", 15)

strategy_zuta_L.go_to_XY(612, 2500, at=100, b=0)
strategy_zuta_L.go_to_XY(612, 2815, at=100, b=0)

strategy_zuta_L.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_L.go_to_XY(612, 2885, at=100, b=0)
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(270)  # ostavlja prednje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_front_arm(85, v=15)
strategy_zuta_L.ungrip_front()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.set_distance_angle(-100, 0)  # dolazi ispred plantera

strategy_zuta_L.back_sensors_off()

strategy_zuta_L.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_L.rotate_to(90)  # 1850
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_back_arm(167, v=15)
strategy_zuta_L.ungrip_back()

strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(180)

strategy_zuta_L.add_points("unload", 6)

strategy_zuta_L.end()

# =======================alternativna strategija========


# ==========================TIMEOUT ===========================

strategy_zuta_L.skip_to_flag("timeout")

strategy_zuta_L.front_all_on()

strategy_zuta_L.go_to_XY(700, 2780, False, at=100, b=0, bs=0.1, s=0.1)
strategy_zuta_L.add_points("unload", 10)

strategy_zuta_L.start_parallel()
strategy_zuta_L.move_front_arm(120)
strategy_zuta_L.move_mechanism(180)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_parallel()


strategy_zuta_L.all_off()

strategy_zuta_L.end()
