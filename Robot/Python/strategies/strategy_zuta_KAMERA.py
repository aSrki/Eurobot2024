from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy_zuta_KAMERA = Strategy()

strategy_zuta_KAMERA.rotate_to(0)

strategy_zuta_KAMERA.set_skip_flag(1)

strategy_zuta_KAMERA.front_sensors_on()
strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(
    180, 1900, ts=0.5, at=0, b=100, bs=0.5)  # rotira panele
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
strategy_zuta_KAMERA.check_cam([1, 5, 6, 2, 3, 4])

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

# strategy_zuta_KAMERA.start_step_actions()
# strategy_zuta_KAMERA.go_to_XY(1000, 1500, at=2, b=100)
# strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
# strategy_zuta_KAMERA.end_step_actions()

# strategy_zuta_KAMERA.go_to_XY(1000, 600, at=2, b=50)

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1750, 810, at=100, b=50, bs=1)
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.rotate_to(-90)

strategy_zuta_KAMERA.all_off()
strategy_zuta_KAMERA.set_distance_angle(80, 0)

# strategy_zuta_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_bez_limova())
# strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(1600, 810, False, at=100, b=50)

strategy_zuta_KAMERA.start_step_actions()
# strategy_zuta_KAMERA.go_to_XY(1382, 700, False, at=100, b=50)
strategy_zuta_KAMERA.go_to_XY(1382, 210, False, at=100, b=200)  # 185
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
strategy_zuta_KAMERA.go_to_XY(562, 2700, False, at=100, b=50)
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
strategy_zuta_KAMERA.deactivate_prednja_grtalca()
strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.move_front_arm(120, v=15)
# ostavlja prednje u planter bez saksija
strategy_zuta_KAMERA.move_mechanism(20)
strategy_zuta_KAMERA.end_step_actions()

# strategy_zuta_KAMERA.move_mechanism(180)
strategy_zuta_KAMERA.move_back_arm(190, v=15)
strategy_zuta_KAMERA.ungrip_back()
strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.set_distance_angle(-50, 0)
strategy_zuta_KAMERA.activate_zadnja_desna_grtalca()
strategy_zuta_KAMERA.set_distance_angle(0, -90, g=0.6)
strategy_zuta_KAMERA.deactivate_zadnja_desna_grtalca()
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.go_to_XY(562, 2820, at=100, b=50)
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_zuta_KAMERA.go_to_XY(800, 2750, False)

# strategy_zuta_KAMERA.move_mechanism(100)

# strategy_zuta_KAMERA.set_skip_flag("KRADJA PREDNJA")
# strategy_zuta_KAMERA.check_cam([1,2,3,4,5,6])

strategy_zuta_KAMERA.end()

# ==================KRADJA ZADNJA===================================
strategy_zuta_KAMERA.skip_to_flag("KRADJA ZADNJA")
strategy_zuta_KAMERA.check_time(85, "prednji brzi istovar")
strategy_zuta_KAMERA.set_skip_flag("prednji brzi istovar")

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1222, 2600, False, at=2, b=200)
strategy_zuta_KAMERA.deactivate_prednja_grtalca()
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1282, 2780, False, at=2, b=200)
strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.activate_zadnja_leva_grtalca()
strategy_zuta_KAMERA.move_mechanism(180)
strategy_zuta_KAMERA.move_front_arm(120)
# strategy_zuta_KAMERA.move_mechanism(20)
# strategy_zuta_KAMERA.ungrip_back()
strategy_zuta_KAMERA.end_step_actions()
strategy_zuta_KAMERA.rotate_to(-80)

strategy_zuta_KAMERA.deactivate_zadnja_leva_grtalca()
strategy_zuta_KAMERA.rotate_to(180)

strategy_zuta_KAMERA.go_to_XY(1302, 2870, False)

strategy_zuta_KAMERA.move_mechanism(20)
strategy_zuta_KAMERA.move_back_arm(165, v=15)

strategy_zuta_KAMERA.set_skip_flag("prednji brzi istovar")
strategy_zuta_KAMERA.grip_back()
strategy_zuta_KAMERA.check_object()
strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.go_to_XY(1302, 2250, at=0, b=200)
strategy_zuta_KAMERA.go_to_XY(562, 2250, at=0, b=50)
strategy_zuta_KAMERA.go_to_XY(562, 2820, at=100, b=50)
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_zuta_KAMERA.set_distance_angle(-100, 0)

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.rotate_to(180)
strategy_zuta_KAMERA.move_mechanism(20)
strategy_zuta_KAMERA.end_step_actions()

# strategy_zuta_KAMERA.go_to_XY(562, 2750, False)
strategy_zuta_KAMERA.move_back_arm(190, v=15)
strategy_zuta_KAMERA.ungrip_back()
strategy_zuta_KAMERA.activate_zadnja_desna_grtalca()
strategy_zuta_KAMERA.set_distance_angle(0, -90, g=0.6)

strategy_zuta_KAMERA.go_to_XY(800, 2750, False)
strategy_zuta_KAMERA.end()

# ==================KRADJA PREDNJA===================================

# ipak je zadnja ali nemamo 3. bunt
strategy_zuta_KAMERA.skip_to_flag("KRADJA PREDNJA")
# strategy_zuta_KAMERA.check_time(95, "timeout")

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1282, 2600, False, at=2, b=200)
strategy_zuta_KAMERA.deactivate_zadnja_grtalca()
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(1282, 2760, False, at=2, b=200)
strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.activate_zadnja_leva_grtalca()
strategy_zuta_KAMERA.move_mechanism(180)
strategy_zuta_KAMERA.move_front_arm(120)
# strategy_zuta_KAMERA.move_mechanism(20)
# strategy_zuta_KAMERA.ungrip_back()
strategy_zuta_KAMERA.end_step_actions()
strategy_zuta_KAMERA.rotate_to(-80)

strategy_zuta_KAMERA.deactivate_zadnja_leva_grtalca()
strategy_zuta_KAMERA.rotate_to(180)

strategy_zuta_KAMERA.go_to_XY(1302, 2870, False)

strategy_zuta_KAMERA.move_mechanism(20)
strategy_zuta_KAMERA.move_back_arm(165, v=15)

strategy_zuta_KAMERA.set_skip_flag("nastavak kradje")  # TODO: napravi
strategy_zuta_KAMERA.grip_back()
strategy_zuta_KAMERA.check_object()

strategy_zuta_KAMERA.move_back_arm(210, v=15)

strategy_zuta_KAMERA.move_mechanism(180)
strategy_zuta_KAMERA.set_skip_flag("zadnji brzi istovar")
strategy_zuta_KAMERA.check_time(85, "zadnji brzi istovar")

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.go_to_XY(1302, 2450, at=0, b=200)
strategy_zuta_KAMERA.go_to_XY(562, 450, at=0, b=200)

strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(592, 195, at=0, b=200)
strategy_zuta_KAMERA.move_front_arm(120, v=30)
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.rotate_to(180)
strategy_zuta_KAMERA.move_mechanism(350)  # ovo samo ja smem!!! - Andrija
strategy_zuta_KAMERA.move_front_arm(80, v=15)
strategy_zuta_KAMERA.grip_front()
strategy_zuta_KAMERA.check_object()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(562, 2820, False, at=100, b=50)
strategy_zuta_KAMERA.rotate_to(180)
strategy_zuta_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())
strategy_zuta_KAMERA.set_distance_angle(100, 0)
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.go_to_XY(562, 2750)
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.move_front_arm(100, v=15)
strategy_zuta_KAMERA.ungrip_front()
strategy_zuta_KAMERA.activate_prednja_leva_grtalca()
strategy_zuta_KAMERA.set_distance_angle(0, -90, g=0.6)

strategy_zuta_KAMERA.set_distance_angle(100, 0)
strategy_zuta_KAMERA.end()

# =============== nastavak kradje ==================


strategy_zuta_KAMERA.skip_to_flag("nastavak kradje")

strategy_zuta_KAMERA.move_back_arm(210, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

strategy_zuta_KAMERA.check_time(85, "timeout")

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.go_to_XY(1302, 2450, at=0, b=200)
strategy_zuta_KAMERA.start_step_actions()
strategy_zuta_KAMERA.go_to_XY(562, 190, at=0, b=200)
strategy_zuta_KAMERA.move_front_arm(120, v=30)
strategy_zuta_KAMERA.end_step_actions()

strategy_zuta_KAMERA.rotate_to(180)
strategy_zuta_KAMERA.move_mechanism(340)
strategy_zuta_KAMERA.move_front_arm(80, v=15)

strategy_zuta_KAMERA.set_skip_flag("timeout")
strategy_zuta_KAMERA.grip_front()
strategy_zuta_KAMERA.check_object()
strategy_zuta_KAMERA.move_front_arm(120, v=15)
strategy_zuta_KAMERA.move_mechanism(180)

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(562, 2820, False, at=100, b=50)
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_zuta_KAMERA.go_to_XY(800, 2750, False)
strategy_zuta_KAMERA.end()

# ======================prednji brzi istovar=======================

strategy_zuta_KAMERA.skip_to_flag("prednji brzi istovar")

strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.move_front_arm(120)

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(1200, 2250, at=0, b=200)

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.go_to_XY(562, 2820, at=100, b=50)
strategy_zuta_KAMERA.rotate_to(0)
strategy_zuta_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_zuta_KAMERA.go_to_XY(800, 2750, False)
strategy_zuta_KAMERA.end()
# ======================zadnji brzi istovar=======================

strategy_zuta_KAMERA.skip_to_flag("zadnji brzi istovar")

strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.move_front_arm(120)

strategy_zuta_KAMERA.back_all_off()
strategy_zuta_KAMERA.front_all_on()

strategy_zuta_KAMERA.go_to_XY(1000, 2250, at=0, b=200)

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()

strategy_zuta_KAMERA.go_to_XY(562, 2820, False, at=100, b=50)
strategy_zuta_KAMERA.rotate_to(180)
strategy_zuta_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_zuta_KAMERA.go_to_XY(800, 2750, False)
strategy_zuta_KAMERA.end()

# ==================timeout=======================

strategy_zuta_KAMERA.skip_to_flag("timeout")

strategy_zuta_KAMERA.start_parallel()
strategy_zuta_KAMERA.ungrip_back()
strategy_zuta_KAMERA.ungrip_front()
strategy_zuta_KAMERA.move_back_arm(210)
strategy_zuta_KAMERA.move_front_arm(120)
strategy_zuta_KAMERA.end_parallel()

strategy_zuta_KAMERA.front_all_off()
strategy_zuta_KAMERA.back_all_on()
strategy_zuta_KAMERA.go_to_XY(800, 2750, False)

strategy_zuta_KAMERA.end()
