from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy_plava_KAMERA = Strategy()

strategy_plava_KAMERA.rotate_to(0)

strategy_plava_KAMERA.set_skip_flag(1)

strategy_plava_KAMERA.back_sensors_on()
strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(
    185, -1900, False, ts=0.5, at=0, b=100, bs=0.5)  # rotira panele
strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.activate_triangle()
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
# strategy_plava_KAMERA.add_sequence(prepare_front_arm())
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.skip_to_flag(1)
strategy_plava_KAMERA.deactivate_triangle()

strategy_plava_KAMERA.add_points("unload", 25)  # ispisuje poene za panele

strategy_plava_KAMERA.check_cam([4, 1, 3, 2, 6, 5])
strategy_plava_KAMERA.check_cam([1, 3, 2, 6, 5, 4])

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

# strategy_plava_KAMERA.start_step_actions()
# strategy_plava_KAMERA.go_to_XY(1000, 1500, at=2, b=100)
# strategy_plava_KAMERA.deactivate_zadnja_grtalca()
# strategy_plava_KAMERA.end_step_actions()

# strategy_plava_KAMERA.go_to_XY(1000, 600, at=2, b=50)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1750, -810, False, at=100, b=50, bs=1)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.rotate_to(90)

strategy_plava_KAMERA.all_off()
strategy_plava_KAMERA.set_distance_angle(-90, 0)

strategy_plava_KAMERA.rotate_to(90)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_bez_limova())

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.go_to_XY(1600, -810, at=100, b=50)

strategy_plava_KAMERA.start_step_actions()
# strategy_plava_KAMERA.go_to_XY(1382, 700, False, at=100, b=50)
strategy_plava_KAMERA.go_to_XY(1382, -210, at=100, b=200)  # 185
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.end_step_actions()

# strategy_plava_KAMERA.start_step_actions()  # podize ruku
strategy_plava_KAMERA.rotate_to(0)
# ostavlja biljke u drugi plenter
# strategy_plava_KAMERA.end_step_actions()
strategy_plava_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.set_distance_angle(-200, 0, at=100, b=50)

strategy_plava_KAMERA.set_skip_flag("KRADJA PREDNJA")
strategy_plava_KAMERA.check_cam([6, 5, 3, 2, 1, 4])
strategy_plava_KAMERA.set_skip_flag("KRADJA ZADNJA")
strategy_plava_KAMERA.check_cam([3, 5, 2, 1, 4, 6])

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(562, -2300, at=100, b=50)
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.start_step_actions()  # dolazi i priprema ruku
strategy_plava_KAMERA.go_to_XY(562, -2680, at=100, b=50)
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.move_back_arm(210, v=15)
# ostavlja prednje u planter bez saksija
strategy_plava_KAMERA.move_mechanism(340)
strategy_plava_KAMERA.end_step_actions()

# strategy_plava_KAMERA.move_mechanism(180)
strategy_plava_KAMERA.move_front_arm(100, v=15)
strategy_plava_KAMERA.ungrip_front()
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.set_distance_angle(70, 0)
strategy_plava_KAMERA.activate_prednja_desna_grtalca()
strategy_plava_KAMERA.set_distance_angle(0, 90, g=0.6)

strategy_plava_KAMERA.add_points("unload", 8)

strategy_plava_KAMERA.deactivate_prednja_desna_grtalca()
strategy_plava_KAMERA.set_distance_angle(-30, 0)
strategy_plava_KAMERA.go_to_XY(562, -2800, False, at=100, b=50)
strategy_plava_KAMERA.rotate_to(0)
strategy_plava_KAMERA.set_distance_angle(-50, 0)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_plava_KAMERA.go_to_XY(650, -2750)

# strategy_plava_KAMERA.move_mechanism(100)

# strategy_plava_KAMERA.set_skip_flag("KRADJA PREDNJA")
# strategy_plava_KAMERA.check_cam([1,2,3,4,5,6])

strategy_plava_KAMERA.end()

# ==================KRADJA ZADNJA===================================
strategy_plava_KAMERA.skip_to_flag("KRADJA ZADNJA")
strategy_plava_KAMERA.check_time(85, "prednji brzi istovar")
strategy_plava_KAMERA.set_skip_flag("prednji brzi istovar")

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1242, -2600, at=2, b=200)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1302, -2780, at=2, b=200)
strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.activate_prednja_leva_grtalca()
strategy_plava_KAMERA.move_mechanism(180)
strategy_plava_KAMERA.move_back_arm(210)
# strategy_plava_KAMERA.move_mechanism(20)
# strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.end_step_actions()
strategy_plava_KAMERA.rotate_to(80)

strategy_plava_KAMERA.deactivate_prednja_leva_grtalca()

strategy_plava_KAMERA.go_to_XY(1352, -2870)
strategy_plava_KAMERA.rotate_to(180)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.set_distance_angle(20, 0)
strategy_plava_KAMERA.move_mechanism(340)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.move_front_arm(75, v=15)

strategy_plava_KAMERA.set_skip_flag("prednji brzi istovar")
strategy_plava_KAMERA.grip_front()
strategy_plava_KAMERA.check_object()
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.move_mechanism(180)

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1302, -2250, False, at=0, b=200)
strategy_plava_KAMERA.move_mechanism(180)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.go_to_XY(632, -2250, False, at=0, b=50)
strategy_plava_KAMERA.go_to_XY(632, -2820, False, at=100, b=50)
strategy_plava_KAMERA.rotate_to(0)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()
strategy_plava_KAMERA.set_distance_angle(100, 0, at=100, b=50)

# strategy_plava_KAMERA.start_step_actions()
# strategy_plava_KAMERA.rotate_to(180)
# strategy_plava_KAMERA.move_mechanism(20)
# strategy_plava_KAMERA.end_step_actions()

# # strategy_plava_KAMERA.go_to_XY(562, 2750, False)
# strategy_plava_KAMERA.move_back_arm(190, v=15)
# strategy_plava_KAMERA.ungrip_back()
# strategy_plava_KAMERA.activate_zadnja_desna_grtalca()
# strategy_plava_KAMERA.set_distance_angle(0, -90, g=0.6)

strategy_plava_KAMERA.all_off()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(650, -2750)
strategy_plava_KAMERA.move_front_arm(80, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.ungrip_front()
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.end()

# ==================KRADJA PREDNJA===================================

# ipak je zadnja ali nemamo 3. bunt
strategy_plava_KAMERA.skip_to_flag("KRADJA PREDNJA")
# strategy_plava_KAMERA.check_time(95, "timeout")

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1242, -2600, at=2, b=200)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1302, -2780, at=2, b=200)
strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.activate_prednja_leva_grtalca()
strategy_plava_KAMERA.move_mechanism(180)
strategy_plava_KAMERA.move_back_arm(210)
# strategy_plava_KAMERA.move_mechanism(20)
# strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.end_step_actions()
strategy_plava_KAMERA.rotate_to(80)

strategy_plava_KAMERA.deactivate_prednja_leva_grtalca()

strategy_plava_KAMERA.go_to_XY(1352, -2870)
strategy_plava_KAMERA.rotate_to(180)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.set_distance_angle(20, 0)
strategy_plava_KAMERA.move_mechanism(340)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.move_front_arm(75, v=15)

strategy_plava_KAMERA.set_skip_flag("nastavak kradje")
strategy_plava_KAMERA.grip_front()
strategy_plava_KAMERA.check_object()

strategy_plava_KAMERA.move_front_arm(120, v=15)

strategy_plava_KAMERA.move_mechanism(180)
strategy_plava_KAMERA.set_skip_flag("zadnji brzi istovar")
strategy_plava_KAMERA.check_time(85, "zadnji brzi istovar")

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.go_to_XY(1302, -2450, False, at=0, b=200)
strategy_plava_KAMERA.go_to_XY(562, -450, False, at=0, b=200)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(592, -195, False, at=0, b=200)
strategy_plava_KAMERA.move_back_arm(210, v=30)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.rotate_to(180)
strategy_plava_KAMERA.move_mechanism(10)  # ovo samo ja smem!!! - Andrija
strategy_plava_KAMERA.move_back_arm(170, v=15)
strategy_plava_KAMERA.grip_back()
strategy_plava_KAMERA.check_object()
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.move_mechanism(180)

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.go_to_XY(632, -2820, at=100, b=50)
strategy_plava_KAMERA.rotate_to(180)
strategy_plava_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_plava_KAMERA.all_off()

strategy_plava_KAMERA.set_distance_angle(-100, 0)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(650, -2750)
strategy_plava_KAMERA.move_back_arm(170, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.move_back_arm(210, v=15)

# strategy_plava_KAMERA.set_distance_angle(100, 0)
# strategy_plava_KAMERA.rotate_to(0)
# strategy_plava_KAMERA.go_to_XY(562, 2750)
# strategy_plava_KAMERA.rotate_to(0)
# strategy_plava_KAMERA.move_front_arm(100, v=15)
# strategy_plava_KAMERA.ungrip_front()
# strategy_plava_KAMERA.activate_prednja_leva_grtalca()
# strategy_plava_KAMERA.set_distance_angle(0, -90, g=0.6)

# strategy_plava_KAMERA.set_distance_angle(100, 0)
strategy_plava_KAMERA.end()

# =============== nastavak kradje ==================


strategy_plava_KAMERA.skip_to_flag("nastavak kradje")

strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.move_mechanism(180)

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(1302, -2450, False, at=0, b=100)
strategy_plava_KAMERA.deactivate_prednja_grtalca()
strategy_plava_KAMERA.deactivate_zadnja_grtalca()
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.check_time(85, "timeout")

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.go_to_XY(1302, -2450, False, at=0, b=200)
strategy_plava_KAMERA.go_to_XY(562, -450, False, at=0, b=200)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(592, -195, False, at=0, b=200)
strategy_plava_KAMERA.move_back_arm(210, v=30)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.rotate_to(180)
strategy_plava_KAMERA.move_mechanism(10)  # ovo samo ja smem!!! - Andrija
strategy_plava_KAMERA.move_back_arm(170, v=15)

strategy_plava_KAMERA.set_skip_flag("timeout")
strategy_plava_KAMERA.grip_back()
strategy_plava_KAMERA.check_object()
strategy_plava_KAMERA.move_back_arm(210, v=15)
strategy_plava_KAMERA.move_mechanism(180)

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.go_to_XY(632, -2620, at=100, b=50)

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.go_to_XY(632, -2820, False, at=100, b=50)
strategy_plava_KAMERA.rotate_to(0)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_plava_KAMERA.all_off()

strategy_plava_KAMERA.set_distance_angle(100, 0)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(650, -2750)
strategy_plava_KAMERA.move_front_arm(80, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.ungrip_front()
strategy_plava_KAMERA.move_front_arm(120, v=15)
strategy_plava_KAMERA.end()

# ======================prednji brzi istovar=======================

strategy_plava_KAMERA.skip_to_flag("prednji brzi istovar")

strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.move_back_arm(210)

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.go_to_XY(1200, -2250, False, at=0, b=200)

strategy_plava_KAMERA.go_to_XY(632, -2820, False, at=100, b=50)
strategy_plava_KAMERA.rotate_to(0)
strategy_plava_KAMERA.add_sequence(ostavljanje_zadnjom_rukom_sa_limova())

strategy_plava_KAMERA.all_off()

strategy_plava_KAMERA.set_distance_angle(100, 0)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(650, -2750)
strategy_plava_KAMERA.move_front_arm(80, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.ungrip_front()
strategy_plava_KAMERA.move_front_arm(120, v=15)

strategy_plava_KAMERA.end()
# ======================zadnji brzi istovar=======================

strategy_plava_KAMERA.skip_to_flag("zadnji brzi istovar")

strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.move_back_arm(210)

strategy_plava_KAMERA.front_all_off()
strategy_plava_KAMERA.back_all_on()

strategy_plava_KAMERA.go_to_XY(1000, -2250, False, at=0, b=200)

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()

strategy_plava_KAMERA.go_to_XY(632, -2820, at=100, b=50)
strategy_plava_KAMERA.rotate_to(180)
strategy_plava_KAMERA.add_sequence(ostavljanje_prednjom_rukom_sa_limovima())

strategy_plava_KAMERA.all_off()

strategy_plava_KAMERA.set_distance_angle(-100, 0)

strategy_plava_KAMERA.start_step_actions()
strategy_plava_KAMERA.go_to_XY(650, -2750)
strategy_plava_KAMERA.move_back_arm(170, v=15)
strategy_plava_KAMERA.end_step_actions()

strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.move_back_arm(210, v=15)

strategy_plava_KAMERA.end()

# ==================timeout=======================

strategy_plava_KAMERA.skip_to_flag("timeout")

strategy_plava_KAMERA.start_parallel()
strategy_plava_KAMERA.ungrip_back()
strategy_plava_KAMERA.ungrip_front()
strategy_plava_KAMERA.move_back_arm(210)
strategy_plava_KAMERA.move_front_arm(120)
strategy_plava_KAMERA.end_parallel()

strategy_plava_KAMERA.back_all_off()
strategy_plava_KAMERA.front_all_on()
strategy_plava_KAMERA.go_to_XY(650, -2750, at=100, b=0)

strategy_plava_KAMERA.end()
