from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, 4 seta biljaka zbog plus 5 na simu

strategy_zuta_L = Strategy()

strategy_zuta_L.rotate_to(0)

strategy_zuta_L.add_sequence(yellow_get_5_back())

strategy_zuta_L.set_skip_flag(1)  # ako ne nadje nista na drugom setu

strategy_zuta_L.add_sequence(yellow_get_3_front(True))  # -20 #110

strategy_zuta_L.skip_to_flag("reset")

# strategy_zuta_L.set_skip_flag(2)

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1000, 1500, False, at=100, b=200)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_step_actions()

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu
# strategy_zuta_L.set_skip_flag(3)

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1550, 450, at=100, b=50)  # dolazi ispred plantera
strategy_zuta_L.move_front_arm(130)  # ovo samo ja smem
strategy_zuta_L.activate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1350, 762, False, at=100, b=50)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

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
strategy_zuta_L.go_to_XY(1432, 762, False, at=100, b=50)  # ??????

# =============================================

strategy_zuta_L.start_step_actions()  # podize ruku
strategy_zuta_L.go_to_XY(1432, 200, False, at=100, b=200)  # -285
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_back_arm(175, v=15)
strategy_zuta_L.ungrip_back()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.back_sensors_off()
strategy_zuta_L.front_sensors_on()

strategy_zuta_L.set_skip_flag(3)
strategy_zuta_L.add_sequence(yellow_get_1_front(True))
strategy_zuta_L.skip_to_flag("reset")

strategy_zuta_L.add_sequence(yellow_get_4_back())

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(210, 280, False, at=100, b=50)
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.rotate_to(0)
strategy_zuta_L.move_mechanism(180)
strategy_zuta_L.move_front_arm(80)
strategy_zuta_L.move_back_arm(210)
strategy_zuta_L.end_step_actions()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(185, 1850, g=1, at=100,
                         b=50, ts = 0.5)  # rotira panele #y = 750
strategy_zuta_L.activate_triangle()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.add_points("unload", 30)

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(562, 2300, at=100, b=50)
strategy_zuta_L.deactivate_triangle()
strategy_zuta_L.end_step_actions()
# strategy_zuta_L.go_to_XY(612, 2815, at=100, b=50)

strategy_zuta_L.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_L.go_to_XY(562, 2800, at=100, b=50)
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(340)  # ostavlja prednje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_front_arm(85, v=15)
strategy_zuta_L.ungrip_front()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(450, 450, False, at=100,
                         b=50)  # dolazi ispred plantera

strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.back_sensors_off()

# dolazi i priprema ruku # 1850

strategy_zuta_L.move_back_arm(177, v=15)
strategy_zuta_L.ungrip_back()

strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(180)

# strategy_zuta_L.add_points("unload", 6)

strategy_zuta_L.end()

# =======================alternativna strategija========
strategy_zuta_L.skip_to_flag(1)

strategy_zuta_L.add_sequence(yellow_get_6_front())

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1400, 2150, at=100, b=200)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_step_actions()

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu
# strategy_zuta_L.set_skip_flag(3)

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1650, 450, at=100, b=200)  # dolazi ispred plantera
strategy_zuta_L.move_front_arm(130)  # ovo samo ja smem
strategy_zuta_L.activate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(1350, 762, False, at=100, b=50)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

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
strategy_zuta_L.go_to_XY(1432, 762, False, at=100, b=50)  # ??????

# =============================================

strategy_zuta_L.start_step_actions()  # podize ruku
strategy_zuta_L.go_to_XY(1432, 185, False, at=100, b=200)  # -285
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_back_arm(175, v=15)
strategy_zuta_L.ungrip_back()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_back_arm(210, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.set_skip_flag(2)
strategy_zuta_L.set_distance_angle(300, 0, at=0, b=200)
strategy_zuta_L.skip_to_flag(2)

strategy_zuta_L.skip_to_flag(3)
strategy_zuta_L.add_sequence(yellow_get_4_front())

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(210, 280, False, at=100, b=50)
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.back_all_off()
strategy_zuta_L.front_all_on()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.rotate_to(0)
strategy_zuta_L.move_mechanism(180)
strategy_zuta_L.move_front_arm(80)
strategy_zuta_L.move_back_arm(210)
strategy_zuta_L.end_step_actions()

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(185, 1850, g=1, at=100,
                         b=50, ts = 0.5)  # rotira panele #y = 750
strategy_zuta_L.activate_triangle()
strategy_zuta_L.end_step_actions()

strategy_zuta_L.add_points("unload", 30)

strategy_zuta_L.start_step_actions()
strategy_zuta_L.go_to_XY(562, 2300, at=100, b=50)
strategy_zuta_L.deactivate_triangle()
strategy_zuta_L.end_step_actions()
# strategy_zuta_L.go_to_XY(612, 2815, at=100, b=50)

strategy_zuta_L.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_L.go_to_XY(562, 2800, at=100, b=50)
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(340)  # ostavlja prednje u planter bez saksija
strategy_zuta_L.end_step_actions()

strategy_zuta_L.move_front_arm(85, v=15)
strategy_zuta_L.ungrip_front()

# strategy_zuta_L.start_parallel()
strategy_zuta_L.move_front_arm(120, v=15)
strategy_zuta_L.move_mechanism(180)
# strategy_zuta_L.end_parallel()

strategy_zuta_L.add_points("unload", 24)

strategy_zuta_L.front_all_off()
strategy_zuta_L.back_all_on()

strategy_zuta_L.go_to_XY(450, 450, False, at=100,
                         b=50)  # dolazi ispred plantera

strategy_zuta_L.end()


# ==========================TIMEOUT ===========================

strategy_zuta_L.skip_to_flag("timeout")

strategy_zuta_L.front_all_on()

strategy_zuta_L.go_to_XY(450, 450, False, at=100, b=50, bs=0.1, s=0.1)
# strategy_zuta_L.add_points("unload", 10)

strategy_zuta_L.start_parallel()
strategy_zuta_L.ungrip_back()
strategy_zuta_L.ungrip_front()
strategy_zuta_L.move_front_arm(120)
strategy_zuta_L.move_mechanism(180)
strategy_zuta_L.deactivate_prednja_grtalca()
strategy_zuta_L.deactivate_zadnja_grtalca()
strategy_zuta_L.end_parallel()

strategy_zuta_L.all_off()

strategy_zuta_L.end()
