from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Plava strana 3 solarnih, 4 seta biljaka zbog plus 5 na sime

strategy3_brza = Strategy()

strategy3_brza.all_off()
strategy3_brza.rotate_to(0)

strategy3_brza.back_sensors_on()
strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(195, -800, False, g=0.4)  # rotira panele #y = 750
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

strategy3_brza.add_sequence(grip_back_plant(True))  # -20

strategy3_brza.set_skip_flag(2)  # u slucaju da sretnemo nekoga prekoputa

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3_brza.go_to_XY(1500, -1500, off=100, at=0, b=100)  # off = 120
strategy3_brza.add_sequence(prepare_front_arm())
strategy3_brza.deactivate_zadnja_grtalca()
# strategy3_brza.move_mechanism(260)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_front_plant(True))

# strategy3_brza.rotate_to(-90)

# ovo sluzi da pokusa da zaobidje time sto ode na zaobilaznu koordinatu u alternativnoj 2
strategy3_brza.set_skip_flag(3)

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1800, -730, at=2, b=200,
                        bs=1)  # dolazi ispred plantera 1750
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.skip_to_flag("reset")

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.go_to_XY(1850, -730)  # 1850
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.move_front_arm(85, v=15)
strategy3_brza.ungrip_front()

# strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120, v=30)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

# ======================================================================

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1382, -700, False, at=100, b=0)
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.start_step_actions()  # podize ruku
strategy3_brza.go_to_XY(1382, -190, False, at=100, b=200)  # -185
strategy3_brza.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(170, v=15)
strategy3_brza.ungrip_back()

# strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========
# 650 # ide unatrrag prema sledecem tanjiru
strategy3_brza.set_distance_angle(100, 0)

strategy3_brza.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy3_brza.go_to_XY(1300, -700, at=100, b=0)
strategy3_brza.move_mechanism(180)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(180)
# odavde skace na sledece ide na sledece ako ovih nema
strategy3_brza.set_skip_flag(4)
strategy3_brza.add_sequence(grip3_front_plant(0, True))
strategy3_brza.skip_to_flag("reset")

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(0)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.set_distance_angle(-230, 0)
strategy3_brza.move_mechanism(180)
strategy3_brza.add_sequence(grip_back_plant(-130))  # -70

# ako vidi nekoga odustaje i ide da ostavi biljke nazad
strategy3_brza.set_skip_flag(5)

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1000, -1500, False, at=0, b=0)  # pa na jos 6 komada
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(450, -450, at=100, b=0)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.move_front_arm(120)
strategy3_brza.move_mechanism(180)
strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 6)

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1300, -650, False, at=100, b=0)
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.skip_to_flag(5)  # do ovde dolazi

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1542, -270, at=100, b=200)  # 350
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.rotate_to(0)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(230)  # 220
strategy3_brza.move_front_arm(100, v=30)  # 100
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-200, 0, at=100, b=0)
strategy3_brza.grip_front()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.go_to_XY(1312, -270, False)  # 285
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(130)  # izbaci ruku
strategy3_brza.move_back_arm(190, v=30)
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-60, 0)
strategy3_brza.activate_zadnja_desna_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 20)

strategy3_brza.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.all_off()

strategy3_brza.end()

# ======================alternativna strategija =============================================

strategy3_brza.skip_to_flag(1)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
# off = 60 # 1320 ide do biljaka kod sime  ...posl 1270
strategy3_brza.go_to_XY(1500, -1500, False, off=120, at=100, b=200)
strategy3_brza.add_sequence(prepare_back_arm())
strategy3_brza.deactivate_prednja_grtalca()
# strategy3_brza.move_mechanism(260)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.end_step_actions()

# strategy3_brza.rotate_to(-90)

strategy3_brza.add_sequence(grip_back_plant())

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1300, -2000, off=100, at=100,
                        b=0)  # dolazi do tanjira 4 -1210
strategy3_brza.add_sequence(prepare_front_arm())
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.set_skip_flag(2)
strategy3_brza.add_sequence(grip_front_plant(True))
strategy3_brza.set_skip_flag("reset")

# strategy3_brza.front_all_off()
# strategy3_brza.back_all_on()
# ovde skace na zaobilaznu koordinatu u alternativnoj 2

strategy3_brza.set_skip_flag(3)


strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1800, -730, at=2, b=200,
                        bs=1)  # dolazi ispred plantera 1750

strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(-90)

strategy3_brza.front_all_off()
strategy3_brza.skip_to_flag("reset")
# strategy3_brza.rotate_to(-90)

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.set_distance_angle(50, 0)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(85, v=15)
strategy3_brza.ungrip_front()

# strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120, v=30)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

# ========================================================

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1382, -700, False, at=100, b=0)
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.start_step_actions()  # podize ruku
strategy3_brza.go_to_XY(1382, -200, False, at=100, b=200)  # -185
strategy3_brza.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(170, v=15)
strategy3_brza.ungrip_back()

# strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)


# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========
# 650 # ide unatrrag prema sledecem tanjiru
strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.set_distance_angle(100, 0)

strategy3_brza.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy3_brza.go_to_XY(1300, -700, at=100, b=0)
strategy3_brza.move_mechanism(180)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(180)
strategy3_brza.add_sequence(grip3_front_plant())

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(0)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.set_distance_angle(-230, 0)
strategy3_brza.move_mechanism(180)
strategy3_brza.add_sequence(grip_back_plant(-130))  # -70

# strategy3_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3_brza.rotate_to(-90)

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1542, -270, at=100, b=200)  # 350
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.rotate_to(0)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(230)  # 220
strategy3_brza.move_front_arm(100, v=30)  # 100
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-200, 0, at=100, b=0)
strategy3_brza.grip_front()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.go_to_XY(1312, -270, False)  # 285
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(130)  # izbaci ruku
strategy3_brza.move_back_arm(190, v=30)
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-60, 0)
strategy3_brza.activate_zadnja_desna_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 20)

strategy3_brza.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.all_off()

strategy3_brza.end()

# ========================grananje 2===============
# ============================brze, 6 manje, valjda pouzdanije===============

strategy3_brza.skip_to_flag(2)
# strategy3_brza.skip_to_flag("skip_object")

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(700, -2000, off=120, at=100, b=0)
strategy3_brza.add_sequence(prepare_front_arm())
strategy3_brza.deactivate_zadnja_grtalca()
# strategy3_brza.move_mechanism(100)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.add_sequence(grip_front_plant())

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
strategy3_brza.skip_to_flag(3)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1050, -600, False, at=0, b=0)
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1800, -730, at=2, b=200,
                        bs=1)  # dolazi ispred plantera 1750
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.move_front_arm(120, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(-90)
strategy3_brza.skip_to_flag("reset")

strategy3_brza.front_all_off()

strategy3_brza.start_step_actions()  # dolazi i priprema ruku
strategy3_brza.set_distance_angle(50, 0)
strategy3_brza.move_mechanism(270)  # ostavlja zadnje u planter bez saksija
strategy3_brza.end_step_actions()

strategy3_brza.move_front_arm(85, v=15)
strategy3_brza.ungrip_front()

# strategy3_brza.start_parallel()
strategy3_brza.move_front_arm(120, v=30)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)

# ===============================================

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1382, -700, False, at=100, b=200)
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.end_step_actions()

strategy3_brza.start_step_actions()  # podize ruku
strategy3_brza.go_to_XY(1382, -200, False, at=100, b=200)  # -185
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(170, v=15)
strategy3_brza.ungrip_back()

# strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=15)
strategy3_brza.move_mechanism(180)
# strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 24)


# =======OVAJ DEO MOZE DA SE DORADI JER ONI METALI MOGU DA SE ISKORISTE========
# 650 # ide unatrrag prema sledecem tanjiru

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.set_distance_angle(100, 0)

strategy3_brza.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy3_brza.go_to_XY(1300, -700, at=100, b=0)
strategy3_brza.move_mechanism(180)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(180)
strategy3_brza.add_sequence(grip3_front_plant())

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(0)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.set_distance_angle(-230, 0)
strategy3_brza.move_mechanism(180)
strategy3_brza.add_sequence(grip_back_plant(-130))  # -70

# strategy3_brza.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy3_brza.rotate_to(-90)

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1542, -270, at=100, b=200)  # 350
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.rotate_to(0)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(230)  # 220
strategy3_brza.move_front_arm(100, v=30)  # 100
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-200, 0, at=100, b=0)
strategy3_brza.grip_front()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.go_to_XY(1312, -270, False)  # 285
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(130)  # izbaci ruku
strategy3_brza.move_back_arm(190, v=30)
strategy3_brza.ungrip_back()

strategy3_brza.start_parallel()
strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.activate_zadnja_desna_grtalca()
strategy3_brza.end_parallel()

strategy3_brza.add_points("unload", 20)

strategy3_brza.set_distance_angle(-60, 0)


strategy3_brza.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.all_off()

strategy3_brza.end()


# ============traganje za biljakama na kraju strategija============
strategy3_brza.skip_to_flag(4)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(700, -700, False, at=100, b=0)
strategy3_brza.add_sequence(prepare_arms6())
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(180)
strategy3_brza.activate_prednja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.set_skip_flag(6)
strategy3_brza.add_sequence(grip3_front_plant(0, True))
strategy3_brza.skip_to_flag("reset")

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(0)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.set_distance_angle(-230, 0)
strategy3_brza.move_mechanism(180)
strategy3_brza.add_sequence(grip_back_plant(-130))


# ==========================univerzalni kraj=======================
strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1542, -270, at=100, b=200)  # 350
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.rotate_to(0)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(230)  # 220
strategy3_brza.move_front_arm(100, v=30)  # 100
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-200, 0, at=100, b=0)
strategy3_brza.grip_front()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.go_to_XY(1312, -270, False)  # 285
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(130)  # izbaci ruku
strategy3_brza.move_back_arm(190, v=30)
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-60, 0)

strategy3_brza.activate_zadnja_desna_grtalca()

strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 20)

strategy3_brza.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru
# strategy3_brza.rotate_to(90)
strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
# strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(200)

strategy3_brza.all_off()


strategy3_brza.end()
# ================traganje za biljkama dalje.... ako malo pre nije nasao ===================

strategy3_brza.skip_to_flag(6)

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(700, -1700, at=100, b=0)
strategy3_brza.add_sequence(prepare_arms6())
strategy3_brza.end_step_actions()

strategy3_brza.rotate_to(180)

strategy3_brza.set_skip_flag(7)
strategy3_brza.add_sequence(grip3_front_plant(0, True))
strategy3_brza.skip_to_flag("reset")

strategy3_brza.start_step_actions()
strategy3_brza.rotate_to(0)
strategy3_brza.activate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.set_distance_angle(-230, 0)
strategy3_brza.move_mechanism(180)
strategy3_brza.add_sequence(grip_back_plant(-130))

# ==========================univerzalni kraj=======================

strategy3_brza.back_all_off()
strategy3_brza.front_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.go_to_XY(1542, -270, at=100, b=200)  # 350
strategy3_brza.move_front_arm(120, v=15)  # podize ruku
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.front_all_off()

strategy3_brza.rotate_to(0)
# strategy3_brza.set_distance_angle(-10, 0)
strategy3_brza.move_mechanism(230)  # 220
strategy3_brza.move_front_arm(100, v=30)  # 100
strategy3_brza.ungrip_front()
strategy3_brza.move_front_arm(120, v=30)

strategy3_brza.back_all_on()

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-200, 0, at=100, b=0)
strategy3_brza.grip_front()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_step_actions()


strategy3_brza.move_back_arm(210, v=30)
strategy3_brza.go_to_XY(1312, -270, False)  # 285
strategy3_brza.rotate_to(180)
strategy3_brza.move_mechanism(130)  # izbaci ruku
strategy3_brza.move_back_arm(190, v=30)
strategy3_brza.ungrip_back()
strategy3_brza.move_back_arm(210, v=30)

strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-60, 0)

strategy3_brza.activate_zadnja_desna_grtalca()

strategy3_brza.end_step_actions()

strategy3_brza.add_points("unload", 20)

strategy3_brza.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru
# strategy3_brza.rotate_to(90)
strategy3_brza.start_step_actions()
strategy3_brza.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
# strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.end_step_actions()

strategy3_brza.move_back_arm(200)

strategy3_brza.all_off()


strategy3_brza.end()

# ===============ako nista nije nasao :(==============
strategy3_brza.skip_to_flag(7)

strategy3_brza.front_all_off()
strategy3_brza.back_all_on()

strategy3_brza.go_to_XY(1550, -250, False, at=100, b=0, bs=0.1, s=0.1)
# ==========================TIMEOUT ===========================

strategy3_brza.skip_to_flag("timeout")
# strategy3_brza.skip_to_flag("skip_object")

strategy3_brza.back_all_on()

strategy3_brza.go_to_XY(1650, -200, False, at=100, b=0, bs=0.1, s=0.1)
# strategy3_brza.add_points("unload", 10)

strategy3_brza.start_parallel()
strategy3_brza.ungrip_back()
strategy3_brza.ungrip_front()
strategy3_brza.move_back_arm(210)
strategy3_brza.move_mechanism(180)
strategy3_brza.deactivate_zadnja_grtalca()
strategy3_brza.deactivate_prednja_grtalca()
strategy3_brza.end_parallel()

strategy3_brza.all_off()

strategy3_brza.end()
