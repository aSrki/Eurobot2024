from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Plava strana 3 solarnih, 4 seta biljaka zbog plus 5 na sime

strategy3 = Strategy()

strategy3.rotate_to(0)
strategy3.back_all_on()
strategy3.start_step_actions()
strategy3.go_to_XY(195, -830, False, g=0.4)  # rotira panele #y = 750
strategy3.activate_triangle()
strategy3.deactivate_prednja_grtalca()
strategy3.deactivate_zadnja_grtalca()
strategy3.add_sequence(prepare_back_arm())  # priprema za hvatanje
strategy3.end_step_actions()

strategy3.add_points("unload", 15)

# ako detektuje idemo prekoputa, ova strategija se nalazi na kraju
strategy3.set_skip_flag(1)

strategy3.start_step_actions()
strategy3.go_to_XY(500, -1500, False, off=120, b=50,
                   at=0)  # dolazi do tanjira 4 -1210
strategy3.deactivate_triangle()
strategy3.activate_zadnja_grtalca()
strategy3.end_step_actions()

strategy3.add_sequence(grip_back_plant())  # -20

strategy3.skip_to_flag(2)  # u slucaju da sretnemo nekoga prekoputa

strategy3.back_sensors_off()
strategy3.front_sensors_on()

strategy3.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3.go_to_XY(1500, -1500, off=120)
strategy3.add_sequence(prepare_front_arm())
strategy3.deactivate_zadnja_grtalca()
# strategy3.move_mechanism(260)
strategy3.activate_prednja_grtalca()
strategy3.end_step_actions()

strategy3.skip_to_flag("reset")  # gasenje flag-a

# strategy3.rotate_to(-90)

strategy3.add_sequence(grip_front_plant())

strategy3.start_step_actions()
strategy3.go_to_XY(1750, -762)  # dolazi ispred plantera
strategy3.deactivate_prednja_grtalca()
strategy3.end_step_actions()

strategy3.front_sensors_off()

strategy3.start_step_actions()  # dolazi i priprema ruku
strategy3.go_to_XY(1820, -762, False)  # 1850
strategy3.move_back_arm(210, v=15)
strategy3.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy3.end_step_actions()

strategy3.move_back_arm(175, v=15)
strategy3.ungrip_back()

strategy3.start_parallel()
strategy3.move_back_arm(210, v=15)
strategy3.move_mechanism(180)
strategy3.end_parallel()

strategy3.add_points("unload", 24)

strategy3.front_sensors_on()
strategy3.go_to_XY(1382, -650)  # ide unapred prema sledecem planteru

strategy3.start_step_actions()  # podize ruku
strategy3.go_to_XY(1382, -185)  # -285
strategy3.move_front_arm(120, v=15)
strategy3.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy3.end_step_actions()

strategy3.move_front_arm(77, v=15)
strategy3.ungrip_front()

strategy3.start_parallel()
strategy3.move_front_arm(120, v=30)
strategy3.move_mechanism(180)
strategy3.end_parallel()

strategy3.add_points("unload", 24)

strategy3.front_sensors_off()
strategy3.back_sensors_on()

strategy3.start_step_actions()  # ide na sledece biljke
strategy3.go_to_XY(1300, -700, False)  # -700
strategy3.rotate_to(3)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy3.add_sequence(prepare_arms6())
strategy3.end_step_actions()

# strategy3.rotate_to(0)  # hvata biljke 6 komada
strategy3.add_sequence(grip3_back_plant(-120))  # -120
# strategy3.set_distance_angle(60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3.back_sensors_off()

strategy3.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA


strategy3.front_sensors_on()
strategy3.activate_prednja_grtalca()
strategy3.set_distance_angle(230, 0)
strategy3.add_sequence(grip_front_plant())  # 130
# strategy3.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3.rotate_to(-90)

strategy3.front_sensors_off()
strategy3.back_sensors_on()

strategy3.go_to_XY(590, -600, False)  # ide da ih ostavi kako zna i ume
strategy3.start_step_actions()
strategy3.go_to_XY(590, -285, False)  # 350
strategy3.move_back_arm(210, v=15)  # podize ruku
strategy3.end_step_actions()

strategy3.back_sensors_off()

strategy3.rotate_to(180)
# strategy3.set_distance_angle(-10, 0)
strategy3.move_mechanism(140)  # 180 130
strategy3.move_back_arm(190, v=30)  # 170
strategy3.ungrip_back()
strategy3.move_back_arm(200, v=30)

strategy3.start_step_actions()
strategy3.set_distance_angle(100, 0)
strategy3.grip_back()
strategy3.activate_prednja_grtalca(350, 340)  # izbacuje desnu grtalcu
strategy3.end_step_actions()


strategy3.move_front_arm(110, v=30)
strategy3.go_to_XY(624, -300)  # 285 325
strategy3.rotate_to(0)
# strategy3.move_back_arm(190, v=15)
strategy3.move_mechanism(160)  # izbaci ruku 170
strategy3.move_front_arm(90, v=30)  # 90
strategy3.ungrip_front()
strategy3.move_front_arm(120, v=30)

strategy3.set_distance_angle(50, 0)
strategy3.set_distance_angle(0, 90, g=0.3)  # zatorira ka tanjiru
strategy3.set_distance_angle(100, 0, g=0.5)  # udje u tanjur
strategy3.deactivate_prednja_grtalca()
strategy3.set_distance_angle(-100, 0)

strategy3.add_points("unload", 20)

# strategy3.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy3.move_mechanism(180)

strategy3.back_sensors_on()

strategy3.start_step_actions()
strategy3.go_to_XY(700, -1000, False, off=120)
strategy3.activate_zadnja_grtalca()
strategy3.move_mechanism(80)
strategy3.end_step_actions()

strategy3.move_back_arm(165, v=30)
strategy3.add_points("unload", 6)

strategy3.start_step_actions()
strategy3.go_to_XY(1500, -400, False)
strategy3.move_back_arm(210, v=2)
strategy3.end_step_actions()

strategy3.start_parallel()
strategy3.move_mechanism(180)
strategy3.deactivate_zadnja_grtalca()
strategy3.end_parallel()

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy3.add_points("unload", 10)

strategy3.all_off()

strategy3.end()

# ======================alternativna strategija =============================================

strategy3.skip_to_flag(1)

strategy3.back_sensors_on()
strategy3.front_sensors_off()

strategy3.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3.go_to_XY(1500, -1500, False, off=120)
strategy3.add_sequence(prepare_back_arm())
strategy3.deactivate_prednja_grtalca()
# strategy3.move_mechanism(260)
strategy3.activate_zadnja_grtalca()
strategy3.end_step_actions()

# strategy3.rotate_to(-90)

strategy3.add_sequence(grip_back_plant())

strategy3.front_sensors_on()
strategy3.back_sensors_off()

strategy3.start_step_actions()
strategy3.go_to_XY(1300, -2000, off=100)  # dolazi do tanjira 4 -1210
strategy3.add_sequence(prepare_front_arm())
strategy3.deactivate_zadnja_grtalca()
strategy3.activate_prednja_grtalca()
strategy3.end_step_actions()

strategy3.add_sequence(grip_front_plant())  # -20

strategy3.front_sensors_off()
strategy3.back_sensors_on()

strategy3.start_step_actions()
strategy3.go_to_XY(1750, -762, False)  # dolazi ispred plantera
strategy3.deactivate_prednja_grtalca()
strategy3.end_step_actions()

strategy3.back_sensors_off()

strategy3.start_step_actions()  # dolazi i priprema ruku
strategy3.go_to_XY(1850, -762, False)  # 1850
strategy3.move_back_arm(210, v=15)
strategy3.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy3.end_step_actions()

strategy3.move_back_arm(175, v=15)
strategy3.ungrip_back()

strategy3.start_parallel()
strategy3.move_back_arm(210, v=30)
strategy3.move_mechanism(180)
strategy3.end_parallel()

strategy3.add_points("unload", 24)

strategy3.front_sensors_on()
strategy3.go_to_XY(1382, -650)  # ide unapred prema sledecem planteru

strategy3.start_step_actions()  # podize ruku
strategy3.go_to_XY(1382, -185)  # -285
strategy3.move_front_arm(120, v=15)
strategy3.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy3.end_step_actions()

strategy3.move_front_arm(77, v=15)
strategy3.ungrip_front()

strategy3.start_parallel()
strategy3.move_front_arm(120, v=30)
strategy3.move_mechanism(180)
strategy3.end_parallel()

strategy3.add_points("unload", 24)

strategy3.front_sensors_off()
strategy3.back_sensors_on()

strategy3.start_step_actions()  # ide na sledece biljke
strategy3.go_to_XY(1300, -700, False)  # -700
strategy3.rotate_to(3)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy3.add_sequence(prepare_arms6())
strategy3.end_step_actions()

# strategy3.rotate_to(0)  # hvata biljke 6 komada
strategy3.add_sequence(grip3_back_plant(-120))  # -120
# strategy3.set_distance_angle(60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy3.back_sensors_off()

strategy3.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA


strategy3.front_sensors_on()
strategy3.activate_prednja_grtalca()
strategy3.set_distance_angle(230, 0)
strategy3.add_sequence(grip_front_plant())  # 130
# strategy3.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3.rotate_to(-90)

strategy3.front_sensors_off()
strategy3.back_sensors_on()

strategy3.go_to_XY(624, -600, False)  # ide da ih ostavi kako zna i ume
strategy3.start_step_actions()
strategy3.go_to_XY(624, -285, False)  # 350
strategy3.move_back_arm(210, v=15)  # podize ruku
strategy3.end_step_actions()

strategy3.back_sensors_off()

strategy3.rotate_to(180)
# strategy3.set_distance_angle(-10, 0)
strategy3.move_mechanism(140)  # 180 130
strategy3.move_back_arm(190, v=30)  # 170
strategy3.ungrip_back()
strategy3.move_back_arm(200, v=30)

strategy3.start_step_actions()
strategy3.set_distance_angle(100, 0)
strategy3.grip_back()
strategy3.deactivate_prednja_grtalca()  # izbacuje desnu grtalcu
strategy3.move_front_arm(110, v=30)
strategy3.end_step_actions()


strategy3.go_to_XY(590, -330)  # 285 325
strategy3.rotate_to(0)
# strategy3.move_back_arm(190, v=15)
# bilo 160 kada je prethodni GOTO bio na 300 po Y # izbaci ruku 170
strategy3.move_mechanism(210)
strategy3.move_front_arm(90, v=30)  # 90
strategy3.ungrip_front()
strategy3.move_front_arm(120, v=30)

strategy3.activate_prednja_grtalca(350, 340)
strategy3.set_distance_angle(80, 0)
strategy3.set_distance_angle(0, 90, g=0.3)  # zatorira ka tanjiru
strategy3.set_distance_angle(100, 0, g=0.5)  # udje u tanjur
strategy3.deactivate_prednja_grtalca()

strategy3.add_points("unload", 20)

strategy3.set_distance_angle(-100, 0)
# strategy3.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy3.move_mechanism(180)

strategy3.back_sensors_on()

strategy3.start_step_actions()
strategy3.go_to_XY(700, -1000, False, off=120)
strategy3.activate_zadnja_grtalca()
strategy3.move_mechanism(80)
strategy3.end_step_actions()

strategy3.move_back_arm(165, v=30)
strategy3.add_points("unload", 6)

strategy3.start_step_actions()
strategy3.go_to_XY(1500, -300, False)
strategy3.move_back_arm(210, v=2)
strategy3.end_step_actions()

strategy3.start_parallel()
strategy3.move_mechanism(180)
strategy3.deactivate_zadnja_grtalca()
strategy3.end_parallel()

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy3.all_off()

strategy3.add_points("unload", 10)

strategy3.end()

# ==========================TIMEOUT ===========================

strategy3.skip_to_flag("timeout")
# strategy3.skip_to_flag("skip_object")

strategy3.back_sensors_on()

strategy3.go_to_XY(1600, -300, False)

strategy3.start_parallel()
strategy3.move_back_arm(210)
strategy3.move_mechanism(180)
strategy3.deactivate_zadnja_grtalca()
strategy3.end_parallel()
strategy3.add_points("unload", 10)

strategy3.all_off()

strategy3.end()
