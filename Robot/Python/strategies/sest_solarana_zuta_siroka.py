from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, pasivna odnosno osnovna

sest_solarna_zuta_siroka = Strategy()
# idemo na panele
sest_solarna_zuta_siroka.rotate_to(0)
sest_solarna_zuta_siroka.set_skip_flag("odma")
sest_solarna_zuta_siroka.front_sensors_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(190, 1780, at=0, ts=0.5)  # rotira panele
sest_solarna_zuta_siroka.activate_triangle()
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210)
sest_solarna_zuta_siroka.add_sequence(prepare_front_arm())
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.skip_to_flag("odma")
sest_solarna_zuta_siroka.deactivate_triangle()
sest_solarna_zuta_siroka.add_points("unload", 15)  # ispisuje poene za panele

# dize zastavu koja ga baca na prvi tanjir (srednji tanjir kod sima)
sest_solarna_zuta_siroka.set_skip_flag(1)
# ako detektuje nekog ili ako ne bude biljaka na cetvrtom (srednjem kod panela) tanjiru


# provjerava da li je pokupio biljke na prvom tanjiru
sest_solarna_zuta_siroka.add_sequence(yellow_get_4_front(True))

# u slucaju da sretnemo nekoga dok ide do tanjira kod sima
sest_solarna_zuta_siroka.set_skip_flag(2)
# skocice ako ne nadje biljke na fleg 2 to jest na peti tanjir

sest_solarna_zuta_siroka.add_sequence(yellow_get_1_back(True))

# skipuje na drugu alternativnu jer tamo ima zaobilaznu koordinatu da bi mogao doci do prvog plentera
sest_solarna_zuta_siroka.set_skip_flag("zaobilazak")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=2, b=200,
                                  bs=1)  # dolazi ispred prvog plantera , plenter kod sima
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(95)
sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.skip_to_flag("reset")

# ostavlja zadnje u planter kod sima
sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()


sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)  # poeni za prvi plenter

# ===========================================================

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

# ostavlja biljke u drugi plenter i ravna limove da bi posle mogao da ubaci po 5 biljaka u njih
sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 190, at=100, b=200)
sest_solarna_zuta_siroka.move_mechanism(340)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)  # poeni za drugi plenter

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

# =======dio koji sluzi za ostavljanje 5 biljaka u metale i rotiranje boljaka u potovima tj svrsetak========

# ide unatrrag prema drugom tanjiru
sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke 3 pa 3
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=100,
                                  b=50)  # dolazi do drugog tanjira
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)

# odavde skace na trece biljke ako nema ovih
sest_solarna_zuta_siroka.set_skip_flag(4)
# provjerava da li ima biljak na drugom krugu
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
# i hvata tri biljke zadnjim dijelom ako ima biljaka
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(3)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
# hvata druge tri biljke prednjim dijelom,
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())
# ne provjerava jer ako su bile tu prve tri bice i druge

# u ovom prozoru radimo grtanje trecih biljaka, a ovaj fleg sluzi
# sest_solarna_zuta_siroka.set_skip_flag(5)
# # ako detektujemo nekog u ovom prozoru da preskoci to grtanje i ode odma na stavljanje 5 biljaka u metale

# sest_solarna_zuta_siroka.start_step_actions()
# # odlazi u centar i tu se rotira kako bi zgrnuo biljke iz treceg kruga
# sest_solarna_zuta_siroka.go_to_XY(1000, 1500, at=0, b=50)
# sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.front_all_off()
# sest_solarna_zuta_siroka.back_all_on()

# # grtanje trecih biljaka tj dovodjenje tih biljaka do coska iz kog smo krenuli
# sest_solarna_zuta_siroka.start_step_actions()
# sest_solarna_zuta_siroka.go_to_XY(450, 450, False, at=0, b=50)
# sest_solarna_zuta_siroka.activate_zadnja_grtalca()
# sest_solarna_zuta_siroka.move_back_arm(210)
# sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_step_actions()

# # poeni za gole biljke u cosku iz kog smo krenuli
# sest_solarna_zuta_siroka.add_points("unload", 6)

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
# dolazi blizu metala po istom iksu kako bi ostavio 5 biljaka u njih
sest_solarna_zuta_siroka.go_to_XY(1542, 650, False, at=100, b=50)
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

# skace ovde ako u se u prethodnom prozoru detektuje i preskace grtanje u pocetni cosak
# sest_solarna_zuta_siroka.skip_to_flag(5) NEMA OVOG VISE

sest_solarna_zuta_siroka.set_skip_flag(
    "brzi_istovar")  # stavlja fleg u kojem ako
sest_solarna_zuta_siroka.check_time(72, "brzi_istovar")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1542, 265, False, at=100, b=200)  # 350
sest_solarna_zuta_siroka.move_back_arm(210, v=15)  # podize ruku
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.rotate_to(0)
# sest_solarna_zuta_siroka.set_distance_angle(-10, 0)
sest_solarna_zuta_siroka.move_mechanism(130)  # 220
sest_solarna_zuta_siroka.move_back_arm(190, v=30)  # 100
sest_solarna_zuta_siroka.ungrip_back()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(200, 0, at=100, b=50)
sest_solarna_zuta_siroka.grip_back()
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(120, v=30)
sest_solarna_zuta_siroka.go_to_XY(1312, 270, at=100, b=50)  # 285
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(230)  # izbaci ruku
sest_solarna_zuta_siroka.move_front_arm(100, v=30)
sest_solarna_zuta_siroka.ungrip_front()
sest_solarna_zuta_siroka.move_front_arm(120, v=30)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(60, 0)
sest_solarna_zuta_siroka.activate_prednja_desna_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.set_distance_angle(
    0, 95, g=0.3)  # zatorira ka tanjiru

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(300, 0, g=0.5)  # udje u tanjur
# sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.all_off()

sest_solarna_zuta_siroka.end()

# =======================   alternativna strategija 1   =========================================================================

sest_solarna_zuta_siroka.skip_to_flag(1)
sest_solarna_zuta_siroka.set_skip_flag(15)

sest_solarna_zuta_siroka.add_sequence(yellow_get_1_front(True))

sest_solarna_zuta_siroka.skip_to_flag("reset")
sest_solarna_zuta_siroka.set_skip_flag(13)

sest_solarna_zuta_siroka.add_sequence(yellow_get_6_back(True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

# ovde skace na zaobilaznu koordinatu u alternativnoj 2
sest_solarna_zuta_siroka.set_skip_flag("zaobilazak")

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()
sest_solarna_zuta_siroka.start_step_actions()
# 762 # dolazi ispred plantera
sest_solarna_zuta_siroka.go_to_XY(1800, 780, at=2, b=200, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)

sest_solarna_zuta_siroka.front_all_off()

sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 190, at=100, b=200)  # 185
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)  # za drugi plenter


sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

# ide na tanjir broj tri ako nema u tanjiru dva ili vidi protivnika
sest_solarna_zuta_siroka.set_skip_flag(8)

sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=2, b=50)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))

sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(3)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 2 ako je dosao sa tanjira br.1 =====================================

sest_solarna_zuta_siroka.skip_to_flag(2)
# sest_solarna_zuta_siroka.skip_to_flag("skip_object")
sest_solarna_zuta_siroka.set_skip_flag(24)

sest_solarna_zuta_siroka.add_sequence(yellow_get_5_back(True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
sest_solarna_zuta_siroka.skip_to_flag("zaobilazak")

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1050, 600, at=2, b=50)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 200, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

sest_solarna_zuta_siroka.set_skip_flag(9)
sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=100, b=50)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(5)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 3 ako je dosao sa tanjira br.6 =====================================

sest_solarna_zuta_siroka.skip_to_flag(13)
# sest_solarna_zuta_siroka.skip_to_flag("skip_object")
sest_solarna_zuta_siroka.set_skip_flag(37)

sest_solarna_zuta_siroka.add_sequence(yellow_get_5_back(True, 100))
sest_solarna_zuta_siroka.skip_to_flag("reset")

# ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
sest_solarna_zuta_siroka.skip_to_flag("zaobilazak")

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1050, 600, at=2, b=50)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 800, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 190, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

sest_solarna_zuta_siroka.set_skip_flag(10)
sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=2, b=50)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(3)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# =======================  alternativna strategija sa 2 na 4 (24) kada nema prvog i petog tanjira  ====================================
# nova kad nam g3 ili alekxa mogu uzeti prvi i peti tanjir ( prvi je na 12 sati i tako u smjeru kazaljke na satu dodjes do petog)

sest_solarna_zuta_siroka.skip_to_flag(24)

sest_solarna_zuta_siroka.set_skip_flag(47)
sest_solarna_zuta_siroka.add_sequence(yellow_get_6_back(True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(850, 600, at=0, b=50)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 200, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=100, b=50)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130))

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(5)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

# sest_solarna_zuta_siroka.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# sest_solarna_zuta_siroka.rotate_to(-90)

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())


# ============================== alternativna straegija 5: kada nema 1. i 4. tanjira i ide ukoso preko terena ==============

# sest_solarna_zuta_siroka.skip_to_flag(15)
# # sest_solarna_zuta_siroka.skip_to_flag("skip_object")
# sest_solarna_zuta_siroka.set_skip_flag(56)

# sest_solarna_zuta_siroka.add_sequence(yellow_get_6_back(True))
# sest_solarna_zuta_siroka.skip_to_flag("reset")

# # ovde se ukljucuje ako je imao problem sa dolazenjem do prvog plantera
# sest_solarna_zuta_siroka.skip_to_flag("zaobilazak")

# sest_solarna_zuta_siroka.back_all_off()
# sest_solarna_zuta_siroka.front_all_on()

# sest_solarna_zuta_siroka.start_step_actions()
# sest_solarna_zuta_siroka.go_to_XY(1050, 600, at=0, b=50)
# sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.front_all_off()
# sest_solarna_zuta_siroka.back_all_on()

# sest_solarna_zuta_siroka.start_step_actions()
# sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
# sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# sest_solarna_zuta_siroka.move_back_arm(210, v=15)
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.rotate_to(90)
# sest_solarna_zuta_siroka.skip_to_flag("reset")

# sest_solarna_zuta_siroka.back_all_off()

# sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
# sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# sest_solarna_zuta_siroka.move_mechanism(90)  # ostavlja prednje u planter bez saksija
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.move_back_arm(175, v=15)
# sest_solarna_zuta_siroka.ungrip_back()

# # sest_solarna_zuta_siroka.start_parallel()
# sest_solarna_zuta_siroka.move_back_arm(210, v=30)
# sest_solarna_zuta_siroka.move_mechanism(180)
# # sest_solarna_zuta_siroka.end_parallel()

# sest_solarna_zuta_siroka.add_points("unload", 20)

# sest_solarna_zuta_siroka.front_all_on()

# sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

# sest_solarna_zuta_siroka.start_step_actions()
# sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
# sest_solarna_zuta_siroka.move_front_arm(120, v=15)
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
# sest_solarna_zuta_siroka.go_to_XY(1382, 200, at=100, b=200)  # 185
# sest_solarna_zuta_siroka.rotate_to(180)
# sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.move_front_arm(80, v=15)
# sest_solarna_zuta_siroka.ungrip_front()

# # sest_solarna_zuta_siroka.start_parallel()
# sest_solarna_zuta_siroka.move_front_arm(120, v=15)
# sest_solarna_zuta_siroka.move_mechanism(180)
# # sest_solarna_zuta_siroka.end_parallel()

# sest_solarna_zuta_siroka.add_points("unload", 20)

# # 650 # ide unatrrag prema sledecem tanjiru

# sest_solarna_zuta_siroka.front_all_off()
# sest_solarna_zuta_siroka.back_all_on()

# sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

# sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# # TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
# sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=100, b=50)
# sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.activate_zadnja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()

# sest_solarna_zuta_siroka.rotate_to(180)
# sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-110))

# sest_solarna_zuta_siroka.start_step_actions()
# sest_solarna_zuta_siroka.rotate_to(0)
# sest_solarna_zuta_siroka.activate_prednja_grtalca()
# sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA

# sest_solarna_zuta_siroka.back_all_off()
# sest_solarna_zuta_siroka.front_all_on()

# sest_solarna_zuta_siroka.set_distance_angle(230, 0)
# sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

# sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ========================alternativna strategija 5 ako nema 1. i 4. tanjira =====================================

sest_solarna_zuta_siroka.skip_to_flag(15)
# sest_solarna_zuta_siroka.skip_to_flag("skip_object")
sest_solarna_zuta_siroka.set_skip_flag(56)

sest_solarna_zuta_siroka.add_sequence(yellow_get_6_front(True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.set_skip_flag(57)
sest_solarna_zuta_siroka.add_sequence(yellow_get_3_back(True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1050, 600, at=0, b=50)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 200, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

# 650 # ide unatrrag prema sledecem tanjiru

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_distance_angle(-100, 0)

sest_solarna_zuta_siroka.start_step_actions()  # ide na sledece biljke
# TODO: napraviti da ide na sl tanjir ako ovde vidi protivnika
sest_solarna_zuta_siroka.go_to_XY(1300, 700, False, at=100, b=50)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130))

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(0)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())  # -70

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ===================alternativna gde ide na "nasu stranu"==================================
sest_solarna_zuta_siroka.skip_to_flag(56)
# sest_solarna_zuta_siroka.skip_to_flag("skip_object")

sest_solarna_zuta_siroka.add_sequence(yellow_get_3_front())
sest_solarna_zuta_siroka.skip_to_flag("reset")

# sest_solarna_zuta_siroka.skip_to_flag(37)
sest_solarna_zuta_siroka.skip_to_flag(57)

sest_solarna_zuta_siroka.add_sequence(yellow_get_2_back())
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 780, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 200, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.set_distance_angle(-200, 0, at=0, b=50)
sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.set_skip_flag(7)
sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(700, 1700, False, at=2, b=50)
sest_solarna_zuta_siroka.add_sequence(prepare_arms6())
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)

sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(0)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

sest_solarna_zuta_siroka.end()

# ====================alternativna gde ce na kraju da proverava tanjir br3 jer do sada nije ==========================

sest_solarna_zuta_siroka.skip_to_flag(37)
sest_solarna_zuta_siroka.skip_to_flag(47)


sest_solarna_zuta_siroka.add_sequence(yellow_get_2_back())
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1800, 800, False, at=100, b=50, bs=1)
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.move_back_arm(210, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(90)
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.start_step_actions()  # dolazi i priprema ruku
sest_solarna_zuta_siroka.set_distance_angle(-50, 0)
# ostavlja prednje u planter bez saksija
sest_solarna_zuta_siroka.move_mechanism(90)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_back_arm(175, v=15)
sest_solarna_zuta_siroka.ungrip_back()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(100, 0, at=100, b=50)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1382, 700, at=100, b=50)
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.start_step_actions()  # podize ruku
sest_solarna_zuta_siroka.go_to_XY(1382, 190, at=100, b=200)  # 185
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.move_mechanism(340)  # ostavlja biljke u drugi plenter
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.move_front_arm(80, v=15)
sest_solarna_zuta_siroka.ungrip_front()

# sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.move_front_arm(120, v=15)
sest_solarna_zuta_siroka.move_mechanism(180)
# sest_solarna_zuta_siroka.end_parallel()

sest_solarna_zuta_siroka.add_points("unload", 20)

# ide na tanjir br.3 sada
sest_solarna_zuta_siroka.set_distance_angle(-450, 0, at=100, b=50)

sest_solarna_zuta_siroka.skip_to_flag(9)
sest_solarna_zuta_siroka.skip_to_flag(10)

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(700, 700, at=100, b=50)
sest_solarna_zuta_siroka.add_sequence(prepare_arms6())
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

# sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()

# ovde nema vise sta da trazi i ide kuci ako ne nadje
sest_solarna_zuta_siroka.set_skip_flag(7)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(3)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())

# 3 - 2 u potove i grtne u polje pored
sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())


# ================traganje za biljkama na kraju strategija ==========
sest_solarna_zuta_siroka.skip_to_flag(4)
sest_solarna_zuta_siroka.skip_to_flag(8)

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(700, 700, at=100, b=50)
sest_solarna_zuta_siroka.add_sequence(prepare_arms6())
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

# sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(180)
sest_solarna_zuta_siroka.activate_zadnja_grtalca()
# sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.set_skip_flag(6)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(3)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())

# 3 - 2 u potove i grtne u polje pored
sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ================traganje za biljkama dalje.... ako malo pre nije nasao ===================

sest_solarna_zuta_siroka.skip_to_flag(6)

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(700, 1700, False, at=100, b=50)
sest_solarna_zuta_siroka.add_sequence(prepare_arms6())
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.rotate_to(180)

sest_solarna_zuta_siroka.set_skip_flag(7)
sest_solarna_zuta_siroka.add_sequence(grip3_back_plant(-130, True))
sest_solarna_zuta_siroka.skip_to_flag("reset")

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.rotate_to(0)
sest_solarna_zuta_siroka.activate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
# OVO IZVADITI AKO IDEMO NA 3 TANJIRA
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.set_distance_angle(230, 0)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.add_sequence(grip_front_plant())

sest_solarna_zuta_siroka.add_sequence(univerzalni_kraj_zuta())

# ===============ako nista nije nasao :(==============
sest_solarna_zuta_siroka.skip_to_flag(7)

sest_solarna_zuta_siroka.back_all_off()
sest_solarna_zuta_siroka.front_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1670, 250, at=100, b=50, bs=0.1, s=0.1)
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.end()
# ========================TIME CHECK==============================

sest_solarna_zuta_siroka.skip_to_flag("brzi_istovar")

sest_solarna_zuta_siroka.front_all_off()
sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.go_to_XY(1472, 280, False, at=100, b=200)  # 350
sest_solarna_zuta_siroka.move_back_arm(210, v=15)  # podize ruku
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.ungrip_front()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.back_all_off()

sest_solarna_zuta_siroka.rotate_to(0)
# sest_solarna_zuta_siroka.set_distance_angle(-10, 0)
sest_solarna_zuta_siroka.move_mechanism(130)  # 220
sest_solarna_zuta_siroka.move_back_arm(190, v=30)  # 100
sest_solarna_zuta_siroka.ungrip_back()
sest_solarna_zuta_siroka.move_back_arm(210, v=30)

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(-60, 0)
sest_solarna_zuta_siroka.grip_front()
sest_solarna_zuta_siroka.activate_zadnja_leva_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.add_points("unload", 12)

sest_solarna_zuta_siroka.set_distance_angle(
    0, 93, g=0.3)  # zatorira ka tanjiru

sest_solarna_zuta_siroka.start_step_actions()
sest_solarna_zuta_siroka.set_distance_angle(-200, 0, g=0.5)  # udje u tanjur
# sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_step_actions()

sest_solarna_zuta_siroka.all_off()

sest_solarna_zuta_siroka.end()
# ==========================TIMEOUT ===========================


sest_solarna_zuta_siroka.skip_to_flag("timeout")

sest_solarna_zuta_siroka.back_all_on()

sest_solarna_zuta_siroka.go_to_XY(
    1620, 250, False, at=100, b=50, bs=0.1, s=0.1)

sest_solarna_zuta_siroka.start_parallel()
sest_solarna_zuta_siroka.ungrip_back()
sest_solarna_zuta_siroka.ungrip_front()
sest_solarna_zuta_siroka.move_front_arm(120)
sest_solarna_zuta_siroka.move_mechanism(180)
sest_solarna_zuta_siroka.deactivate_prednja_grtalca()
sest_solarna_zuta_siroka.deactivate_zadnja_grtalca()
sest_solarna_zuta_siroka.end_parallel()


sest_solarna_zuta_siroka.end()
