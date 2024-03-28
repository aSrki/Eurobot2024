from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Plava strana 3 solarnih, 4 seta biljaka zbog plus 5 na sime

strategy3_brza = Strategy()

strategy3_brza.rotate_to(0)
strategy3_brza.back_all_on()
strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(195, -830, False, g=0.4)  # rotira panele #y = 750
strategy3_brza.activate_triangle()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.add_sequence(prepare_back_arm())  # priprema za hvatanje
strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 15)

# ako detektuje idemo prekoputa, ova strategija se nalazi na kraju
strategy3_brza.set_skip_flag(1)

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(500, -1500, False, off=120, b=50,
                        at=0)  # dolazi do tanjira 4 -1210
strategy3_brza.deactivate_triangle()
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_back_plant())  # -20

strategy3_brza.skip_to_flag(2)  # u slucaju da sretnemo nekoga prekoputa

strategy3_brza.back_sensors_off()
strategy3_brza.front_sensors_on()

strategy3_brza.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3_brza.go_to_XY(1500, -1500, off=120)
strategy3_brza.add_sequence(prepare_front_arm())
strategy3_brza.deactivate_zadnja_grtalca()
# strategy3_brza.move_mechanism(260)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.skip_to_flag("reset")  # gasenje flag-a

# strategy3_brza.rotate_to(-90)

strategy3_brza.add_sequence(grip_front_plant())

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1750, -762)  # dolazi ispred plantera
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_sensors_off()

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.go_to_XY(1820, -762)  # 1850
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(80, v=15)
strategy3_brza.ungrip_front()

strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(180)
strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

# ===============================================
strategy3_brza.back_sensors_on()

strategy3_brza.set_distance_angle(-100, 0)

strategy3_brza.back_sensors_off()
strategy3_brza.front_sensors_on()

strategy3_brza.start_step_actions()  # ide na sledece biljke
strategy3_brza.go_to_XY(1300, -1000, off=120)
strategy3_brza.move_mechanism(260)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_front_plant())

# ===============================================

strategy3_brza.start_step_actions()  # podize ruku
strategy3_brza.go_to_XY(1382, -185, False)  # -285
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(170, v=15)
strategy3_brza.ungrip_back()

strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(180)
strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

strategy3_brza.back_sensors_off()
strategy3_brza.front_sensors_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(150, 0)  # dolazi ispred plantera
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_sensors_off()

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.rotate_to(-90)  # 1850
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(77, v=15)
strategy3_brza.ungrip_front()

strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(180)

strategy3_brza.add_points("unload", 6)


strategy3_brza.start_step_actions()  # ide na sledece biljke
strategy3_brza.go_to_XY(700, -700, False)  # -700
strategy3_brza.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy3_brza.add_sequence(prepare_arms6())
strategy3_brza.end_step_actions()

# strategy3_brza.rotate_to(0)  # hvata biljke 6 komada
strategy3_brza.add_sequence(grip3_back_plant(-120))  # -120
# strategy3_brza.set_distance_angle(60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3_brza.back_sensors_off()

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.front_sensors_on()
# strategy3_brza.activate_prednja_grtalca()
strategy3_brza.set_distance_angle(230, 0)
strategy3_brza.add_sequence(grip_front_plant())  # 130
# strategy3_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3_brza.rotate_to(-90)


strategy3_brza.front_sensors_off()
strategy3_brza.back_sensors_on()

# strategy3_brza.go_to_XY(590, -600)  # ide da ih ostavi kako zna i ume
strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(590, -275, False)  # -285
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_sensors_off()

strategy3_brza.rotate_to(180)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(160)  # 180 130
strategy3_brza.move_back_arm(193, v=30)  # 170
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(100, 0)
strategy3_brza.grip_back()
strategy3_brza.end_step_actions()


strategy3_brza.move_front_arm(120, v=30)
strategy3_brza.go_to_XY(624, -325)  # 285 325
strategy3_brza.rotate_to(0)
# strategy3_brza.move_back_arm(190, v=15)
strategy3_brza.move_mechanism(220)  # izbaci ruku 160
strategy3_brza.move_front_arm(95, v=30)  # 90
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(60, 0)
strategy3_brza.activate_prednja_grtalca(350, 300)  # izbacuje desnu grtalcu
strategy3_brza.end_step_actions()

strategy3_brza.set_distance_angle(0, 90, g=0.3)  # zatorira ka tanjiru
strategy3_brza.set_distance_angle(100, 0, g=0.7)  # udje u tanjur
strategy3_brza.deactivate_prednja_grtalca()

strategy3_brza.add_points("unload", 20)

# strategy3_brza.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy3_brza.move_mechanism(180)

strategy3_brza.back_all_on()

strategy3_brza.go_to_XY(1000, -1000, False, g=1.5)

strategy3_brza.go_to_XY(1500, -450, False, g=1.5)

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy3_brza.add_points("unload", 10)

strategy3_brza.all_off()

strategy3_brza.end()

# ======================alternativna strategija =============================================

strategy3_brza.skip_to_flag(1)

strategy3_brza.back_sensors_on()
strategy3_brza.front_sensors_off()

strategy3_brza.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3_brza.go_to_XY(1500, -1500, False, off=120)
strategy3_brza.add_sequence(prepare_back_arm())
strategy3_brza.deactivate_prednja_grtalca()
# strategy3_brza.move_mechanism(260)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.end_step_actions()

# strategy3_brza.rotate_to(-90)

strategy3_brza.add_sequence(grip_back_plant())

strategy3_brza.front_sensors_on()
strategy3_brza.back_sensors_off()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1300, -2000, off=100)  # dolazi do tanjira 4 -1210
strategy3_brza.add_sequence(prepare_front_arm())
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_front_plant())

strategy3_brza.front_sensors_off()
strategy3_brza.back_sensors_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1750, -762, False)  # dolazi ispred plantera
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_sensors_off()

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.go_to_XY(1850, -762)  # 1850
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(85, v=15)
strategy3_brza.ungrip_front()

strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120, v=30)
strategy3_brza.move_mechanism(180)
strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)
strategy3_brza.back_sensors_on()

strategy3_brza.set_distance_angle(-100, 0)

strategy3_brza.back_sensors_off()
strategy3_brza.front_sensors_on()

strategy3_brza.start_step_actions()  # ide na sledece biljke
strategy3_brza.go_to_XY(1300, -1000, off=120)
strategy3_brza.move_mechanism(260)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_front_plant())

# ===============================================

strategy3_brza.start_step_actions()  # podize ruku
strategy3_brza.go_to_XY(1382, -185, False)  # -285
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(170, v=15)
strategy3_brza.ungrip_back()

strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(180)
strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

strategy3_brza.back_sensors_off()
strategy3_brza.front_sensors_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(150, 0)  # dolazi ispred plantera
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_sensors_off()

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.rotate_to(-90)  # 1850
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(77, v=15)
strategy3_brza.ungrip_front()

strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.move_mechanism(180)

strategy3_brza.add_points("unload", 6)
# strategy3_brza.set_distance_angle(200, 0)
# strategy3_brza.start_step_actions()
# strategy3_brza.go_to_XY(1382, -200)
# strategy3_brza.move_front_arm(120, v=15)
# strategy3_brza.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
# strategy3_brza.end_step_actions()

# strategy3_brza.rotate_to(0)
# strategy3_brza.move_front_arm(80, v=30)


# strategy3_brza.set_distance_angle(-100, 0)
# strategy3_brza.set_distance_angle(0, -70)

# strategy3_brza.ungrip_front()

# strategy3_brza.start_parallel()
# strategy3_brza.move_front_arm(120, v=15)
# strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()


# strategy3_brza.add_points("unload", 12)

# strategy3_brza.front_sensors_on()
# strategy3_brza.back_sensors_off()
# =====================================================

strategy3_brza.start_step_actions()  # ide na sledece biljke
strategy3_brza.go_to_XY(700, -700, False)  # -700
strategy3_brza.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy3_brza.add_sequence(prepare_arms6())
strategy3_brza.end_step_actions()

# strategy3_brza.rotate_to(0)  # hvata biljke 6 komada
strategy3_brza.add_sequence(grip3_back_plant(-120))  # -120
# strategy3_brza.set_distance_angle(60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3_brza.back_sensors_off()

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.front_sensors_on()
# strategy3_brza.activate_prednja_grtalca()
strategy3_brza.set_distance_angle(230, 0)
strategy3_brza.add_sequence(grip_front_plant())  # 130
# strategy3_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3_brza.rotate_to(-90)


strategy3_brza.front_sensors_off()
strategy3_brza.back_sensors_on()

# strategy3_brza.go_to_XY(590, -600)  # ide da ih ostavi kako zna i ume
strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(590, -275, False)  # -285
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_sensors_off()

strategy3_brza.rotate_to(180)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(120)  # 180 130
strategy3_brza.move_back_arm(193, v=30)  # 170
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(100, 0)
strategy3_brza.grip_back()
strategy3_brza.end_step_actions()


strategy3_brza.move_front_arm(110, v=30)
strategy3_brza.go_to_XY(624, -325)  # 285 325
strategy3_brza.rotate_to(0)
# strategy3_brza.move_back_arm(190, v=15)
strategy3_brza.move_mechanism(220)  # izbaci ruku 160
strategy3_brza.move_front_arm(95, v=30)  # 90
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(60, 0)
strategy3_brza.activate_prednja_grtalca(350, 300)  # izbacuje desnu grtalcu
strategy3_brza.end_step_actions()

strategy3_brza.set_distance_angle(0, 90, g=0.3)  # zatorira ka tanjiru
strategy3_brza.set_distance_angle(100, 0, g=0.7)  # udje u tanjur
strategy3_brza.deactivate_prednja_grtalca()

strategy3_brza.add_points("unload", 20)

# strategy3_brza.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy3_brza.move_mechanism(180)

strategy3_brza.back_all_on()

strategy3_brza.go_to_XY(1000, -1000, False, g=1.5)

strategy3_brza.go_to_XY(1500, -450, False, g=1.5)

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy3_brza.add_points("unload", 10)

strategy3_brza.all_off()

strategy3_brza.end()

# ==========================TIMEOUT ===========================

strategy3_brza.skip_to_flag("timeout")
# strategy3_brza.skip_to_flag("skip_object")

strategy3_brza.back_sensors_on()

strategy3_brza.go_to_XY(1600, -450, False)
strategy3_brza.add_points("unload", 10)

strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120)
strategy3_brza.move_mechanism(180)
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_parallel()

strategy3_brza.all_off()

strategy3_brza.end()
