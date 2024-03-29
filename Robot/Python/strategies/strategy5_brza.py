from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, 4 seta biljaka zbog plus 5 na simu

strategy5_brza = Strategy()

strategy5_brza.rotate_to(0)
strategy5_brza.front_all_on()
strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(195, 820, g=0.4)  # rotira panele #y = 750
strategy5_brza.activate_triangle()
strategy5_brza.deactivate_prednja_grtalca()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.add_sequence(prepare_front_arm())
strategy5_brza.end_step_actions()

strategy5_brza.add_points("unload", 15)

strategy5_brza.set_skip_flag(1)

strategy5_brza.start_step_actions()
# dolazi do tanjira 4 -1210
strategy5_brza.go_to_XY(500, 1500, off=120, b=50, at=0)
strategy5_brza.deactivate_triangle()
# strategy5_brza.move_mechanism(260)
strategy5_brza.activate_prednja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.add_sequence(grip_front_plant(True))  # -20 #110

strategy5_brza.set_skip_flag(2)

strategy5_brza.front_all_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()
# 1320 ide do biljaka kod sime
strategy5_brza.go_to_XY(1500, 1500, False, off=120, at=0, b=100)
strategy5_brza.add_sequence(prepare_back_arm())
strategy5_brza.deactivate_prednja_grtalca()
# strategy5_brza.move_mechanism(100)
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

# strategy5_brza.rotate_to(90)

strategy5_brza.add_sequence(grip_back_plant(True))  # 0 #-80

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu
strategy5_brza.set_skip_flag(3)

strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(1750, 762, False, at=2, b=200,
                        bs=1)  # dolazi ispred plantera
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_off()
strategy5_brza.skip_to_flag("reset")

strategy5_brza.start_step_actions()  # dolazi i priprema ruku
strategy5_brza.go_to_XY(1850, 762, False)
strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy5_brza.end_step_actions()

strategy5_brza.move_back_arm(175, v=15)
strategy5_brza.ungrip_back()

strategy5_brza.start_parallel()
strategy5_brza.move_back_arm(210, v=30)
strategy5_brza.move_mechanism(180)
strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)
# =================================================

strategy5_brza.front_sensors_on()
# 650 # ide unapred prema sledecem planteru
strategy5_brza.set_distance_angle(100, 0)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()  # ide na sledece biljke
strategy5_brza.go_to_XY(1300, 1000, False, off=120, at=100, b=0)  # ??????
strategy5_brza.move_mechanism(100)
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.add_sequence(grip_back_plant())  # TODO: smisliti nesto pametno

# =============================================

strategy5_brza.start_step_actions()  # podize ruku
strategy5_brza.go_to_XY(1382, 185, at=100, b=200)  # -285
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy5_brza.end_step_actions()

strategy5_brza.move_front_arm(80, v=15)
strategy5_brza.ungrip_front()

# strategy5_brza.start_parallel()
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(180)
# strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-100, 0)  # dolazi ispred plantera
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_off()

strategy5_brza.start_step_actions()  # dolazi i priprema ruku
strategy5_brza.rotate_to(90)  # 1850
strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy5_brza.end_step_actions()

strategy5_brza.move_back_arm(167, v=15)
strategy5_brza.ungrip_back()

strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(180)

strategy5_brza.add_points("unload", 6)

strategy5_brza.start_step_actions()  # ide na sledece biljke
strategy5_brza.go_to_XY(700, 700, at=100, b=0)  # -700
strategy5_brza.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy5_brza.add_sequence(prepare_arms6())
strategy5_brza.end_step_actions()

# strategy5_brza.rotate_to(0)  # hvata biljke 6 komada
strategy5_brza.add_sequence(grip3_front_plant())  # -70
strategy5_brza.front_sensors_off()

strategy5_brza.start_step_actions()
strategy5_brza.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_on()
# strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.set_distance_angle(-230, 0)
strategy5_brza.add_sequence(grip_back_plant())  # 130
# strategy5_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy5_brza.rotate_to(-90)

strategy5_brza.back_sensors_off()
strategy5_brza.front_sensors_on()

strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(624, 280, at=100, b=100)  # 350
strategy5_brza.move_front_arm(120, v=15)  # podize ruku
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.front_sensors_off()
strategy5_brza.back_all_on()

strategy5_brza.rotate_to(180)
# strategy5_brza.set_distance_angle(-10, 0)
strategy5_brza.move_mechanism(265)  # 180
strategy5_brza.move_front_arm(100, v=30)  # 100
strategy5_brza.ungrip_front()
strategy5_brza.move_front_arm(120, v=30)

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-100, 0, at=100, b=0)
strategy5_brza.grip_front()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.move_back_arm(210, v=30)
strategy5_brza.end_step_actions()

strategy5_brza.back_all_off()

strategy5_brza.go_to_XY(590, 330, False)  # 285
strategy5_brza.rotate_to(0)
# strategy5_brza.move_back_arm(190, v=15)
strategy5_brza.move_mechanism(150)  # izbaci ruku
strategy5_brza.move_back_arm(180, v=30)
strategy5_brza.ungrip_back()
strategy5_brza.move_back_arm(210, v=30)

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-60, 0)
strategy5_brza.deactivate_zadnja_grtalca(60, 20)
strategy5_brza.end_step_actions()

strategy5_brza.set_distance_angle(0, -90, g=0.3)  # zatorira ka tanjiru
strategy5_brza.set_distance_angle(-100, 0, g=0.5)  # udje u tanjur
strategy5_brza.deactivate_zadnja_grtalca()


strategy5_brza.add_points("unload", 20)

# strategy5_brza.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy5_brza.move_mechanism(180)

strategy5_brza.front_all_on()

strategy5_brza.go_to_XY(1000, 1000)

strategy5_brza.go_to_XY(1500, 450)

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy5_brza.all_off()

strategy5_brza.add_points("unload", 10)

strategy5_brza.end()

# =======================alternativna strategija========

strategy5_brza.skip_to_flag(1)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()
# 1320 ide do biljaka kod sime
strategy5_brza.go_to_XY(1500, 1500, off=120, at=100, b=200)
strategy5_brza.add_sequence(prepare_front_arm())
strategy5_brza.deactivate_zadnja_grtalca()
# strategy5_brza.move_mechanism(100)
strategy5_brza.activate_prednja_grtalca()
strategy5_brza.end_step_actions()

# strategy5_brza.rotate_to(90)

strategy5_brza.add_sequence(grip_front_plant())  # 0 #-80

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()
# dolazi do tanjira 4 -1210
strategy5_brza.go_to_XY(1300, 2000, False, off=100, at=100, b=0)
strategy5_brza.add_sequence(prepare_back_arm())
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.deactivate_prednja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.set_skip_flag(2)
strategy5_brza.add_sequence(grip_back_plant(True))  # -20
strategy5_brza.set_skip_flag("reset")

# strategy5_brza.front_sensors_on()
# strategy5_brza.back_sensors_off()

# ovde skace na zaobilaznu koordinatu u alternativnoj 2

strategy5_brza.set_skip_flag(3)

strategy5_brza.start_step_actions()
# 762 # dolazi ispred plantera
strategy5_brza.go_to_XY(1700, 800, False, at=2, b=200)
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_off()
strategy5_brza.skip_to_flag("reset")

strategy5_brza.start_step_actions()  # dolazi i priprema ruku
strategy5_brza.go_to_XY(1840, 800, False)  # 1820, 762
strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy5_brza.end_step_actions()

strategy5_brza.move_back_arm(175, v=15)
strategy5_brza.ungrip_back()

strategy5_brza.start_parallel()
strategy5_brza.move_back_arm(210, v=30)
strategy5_brza.move_mechanism(180)
strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)

# ======================OVDE RAZLIKA===================

strategy5_brza.front_sensors_on()
# 650 # ide unapred prema sledecem planteru
strategy5_brza.set_distance_angle(100, 0)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()  # ide na sledece biljke
strategy5_brza.go_to_XY(1300, 1000, False, off=120, at=5, b=0)
strategy5_brza.move_mechanism(100)
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()
# TODO : ista prica kao i za onaj TODO treba nesto pametno smsliti
strategy5_brza.add_sequence(grip_back_plant())

# =============================================

strategy5_brza.start_step_actions()  # podize ruku
strategy5_brza.go_to_XY(1382, 185, at=100, b=200)  # -285
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy5_brza.end_step_actions()

strategy5_brza.move_front_arm(80, v=15)
strategy5_brza.ungrip_front()

# strategy5_brza.start_parallel()
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(180)
# strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-100, 0)  # dolazi ispred plantera
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_off()

strategy5_brza.start_step_actions()  # dolazi i priprema ruku
strategy5_brza.rotate_to(90)  # 1850
strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy5_brza.end_step_actions()

strategy5_brza.move_back_arm(167, v=15)
strategy5_brza.ungrip_back()

strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(180)

strategy5_brza.add_points("unload", 6)

strategy5_brza.start_step_actions()  # ide na sledece biljke
strategy5_brza.go_to_XY(700, 700, at=100, b=0)  # -700
strategy5_brza.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy5_brza.add_sequence(prepare_arms6())
strategy5_brza.end_step_actions()

# strategy5_brza.rotate_to(0)  # hvata biljke 6 komada
strategy5_brza.add_sequence(grip3_front_plant())  # -70
strategy5_brza.front_sensors_off()

strategy5_brza.start_step_actions()
strategy5_brza.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_sensors_on()
# strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.set_distance_angle(-230, 0)
strategy5_brza.add_sequence(grip_back_plant())  # 130
# strategy5_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy5_brza.rotate_to(-90)

strategy5_brza.back_sensors_off()
strategy5_brza.front_sensors_on()

strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(624, 280, at=100, b=200)  # 350
strategy5_brza.move_front_arm(120, v=15)  # podize ruku
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()


strategy5_brza.rotate_to(180)
# strategy5_brza.set_distance_angle(-10, 0)
strategy5_brza.move_mechanism(265)  # 220
strategy5_brza.move_front_arm(100, v=30)  # 100
strategy5_brza.ungrip_front()
strategy5_brza.move_front_arm(120, v=30)

strategy5_brza.front_sensors_off()
strategy5_brza.back_all_on()

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-100, 0)
strategy5_brza.grip_front()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.move_back_arm(210, v=30)
strategy5_brza.end_step_actions()

strategy5_brza.back_all_off()

strategy5_brza.go_to_XY(590, 330, False)  # 285
strategy5_brza.rotate_to(0)
# strategy5_brza.move_back_arm(190, v=15)
strategy5_brza.move_mechanism(150)  # izbaci ruku
strategy5_brza.move_back_arm(180, v=30)
strategy5_brza.ungrip_back()
strategy5_brza.move_back_arm(210, v=30)

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(-60, 0)
strategy5_brza.deactivate_zadnja_grtalca(60, 20)
strategy5_brza.end_step_actions()

strategy5_brza.add_points("unload", 20)

strategy5_brza.set_distance_angle(0, -90, g=0.3)  # zatorira ka tanjiru
strategy5_brza.set_distance_angle(-100, 0, g=0.5)  # udje u tanjur
strategy5_brza.deactivate_zadnja_grtalca()


# strategy5_brza.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy5_brza.move_mechanism(180)

strategy5_brza.front_all_on()

strategy5_brza.go_to_XY(1000, 1000, at=0, b=0)

strategy5_brza.go_to_XY(1500, 450, at=100, b=0)

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy5_brza.add_points("unload", 10)

strategy5_brza.all_off()

strategy5_brza.end()

# ========================grananje 2===============
# ============================brze, 6 manje, valjda pouzdanije===============

strategy5_brza.skip_to_flag(2)
# strategy5_brza.skip_to_flag("skip_object")

strategy5_brza.front_all_off()
strategy5_brza.back_sensors_on()

strategy5_brza.start_step_actions()
# 1320 ide do biljaka kod sime
strategy5_brza.go_to_XY(700, 2000, False, off=120, at=100, b=0)
strategy5_brza.add_sequence(prepare_back_arm())
strategy5_brza.deactivate_prednja_grtalca()
# strategy5_brza.move_mechanism(100)
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.add_sequence(grip_back_plant())

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
strategy5_brza.skip_to_flag(3)

strategy5_brza.back_sensors_off()
strategy5_brza.front_all_on()

strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(1050, 600, at=0, b=0)
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.front_all_off()
strategy5_brza.back_all_on()

# 762 # dolazi ispred plantera
strategy5_brza.go_to_XY(1700, 750, False, at=100, b=0)


strategy5_brza.start_step_actions()  # dolazi i priprema ruku
strategy5_brza.go_to_XY(1840, 750, False, at=100, b=0)  # 1820, 762
strategy5_brza.move_back_arm(210, v=15)
strategy5_brza.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy5_brza.end_step_actions()

strategy5_brza.move_back_arm(175, v=15)
strategy5_brza.ungrip_back()

strategy5_brza.start_parallel()
strategy5_brza.move_back_arm(210, v=30)
strategy5_brza.move_mechanism(180)
strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)

# ======================OVDE RAZLIKA===================
strategy5_brza.front_all_on()
strategy5_brza.set_distance_angle(100, 0)
strategy5_brza.go_to_XY(1382, 700, at=100, b=0)

# =====================================================

strategy5_brza.start_step_actions()  # podize ruku
strategy5_brza.go_to_XY(1382, 210, at=100, b=200)  # 185
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy5_brza.end_step_actions()

strategy5_brza.move_front_arm(80, v=15)
strategy5_brza.ungrip_front()

# strategy5_brza.start_parallel()
strategy5_brza.move_front_arm(120, v=15)
strategy5_brza.move_mechanism(180)
# strategy5_brza.end_parallel()

strategy5_brza.add_points("unload", 24)

strategy5_brza.front_sensors_off()
strategy5_brza.back_sensors_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========

# 650 # ide unatrrag prema sledecem tanjiru
strategy5_brza.set_distance_angle(-100, 0)

strategy5_brza.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy5_brza.go_to_XY(1300, 700, False, at=100, b=0)
strategy5_brza.move_mechanism(180)
strategy5_brza.activate_zadnja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.rotate_to(180)
strategy5_brza.add_sequence(grip3_back_plant(-110))

strategy5_brza.start_step_actions()
strategy5_brza.rotate_to(0)
strategy5_brza.activate_prednja_grtalca()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy5_brza.back_all_off()
strategy5_brza.front_all_on()

strategy5_brza.set_distance_angle(230, 0)
strategy5_brza.move_mechanism(180)
strategy5_brza.add_sequence(grip_front_plant())  # -70

# strategy5_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy5_brza.rotate_to(-90)

strategy5_brza.front_all_off()
strategy5_brza.back_all_on()

strategy5_brza.start_step_actions()
strategy5_brza.go_to_XY(1552, 280, False, at=100, b=200)  # 350
strategy5_brza.move_back_arm(210, v=15)  # podize ruku
strategy5_brza.deactivate_prednja_grtalca()
strategy5_brza.end_step_actions()

strategy5_brza.back_all_off()

strategy5_brza.rotate_to(0)
# strategy5_brza.set_distance_angle(-10, 0)
strategy5_brza.move_mechanism(140)  # 220
strategy5_brza.move_back_arm(190, v=30)  # 100
strategy5_brza.ungrip_back()
strategy5_brza.move_back_arm(210, v=30)

strategy5_brza.back_all_off()
strategy5_brza.front_all_on()

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(200, 0, at=100, b=0)
strategy5_brza.grip_back()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_step_actions()


strategy5_brza.move_front_arm(120, v=30)
strategy5_brza.go_to_XY(1312, 280)  # 285
strategy5_brza.rotate_to(180)
strategy5_brza.move_mechanism(220)  # izbaci ruku
strategy5_brza.move_front_arm(100, v=30)
strategy5_brza.ungrip_front()
strategy5_brza.move_front_arm(120, v=30)

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(60, 0)
strategy5_brza.deactivate_prednja_grtalca(340, 300)
strategy5_brza.end_step_actions()

strategy5_brza.add_points("unload", 20)

strategy5_brza.set_distance_angle(0, 90, g=0.3)  # zatorira ka tanjiru

strategy5_brza.start_step_actions()
strategy5_brza.set_distance_angle(200, 0, g=0.7)  # udje u tanjur
strategy5_brza.deactivate_prednja_grtalca()
strategy5_brza.end_step_actions()


# strategy5_brza.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy5_brza.move_mechanism(180)

# strategy5_brza.back_all_on()
strategy5_brza.all_off()

strategy5_brza.go_to_XY(1600, 250, g=0.5)

# strategy5_brza.go_to_XY(1500, 500)

# 10 sto se vratio robot i 6 poena zbog 3 resistant koje je zgrnuo
strategy5_brza.add_points("unload", 10)


strategy5_brza.end()


# ==========================TIMEOUT ===========================

strategy5_brza.skip_to_flag("timeout")

strategy5_brza.front_all_on()

strategy5_brza.go_to_XY(1620, 250, at=100, b=0, bs=0.1, s=0.1)
strategy5_brza.add_points("unload", 10)

strategy5_brza.start_parallel()
strategy5_brza.move_front_arm(120)
strategy5_brza.move_mechanism(180)
strategy5_brza.deactivate_prednja_grtalca()
strategy5_brza.deactivate_zadnja_grtalca()
strategy5_brza.end_parallel()


strategy5_brza.all_off()

strategy5_brza.end()
