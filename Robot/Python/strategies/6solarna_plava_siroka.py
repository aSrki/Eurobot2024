from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# plava strana 3 solarna, pasivna odnosno osnovna

strategy_plava_FULL = Strategy()
# idemo na panele
strategy_plava_FULL.rotate_to(0)
strategy_plava_FULL.set_skip_flag("odma")
strategy_plava_FULL.back_sensors_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(195, -1850, False, at=0, ts=0.5)  # rotira panele
strategy_plava_FULL.activate_triangle()
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120)
strategy_plava_FULL.add_sequence(prepare_back_arm())
strategy_plava_FULL.end_step_actions()


strategy_plava_FULL.skip_to_flag("odma")
strategy_plava_FULL.deactivate_triangle()
strategy_plava_FULL.add_points("unload", 15)  # ispisuje poene za panele

# dize zastavu koja ga baca na prvi tanjir (srednji tanjir kod sima)
strategy_plava_FULL.set_skip_flag(1)
# ako detektuje nekog ili ako ne bude biljaka na cetvrtom (srednjem kod panela) tanjiru


# provjerava da li je pokupio biljke na prvom tanjiru
strategy_plava_FULL.add_sequence(blue_get_4_back(True))

# u slucaju da sretnemo nekoga dok ide do tanjira kod sima
strategy_plava_FULL.set_skip_flag(2)
# skocice ako ne nadje biljke na fleg 2 to jest na peti tanjir

strategy_plava_FULL.add_sequence(blue_get_1_front(True))

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu da bi mogao doci do prvog plentera
strategy_plava_FULL.set_skip_flag("zaobilazak")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -780, at=2, b=200,
                             bs=1)  # dolazi ispred prvog plantera , plenter kod sima
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-95)
strategy_plava_FULL.front_all_off()
strategy_plava_FULL.skip_to_flag("reset")

# ostavlja zadnje u planter kod sima
strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(50, 0)
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()


strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

# ===========================================================

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

# ostavlja biljke u drugi plenter i ravna limove da bi posle mogao da ubaci po 5 biljaka u njih
strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -185, False, at=100, b=200)
strategy_plava_FULL.move_mechanism(20)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

# =======dio koji sluzi za ostavljanje 5 biljaka u metale i rotiranje biljaka u potovima tj svrsetak========

# ide unaprijed prema drugom tanjiru
strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.start_step_actions()  # ide na sledece biljke 3 pa 3
strategy_plava_FULL.go_to_XY(1300, -700, at=100,
                             b=50)  # dolazi do drugog tanjira
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)

# odavde skace na trece biljke ako nema ovih
strategy_plava_FULL.set_skip_flag(4)

# provjerava da li ima biljak na drugom krugu
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
# i hvata tri biljke zadnjim dijelom ako ima biljaka
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-3)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
# hvata druge tri biljke prednjim dijelom,
strategy_plava_FULL.add_sequence(grip_back_plant())
# ne provjerava jer ako su bile tu prve tri bice i druge

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
# dolazi blizu metala po istom iksu kako bi ostavio 5 biljaka u njih
strategy_plava_FULL.go_to_XY(1542, -650, at=100, b=50)
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()


# stavlja fleg u kojem ako detektuje nekog ide na tri biljke u lim a ne 5
strategy_plava_FULL.set_skip_flag("brzi_istovar")
# ili ako je proslo 74 sekunde ide na 3 biljke u lim a ne 5
strategy_plava_FULL.check_time(72, "brzi_istovar")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1542, -265, at=100, b=200)  # 350
strategy_plava_FULL.move_front_arm(120, v=15)  # podize ruku
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.rotate_to(0)
# strategy_plava_FULL.set_distance_angle(-10, 0)
strategy_plava_FULL.move_mechanism(230)  # 220
strategy_plava_FULL.move_front_arm(100, v=30)  # 100
strategy_plava_FULL.ungrip_front()
strategy_plava_FULL.move_front_arm(120, v=30)

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(-200, 0, at=100, b=50)
strategy_plava_FULL.grip_front()
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(210, v=30)
strategy_plava_FULL.go_to_XY(1312, -270, False, at=100, b=50)  # 285
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(130)  # izbaci ruku
strategy_plava_FULL.move_back_arm(190, v=30)
strategy_plava_FULL.ungrip_back()
strategy_plava_FULL.move_back_arm(210, v=30)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(-60, 0)
strategy_plava_FULL.activate_zadnja_desna_grtalca()
strategy_plava_FULL.end_step_actions()

# dodaje bodove za pet biljaka u limove
strategy_plava_FULL.add_points("unload", 20)

strategy_plava_FULL.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(-300, 0, g=0.5)  # udje u tanjur
# strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.all_off()

strategy_plava_FULL.end()

# =======================   alternativna strategija 1   =========================================================================

strategy_plava_FULL.skip_to_flag(1)
strategy_plava_FULL.set_skip_flag(15)

strategy_plava_FULL.add_sequence(blue_get_1_back(True))

strategy_plava_FULL.skip_to_flag("reset")
strategy_plava_FULL.set_skip_flag(13)

strategy_plava_FULL.add_sequence(blue_get_6_front(True))
strategy_plava_FULL.skip_to_flag("reset")

# ovde skace na zaobilaznu koordinatu u alternativnoj 2
strategy_plava_FULL.set_skip_flag("zaobilazak")

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()
strategy_plava_FULL.start_step_actions()
# 762 # dolazi ispred plantera
strategy_plava_FULL.go_to_XY(1800, -730, False, at=2, b=200, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)

strategy_plava_FULL.back_all_off()

strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter


strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.set_skip_flag(8)

strategy_plava_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_plava_FULL.go_to_XY(1300, -700, at=100, b=50)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-3)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ========================alternativna strategija 2 ako je dosao sa tanjira br.1 =====================================

strategy_plava_FULL.skip_to_flag(2)
# strategy_plava_FULL.skip_to_flag("skip_object")
strategy_plava_FULL.set_skip_flag(24)

strategy_plava_FULL.add_sequence(blue_get_5_front(True))
strategy_plava_FULL.skip_to_flag("reset")

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
strategy_plava_FULL.skip_to_flag("zaobilazak")

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

# strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.go_to_XY(1050, -600, False, at=2, b=50, ns=0)
# strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -780, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni zadrugi plenter


strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.set_skip_flag(9)
strategy_plava_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_plava_FULL.go_to_XY(1300, -700, at=100, b=50)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-5)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())  # -70

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ========================alternativna strategija 3 ako je dosao sa tanjira br.6 =====================================

strategy_plava_FULL.skip_to_flag(13)
# strategy_plava_FULL.skip_to_flag("skip_object")
strategy_plava_FULL.set_skip_flag(37)

strategy_plava_FULL.add_sequence(blue_get_5_front(True, 100))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1050, -600, False, at=0, b=50)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -800, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # ostavlja prve u tanjir

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # dodaje poene za drugi plenter

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.set_skip_flag(10)
strategy_plava_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_plava_FULL.go_to_XY(1300, -700, at=100, b=50)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-3)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# =======================  alternativna strategija sa 2 na 4 (24) kada nema prvog i treceg tanjira  ====================================
# nova kad nam g3 ili alekxa mogu uzeti prvi i treci tanjir ( prvi je na 12 sati i tako u smjeru kazaljke na satu dodjes do treceg)

strategy_plava_FULL.skip_to_flag(24)

strategy_plava_FULL.set_skip_flag(47)
strategy_plava_FULL.add_sequence(blue_get_6_front(True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(850, -600, False, at=1, b=50, ns=0)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -780, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_plava_FULL.go_to_XY(1300, -700, at=100, b=50)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.add_sequence(grip3_front_plant(0))

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-5)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())  # -70

# strategy_plava_FULL.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy_plava_FULL.rotate_to(-90)

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ========================alternativna strategija 5 ako nema 1. i 4. tanjira =====================================

strategy_plava_FULL.skip_to_flag(15)
# strategy_plava_FULL.skip_to_flag("skip_object")
strategy_plava_FULL.set_skip_flag(56)

strategy_plava_FULL.add_sequence(blue_get_6_back(True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.set_skip_flag(57)
strategy_plava_FULL.add_sequence(blue_get_3_front(True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1050, -600, at=0, b=50)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -780, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_distance_angle(100, 0)

strategy_plava_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_plava_FULL.go_to_XY(1300, -700, at=100, b=50)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.activate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.add_sequence(grip3_front_plant(0))

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(0)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())  # -70

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ===================alternativna gde ide na "nasu stranu"==================================
strategy_plava_FULL.skip_to_flag(56)
# strategy_plava_FULL.skip_to_flag("skip_object")

strategy_plava_FULL.add_sequence(blue_get_3_back())
strategy_plava_FULL.skip_to_flag("reset")

# strategy_plava_FULL.skip_to_flag(37)
strategy_plava_FULL.skip_to_flag(57)

strategy_plava_FULL.add_sequence(blue_get_2_front())
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -780, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter

strategy_plava_FULL.set_distance_angle(200, 0, at=0, b=50)

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.set_skip_flag(7)
strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(700, -1700, at=2, b=50)
strategy_plava_FULL.add_sequence(prepare_arms6())
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)

strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(0)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())


# ====================alternativna gde ce na kraju da proverava tanjir br5 jer do sada nije ==========================

strategy_plava_FULL.skip_to_flag(37)
strategy_plava_FULL.skip_to_flag(47)
strategy_plava_FULL.skip_to_flag(57)

strategy_plava_FULL.add_sequence(blue_get_2_front())
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1800, -800, at=100, b=50, bs=1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.move_front_arm(120, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(-90)
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_plava_FULL.set_distance_angle(50, 0)
# ostavlja prednje u planter bez saksija
strategy_plava_FULL.move_mechanism(270)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_front_arm(85, v=15)
strategy_plava_FULL.ungrip_front()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_front_arm(120, v=30)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za prvi plenter

strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-100, 0, at=100, b=50)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1382, -700, False, at=100, b=50)
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.start_step_actions()  # podize ruku
strategy_plava_FULL.go_to_XY(1382, -190, False, at=100, b=200)  # 185
strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.move_back_arm(170, v=15)
strategy_plava_FULL.ungrip_back()

# strategy_plava_FULL.start_parallel()
strategy_plava_FULL.move_back_arm(210, v=15)
strategy_plava_FULL.move_mechanism(180)
# strategy_plava_FULL.end_parallel()

strategy_plava_FULL.add_points("unload", 20)  # poeni za drugi plenter

# ide na tanjir br.5 sada
strategy_plava_FULL.set_distance_angle(450, 0, at=100, b=50)

strategy_plava_FULL.skip_to_flag(9)
strategy_plava_FULL.skip_to_flag(10)


strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()


strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(700, -700, False, at=100, b=50)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.add_sequence(prepare_arms6())
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.activate_prednja_grtalca()

# ovde nema vise sta da trazi i ide kuci ako ne nadje
strategy_plava_FULL.set_skip_flag(7)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-3)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

# 3 - 2 u potove i grtne u polje pored
strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())


# ================traganje za biljkama na kraju strategija ==========
strategy_plava_FULL.skip_to_flag(4)
strategy_plava_FULL.skip_to_flag(8)

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(700, -700,  False, at=100, b=50)
strategy_plava_FULL.add_sequence(prepare_arms6())
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.rotate_to(180)
strategy_plava_FULL.activate_prednja_grtalca()

strategy_plava_FULL.set_skip_flag(6)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(-3)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

# 3 - 2 u potove i grtne u polje pored
strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ================traganje za biljkama dalje.... ako malo pre nije nasao ===================

strategy_plava_FULL.skip_to_flag(6)

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(700, -1700, at=100, b=50)
strategy_plava_FULL.add_sequence(prepare_arms6())
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.rotate_to(180)

strategy_plava_FULL.set_skip_flag(7)
strategy_plava_FULL.add_sequence(grip3_front_plant(0, True))
strategy_plava_FULL.skip_to_flag("reset")

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.rotate_to(0)
strategy_plava_FULL.activate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.set_distance_angle(-230, 0)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.add_sequence(grip_back_plant())

strategy_plava_FULL.add_sequence(univerzalni_kraj_plava())

# ===============ako nista nije nasao :(==============
strategy_plava_FULL.skip_to_flag(7)

strategy_plava_FULL.front_all_off()
strategy_plava_FULL.back_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1670, -250, False, at=100, b=50, bs=0.1, s=0.1)
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.end()
# ========================TIME CHECK==============================

strategy_plava_FULL.skip_to_flag("brzi_istovar")

strategy_plava_FULL.back_all_off()
strategy_plava_FULL.front_all_on()

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.go_to_XY(1472, -280, at=100, b=200)  # 350
strategy_plava_FULL.move_front_arm(120, v=15)  # podize ruku
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.ungrip_back()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.front_all_off()

strategy_plava_FULL.rotate_to(0)
# strategy_plava_FULL.set_distance_angle(-10, 0)
strategy_plava_FULL.move_mechanism(230)  # 220
strategy_plava_FULL.move_front_arm(100, v=30)  # 100
strategy_plava_FULL.ungrip_front()
strategy_plava_FULL.move_front_arm(120, v=30)

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(60, 0)
strategy_plava_FULL.grip_back()
strategy_plava_FULL.activate_prednja_leva_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.add_points("unload", 12)  # poeni za 3 biljke u limovima

strategy_plava_FULL.set_distance_angle(0, -93, g=0.3)  # zatorira ka tanjiru

strategy_plava_FULL.start_step_actions()
strategy_plava_FULL.set_distance_angle(180, 0, g=0.5)  # udje u tanjur
# strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.end_step_actions()

strategy_plava_FULL.all_off()

strategy_plava_FULL.end()
# ==========================TIMEOUT ===========================


strategy_plava_FULL.skip_to_flag("timeout")

strategy_plava_FULL.front_all_on()

strategy_plava_FULL.go_to_XY(1620, -250, False, at=100, b=50, bs=0.1, s=0.1)

strategy_plava_FULL.start_parallel()
strategy_plava_FULL.ungrip_front()
strategy_plava_FULL.ungrip_back()
strategy_plava_FULL.move_back_arm(210)
strategy_plava_FULL.move_mechanism(180)
strategy_plava_FULL.deactivate_zadnja_grtalca()
strategy_plava_FULL.deactivate_prednja_grtalca()
strategy_plava_FULL.end_parallel()


strategy_plava_FULL.end()
