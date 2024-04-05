from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, pasivna odnosno osnovna

strategy_zuta_FULL = Strategy()
# idemo na panele
strategy_zuta_FULL.rotate_to(0)
strategy_zuta_FULL.front_sensors_on()
strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(195, 790, g=0.4)  # rotira panele
strategy_zuta_FULL.activate_triangle()
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.add_sequence(prepare_front_arm())
strategy_zuta_FULL.deactivate_triangle()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.add_points("unload", 15)  # ispisuje poene za panele

# dize zastavu koja ga baca na prvi tanjir (srednji tanjir kod sima)
strategy_zuta_FULL.set_skip_flag(1)
# ako detektuje nekog ili ako ne bude biljaka na cetvrtom (srednjem kod panela) tanjiru


# provjerava da li je pokupio biljke na prvom tanjiru
strategy_zuta_FULL.add_sequence(yellow_get_4_front(True))

# u slucaju da sretnemo nekoga dok ide do tanjira kod sima
strategy_zuta_FULL.set_skip_flag(2)
# skocice ako ne nadje biljke na fleg 2 to jest na peti tanjir

strategy_zuta_FULL.add_sequence(yellow_get_1_back(True))

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu da bi mogao doci do prvog plentera
strategy_zuta_FULL.set_skip_flag("zaobilazak")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 780, False, at=2, b=200,
                            bs=1)  # dolazi ispred prvog plantera , plenter kod sima
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(95)
strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.skip_to_flag("reset")

# ostavlja zadnje u planter kod sima
strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)
strategy_zuta_FULL.end_step_actions()


strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)  # poeni za prvi plenter

# ===========================================================

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

# ostavlja biljke u drugi plenter i ravna limove da bi posle mogao da ubaci po 5 biljaka u njih
strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 190, at=100, b=200)
strategy_zuta_FULL.move_mechanism(340)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)  # poeni za drugi plenter

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

# =======dio koji sluzi za ostavljanje 5 biljaka u metale i rotiranje boljaka u potovima tj svrsetak========

# ide unatrrag prema drugom tanjiru
strategy_zuta_FULL.set_distance_angle(-100, 0)

strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke 3 pa 3
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=100,
                            b=50)  # dolazi do drugog tanjira
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)

# odavde skace na trece biljke ako nema ovih
strategy_zuta_FULL.set_skip_flag(4)
# provjerava da li ima biljak na drugom krugu
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
# i hvata tri biljke zadnjim dijelom ako ima biljaka
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(3)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
# hvata druge tri biljke prednjim dijelom,
strategy_zuta_FULL.add_sequence(grip_front_plant())
# ne provjerava jer ako su bile tu prve tri bice i druge

# u ovom prozoru radimo grtanje trecih biljaka, a ovaj fleg sluzi
# strategy_zuta_FULL.set_skip_flag(5)
# # ako detektujemo nekog u ovom prozoru da preskoci to grtanje i ode odma na stavljanje 5 biljaka u metale

# strategy_zuta_FULL.start_step_actions()
# # odlazi u centar i tu se rotira kako bi zgrnuo biljke iz treceg kruga
# strategy_zuta_FULL.go_to_XY(1000, 1500, at=0, b=50)
# strategy_zuta_FULL.deactivate_zadnja_grtalca()
# strategy_zuta_FULL.deactivate_prednja_grtalca()
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.front_all_off()
# strategy_zuta_FULL.back_all_on()

# # grtanje trecih biljaka tj dovodjenje tih biljaka do coska iz kog smo krenuli
# strategy_zuta_FULL.start_step_actions()
# strategy_zuta_FULL.go_to_XY(450, 450, False, at=0, b=50)
# strategy_zuta_FULL.activate_zadnja_grtalca()
# strategy_zuta_FULL.move_back_arm(210)
# strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_step_actions()

# # poeni za gole biljke u cosku iz kog smo krenuli
# strategy_zuta_FULL.add_points("unload", 6)

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
# dolazi blizu metala po istom iksu kako bi ostavio 5 biljaka u njih
strategy_zuta_FULL.go_to_XY(1542, 650, False, at=100, b=50)
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

# skace ovde ako u se u prethodnom prozoru detektuje i preskace grtanje u pocetni cosak
# strategy_zuta_FULL.skip_to_flag(5) NEMA OVOG VISE

strategy_zuta_FULL.set_skip_flag("brzi_istovar")  # stavlja fleg u kojem ako
strategy_zuta_FULL.check_time(72, "brzi_istovar")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1542, 265, False, at=100, b=200)  # 350
strategy_zuta_FULL.move_back_arm(210, v=15)  # podize ruku
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.rotate_to(0)
# strategy_zuta_FULL.set_distance_angle(-10, 0)
strategy_zuta_FULL.move_mechanism(130)  # 220
strategy_zuta_FULL.move_back_arm(190, v=30)  # 100
strategy_zuta_FULL.ungrip_back()
strategy_zuta_FULL.move_back_arm(210, v=30)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(200, 0, at=100, b=50)
strategy_zuta_FULL.grip_back()
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(120, v=30)
strategy_zuta_FULL.go_to_XY(1312, 270, at=100, b=50)  # 285
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(230)  # izbaci ruku
strategy_zuta_FULL.move_front_arm(100, v=30)
strategy_zuta_FULL.ungrip_front()
strategy_zuta_FULL.move_front_arm(120, v=30)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(60, 0)
strategy_zuta_FULL.activate_prednja_desna_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.set_distance_angle(0, 95, g=0.3)  # zatorira ka tanjiru

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(300, 0, g=0.5)  # udje u tanjur
# strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.all_off()

strategy_zuta_FULL.end()

# =======================   alternativna strategija 1   =========================================================================

strategy_zuta_FULL.skip_to_flag(1)
strategy_zuta_FULL.set_skip_flag(15)

strategy_zuta_FULL.add_sequence(yellow_get_1_front(True))

strategy_zuta_FULL.skip_to_flag("reset")
strategy_zuta_FULL.set_skip_flag(13)

strategy_zuta_FULL.add_sequence(yellow_get_6_back(True))
strategy_zuta_FULL.skip_to_flag("reset")

# ovde skace na zaobilaznu koordinatu u alternativnoj 2
strategy_zuta_FULL.set_skip_flag("zaobilazak")

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()
strategy_zuta_FULL.start_step_actions()
# 762 # dolazi ispred plantera
strategy_zuta_FULL.go_to_XY(1800, 780, at=2, b=200, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)

strategy_zuta_FULL.front_all_off()

strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 190, at=100, b=200)  # 185
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)  # za drugi plenter


strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_distance_angle(-100, 0)

# ide na tanjir broj tri ako nema u tanjiru dva ili vidi protivnika
strategy_zuta_FULL.set_skip_flag(8)

strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=2, b=50)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))

strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(3)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 2 ako je dosao sa tanjira br.1 =====================================

strategy_zuta_FULL.skip_to_flag(2)
# strategy_zuta_FULL.skip_to_flag("skip_object")
strategy_zuta_FULL.set_skip_flag(24)

strategy_zuta_FULL.add_sequence(yellow_get_5_back(True))
strategy_zuta_FULL.skip_to_flag("reset")

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
strategy_zuta_FULL.skip_to_flag("zaobilazak")

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1050, 600, at=2, b=50)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 200, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_distance_angle(-100, 0)

strategy_zuta_FULL.set_skip_flag(9)
strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=100, b=50)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(5)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 3 ako je dosao sa tanjira br.6 =====================================

strategy_zuta_FULL.skip_to_flag(13)
# strategy_zuta_FULL.skip_to_flag("skip_object")
strategy_zuta_FULL.set_skip_flag(37)

strategy_zuta_FULL.add_sequence(yellow_get_5_back(True, 100))
strategy_zuta_FULL.skip_to_flag("reset")

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
strategy_zuta_FULL.skip_to_flag("zaobilazak")

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1050, 600, at=2, b=50)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 800, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 190, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_distance_angle(-100, 0)

strategy_zuta_FULL.set_skip_flag(10)
strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=2, b=50)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(3)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# =======================  alternativna strategija sa 2 na 4 (24) kada nema prvog i petog tanjira  ====================================
# nova kad nam g3 ili alekxa mogu uzeti prvi i peti tanjir ( prvi je na 12 sati i tako u smjeru kazaljke na satu dodjes do petog)

strategy_zuta_FULL.skip_to_flag(24)

strategy_zuta_FULL.set_skip_flag(47)
strategy_zuta_FULL.add_sequence(yellow_get_6_back(True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(850, 600, at=0, b=50)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 200, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_distance_angle(-100, 0)

strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=100, b=50)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130))

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(5)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

# strategy_zuta_FULL.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy_zuta_FULL.rotate_to(-90)

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())


# ============================== alternativna straegija 5: kada nema 1. i 4. tanjira i ide ukoso preko terena ==============

# strategy_zuta_FULL.skip_to_flag(15)
# # strategy_zuta_FULL.skip_to_flag("skip_object")
# strategy_zuta_FULL.set_skip_flag(56)

# strategy_zuta_FULL.add_sequence(yellow_get_6_back(True))
# strategy_zuta_FULL.skip_to_flag("reset")

# # ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
# strategy_zuta_FULL.skip_to_flag("zaobilazak")

# strategy_zuta_FULL.back_all_off()
# strategy_zuta_FULL.front_all_on()

# strategy_zuta_FULL.start_step_actions()
# strategy_zuta_FULL.go_to_XY(1050, 600, at=0, b=50)
# strategy_zuta_FULL.deactivate_zadnja_grtalca()
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.front_all_off()
# strategy_zuta_FULL.back_all_on()

# strategy_zuta_FULL.start_step_actions()
# strategy_zuta_FULL.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
# strategy_zuta_FULL.deactivate_zadnja_grtalca()
# strategy_zuta_FULL.move_back_arm(210, v=15)
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.rotate_to(90)
# strategy_zuta_FULL.skip_to_flag("reset")

# strategy_zuta_FULL.back_all_off()

# strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
# strategy_zuta_FULL.set_distance_angle(-50, 0)
# strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.move_back_arm(175, v=15)
# strategy_zuta_FULL.ungrip_back()

# # strategy_zuta_FULL.start_parallel()
# strategy_zuta_FULL.move_back_arm(210, v=30)
# strategy_zuta_FULL.move_mechanism(180)
# # strategy_zuta_FULL.end_parallel()

# strategy_zuta_FULL.add_points("unload", 20)

# strategy_zuta_FULL.front_all_on()

# strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

# strategy_zuta_FULL.start_step_actions()
# strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
# strategy_zuta_FULL.move_front_arm(120, v=15)
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.start_step_actions()  # podize ruku
# strategy_zuta_FULL.go_to_XY(1382, 200, at=100, b=200)  # 185
# strategy_zuta_FULL.rotate_to(180)
# strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.move_front_arm(80, v=15)
# strategy_zuta_FULL.ungrip_front()

# # strategy_zuta_FULL.start_parallel()
# strategy_zuta_FULL.move_front_arm(120, v=15)
# strategy_zuta_FULL.move_mechanism(180)
# # strategy_zuta_FULL.end_parallel()

# strategy_zuta_FULL.add_points("unload", 20)

# # 650 # ide unatrrag prema sledecem tanjiru

# strategy_zuta_FULL.front_all_off()
# strategy_zuta_FULL.back_all_on()

# strategy_zuta_FULL.set_distance_angle(-100, 0)

# strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# # TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
# strategy_zuta_FULL.go_to_XY(1300, 700, False, at=100, b=50)
# strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.activate_zadnja_grtalca()
# strategy_zuta_FULL.end_step_actions()

# strategy_zuta_FULL.rotate_to(180)
# strategy_zuta_FULL.add_sequence(grip3_back_plant(-110))

# strategy_zuta_FULL.start_step_actions()
# strategy_zuta_FULL.rotate_to(0)
# strategy_zuta_FULL.activate_prednja_grtalca()
# strategy_zuta_FULL.deactivate_zadnja_grtalca()
# strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

# strategy_zuta_FULL.back_all_off()
# strategy_zuta_FULL.front_all_on()

# strategy_zuta_FULL.set_distance_angle(230, 0)
# strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

# strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 5 ako nema 1. i 4. tanjira =====================================

strategy_zuta_FULL.skip_to_flag(15)
# strategy_zuta_FULL.skip_to_flag("skip_object")
strategy_zuta_FULL.set_skip_flag(56)

strategy_zuta_FULL.add_sequence(yellow_get_6_front(True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.set_skip_flag(57)
strategy_zuta_FULL.add_sequence(yellow_get_3_back(True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1050, 600, at=0, b=50)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 200, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_distance_angle(-100, 0)

strategy_zuta_FULL.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
strategy_zuta_FULL.go_to_XY(1300, 700, False, at=100, b=50)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130))

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(0)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())  # -70

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ===================alternativna gde ide na "nasu stranu"==================================
strategy_zuta_FULL.skip_to_flag(56)
# strategy_zuta_FULL.skip_to_flag("skip_object")

strategy_zuta_FULL.add_sequence(yellow_get_3_front())
strategy_zuta_FULL.skip_to_flag("reset")

# strategy_zuta_FULL.skip_to_flag(37)
strategy_zuta_FULL.skip_to_flag(57)

strategy_zuta_FULL.add_sequence(yellow_get_2_back())
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 200, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.set_distance_angle(-200, 0, at=0, b=50)
strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.set_skip_flag(7)
strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(700, 1700, False, at=2, b=50)
strategy_zuta_FULL.add_sequence(prepare_arms6())
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)

strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(0)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

strategy_zuta_FULL.end()

# ====================alternativna gde ce na kraju da proverava tanjir br3 jer do sada nije ==========================

strategy_zuta_FULL.skip_to_flag(37)
strategy_zuta_FULL.skip_to_flag(47)


strategy_zuta_FULL.add_sequence(yellow_get_2_back())
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1800, 800, False, at=100, b=50, bs=1)
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.move_back_arm(210, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(90)
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.start_step_actions()  # dolazi i priprema ruku
strategy_zuta_FULL.set_distance_angle(-50, 0)
strategy_zuta_FULL.move_mechanism(90)  # ostavlja prednje u planter bez saksija
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_back_arm(175, v=15)
strategy_zuta_FULL.ungrip_back()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_back_arm(210, v=30)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(100, 0, at=100, b=50)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1382, 700, at=100, b=50)
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.start_step_actions()  # podize ruku
strategy_zuta_FULL.go_to_XY(1382, 190, at=100, b=200)  # 185
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.move_front_arm(80, v=15)
strategy_zuta_FULL.ungrip_front()

# strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.move_front_arm(120, v=15)
strategy_zuta_FULL.move_mechanism(180)
# strategy_zuta_FULL.end_parallel()

strategy_zuta_FULL.add_points("unload", 20)

# ide na tanjir br.3 sada
strategy_zuta_FULL.set_distance_angle(-450, 0, at=100, b=50)

strategy_zuta_FULL.skip_to_flag(9)
strategy_zuta_FULL.skip_to_flag(10)

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(700, 700, at=100, b=50)
strategy_zuta_FULL.add_sequence(prepare_arms6())
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

# strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
# strategy_zuta_FULL.end_step_actions()

# ovde nema vise sta da trazi i ide kuci ako ne nadje
strategy_zuta_FULL.set_skip_flag(7)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(3)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())

# 3 - 2 u potove i grtne u polje pored
strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())


# ================traganje za biljkama na kraju strategija ==========
strategy_zuta_FULL.skip_to_flag(4)
strategy_zuta_FULL.skip_to_flag(8)

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(700, 700, at=100, b=50)
strategy_zuta_FULL.add_sequence(prepare_arms6())
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

# strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(180)
strategy_zuta_FULL.activate_zadnja_grtalca()
# strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.set_skip_flag(6)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(3)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())

# 3 - 2 u potove i grtne u polje pored
strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ================traganje za biljkama dalje.... ako malo pre nije nasao ===================

strategy_zuta_FULL.skip_to_flag(6)

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(700, 1700, False, at=100, b=50)
strategy_zuta_FULL.add_sequence(prepare_arms6())
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.rotate_to(180)

strategy_zuta_FULL.set_skip_flag(7)
strategy_zuta_FULL.add_sequence(grip3_back_plant(-130, True))
strategy_zuta_FULL.skip_to_flag("reset")

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.rotate_to(0)
strategy_zuta_FULL.activate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.set_distance_angle(230, 0)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.add_sequence(grip_front_plant())

strategy_zuta_FULL.add_sequence(univerzalni_kraj_zuta())

# ===============ako nista nije nasao :(==============
strategy_zuta_FULL.skip_to_flag(7)

strategy_zuta_FULL.back_all_off()
strategy_zuta_FULL.front_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1670, 250, at=100, b=50, bs=0.1, s=0.1)
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.end()
# ========================TIME CHECK==============================

strategy_zuta_FULL.skip_to_flag("brzi_istovar")

strategy_zuta_FULL.front_all_off()
strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.go_to_XY(1472, 280, False, at=100, b=200)  # 350
strategy_zuta_FULL.move_back_arm(210, v=15)  # podize ruku
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.ungrip_front()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.back_all_off()

strategy_zuta_FULL.rotate_to(0)
# strategy_zuta_FULL.set_distance_angle(-10, 0)
strategy_zuta_FULL.move_mechanism(130)  # 220
strategy_zuta_FULL.move_back_arm(190, v=30)  # 100
strategy_zuta_FULL.ungrip_back()
strategy_zuta_FULL.move_back_arm(210, v=30)

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(-60, 0)
strategy_zuta_FULL.grip_front()
strategy_zuta_FULL.activate_zadnja_leva_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.add_points("unload", 12)

strategy_zuta_FULL.set_distance_angle(0, 93, g=0.3)  # zatorira ka tanjiru

strategy_zuta_FULL.start_step_actions()
strategy_zuta_FULL.set_distance_angle(-180, 0, g=0.5)  # udje u tanjur
# strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_step_actions()

strategy_zuta_FULL.all_off()

strategy_zuta_FULL.end()
# ==========================TIMEOUT ===========================


strategy_zuta_FULL.skip_to_flag("timeout")

strategy_zuta_FULL.back_all_on()

strategy_zuta_FULL.go_to_XY(1620, 250, False, at=100, b=50, bs=0.1, s=0.1)

strategy_zuta_FULL.start_parallel()
strategy_zuta_FULL.ungrip_back()
strategy_zuta_FULL.ungrip_front()
strategy_zuta_FULL.move_front_arm(120)
strategy_zuta_FULL.move_mechanism(180)
strategy_zuta_FULL.deactivate_prednja_grtalca()
strategy_zuta_FULL.deactivate_zadnja_grtalca()
strategy_zuta_FULL.end_parallel()


strategy_zuta_FULL.end()
