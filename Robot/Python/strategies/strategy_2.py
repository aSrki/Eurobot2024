from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy2 = Strategy()

# robot krece iz zelenog polja u drugom kvadrantu
# ======================NOVA STRATEGIJA NOVA NOVA NOVA NOVA

# strategy2.lift_cakes(10)

strategy2.front_all_on()
strategy2.back_all_off()
# strategy2.go_to_XY(185, 1795)
strategy2.set_skip_flag(1)
strategy2.add_sequence(cherry3())  # sisa po visnjicama
strategy2.skip_to_flag("reset")
strategy2.front_all_off()
strategy2.back_all_on()
strategy2.move_vacuum(173)
strategy2.go_to_XY(200, 1825, False, g=0.9, ss=1, bs=0, at=0,
                   b=200)
strategy2.back_all_off()
strategy2.front_all_on()
strategy2.set_skip_flag(8)  # ode do pinka 2
# vise pokusaja da nebi trigerevo skipovanje pink1 i yellow 1
strategy2.go_to_XY(700, 2425, True, g=0.9, ss=1, bs=2, at=3, b=50)

strategy2.back_all_off()
strategy2.front_all_on()
strategy2.set_skip_flag(3)  # ova ga salje na pink1
strategy2.add_sequence(pink2())  # 0, 30
strategy2.front_all_off()
strategy2.back_all_on()
strategy2.skip_to_flag("reset")
strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
strategy2.back_all_off()
strategy2.front_all_on()
strategy2.add_sequence(yellow2())  # 0, 50
strategy2.set_skip_flag(10)  # skace na drugi deo terena po druge braon pakove
strategy2.add_sequence(brown2())

strategy2.go_to_XY(1675, 2620, True, ss=0.5, bs=2,
                   at=100, b=200)  # ide do basketa
strategy2.front_all_off()
strategy2.go_to_XY(1725, 2660, True)  # 1775 #namesta poziciju
# strategy2.back_all_on()

strategy2.add_sequence(unload_basket_green())

strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
strategy2.check_time(60)

strategy2.go_to_XY(1600, 2600, False)
strategy2.add_sequence(sortCakes(-40))

strategy2.move_pipe(170)
strategy2.move_door(190)
strategy2.check_time(1, "timeout")


# strategy2.back_all_on()
# strategy2.go_to_XY(1000, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1600, 1400, False, ss=0.5, bs=0.5, at=100, b=0)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1300, False)
# strategy2.rotate_to(0)

# strategy2.end()
# ==================================================================
# skip strat ide na drugi dispenzer


strategy2.skip_to_flag(1)

strategy2.vacuum_cherry(0)
strategy2.back_all_on()
strategy2.go_to_XY(190, 1820, False, ss=0.5, bs=2, at=2,
                   b=0)  # odmakne se od dispensera
# van stepekshona je zato sto bi inace spucao ruku u dispenser
strategy2.move_vacuum(173)
strategy2.back_all_off()
strategy2.front_all_on()

strategy2.go_to_XY(830, 2300, True, ss=0.5, bs=1, at=100,  # pokusava beskrajno da dodje do cheroa
                   b=0)  # 810 # ide do druge visnje
strategy2.set_skip_flag(4)
strategy2.go_to_XY(830, 2500, True, g=0.7, ss=0.5, bs=0, at=0,
                   b=100)  # ako je neko na cheroima ide dalje da sortira
strategy2.front_all_off()

# pali zadnje senzore kada krene u rikverc unutar ovog taska
strategy2.add_sequence(cherry2())  # sisa po visnjama
strategy2.back_all_off()
# strategy2.go_to_XY(855, 2500, False, 0.1)
strategy2.move_vacuum(173)

strategy2.skip_to_flag(4)
strategy2.vacuum_cherry(0)
strategy2.front_all_on()  # ide po pakove
# ide na drugu stranu, nece da sortira ako skupi sve, tek iz nje moze da predje na verzije sa 1 ili 2 unload-a
strategy2.set_skip_flag(5)
strategy2.add_sequence(pink2())  # 0, 30
strategy2.skip_to_flag("reset")
strategy2.back_all_on()
strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
strategy2.back_all_off()
strategy2.front_all_on()
strategy2.add_sequence(yellow2(0, 50))  # 0, 50
strategy2.set_skip_flag(6)
strategy2.front_all_on()  # skace na drugi deo terena po druge braon pakove
strategy2.add_sequence(brown2())
strategy2.front_all_off()

strategy2.front_all_on()
strategy2.go_to_XY(1675, 2620, True, ss=0.5, bs=2,
                   at=100, b=200)  # ide do basketa
strategy2.front_all_off()
strategy2.go_to_XY(1725, 2660, True)  # 1775 #namesta poziciju

strategy2.add_sequence(unload_basket_green())

strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
strategy2.check_time(60)

strategy2.go_to_XY(1600, 2600, False)
strategy2.add_sequence(sortCakes(-40))

strategy2.move_door(190)
strategy2.move_pipe(170)
strategy2.check_time(1, "timeout")

# strategy2.back_all_on()
# strategy2.go_to_XY(1000, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1600, 1400, False, ss=0.5, bs=0.5, at=100, b=0)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1300, False)
# strategy2.rotate_to(0)

# strategy2.end()
# ================================================DRUGI KVADRANT (kv.1)


# ovde je stigao ako je detektovao nekoga na prvom delu
strategy2.skip_to_flag(3)
strategy2.skip_to_flag(5)
strategy2.skip_to_flag(8)
strategy2.front_all_on()  # ide po pakove
strategy2.set_skip_flag(7)
strategy2.add_sequence(pink1(0, 0, attempts=100))
strategy2.skip_to_flag("reset")
strategy2.back_all_on()
strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
strategy2.back_all_off()
strategy2.front_all_on()
strategy2.add_sequence(yellow1())
strategy2.skip_to_flag(6)  # dosao na ovaj deo terena
strategy2.skip_to_flag(10)
strategy2.front_all_on()
# pomocna koordinata da proba zaobici
strategy2.go_to_XY(1275, 2300, True, ss=0.5, bs=0, at=0, b=200)
strategy2.skip_to_flag(7)
strategy2.front_all_on()
strategy2.add_sequence(brown1())
strategy2.front_all_off()

strategy2.back_all_on()
strategy2.go_to_XY(1675, 2620, False, ss=0.5, bs=2,
                   at=100, b=200)  # ide do basketa
strategy2.front_all_off()
strategy2.go_to_XY(1725, 2660, True)  # 1775 #namesta poziciju

strategy2.add_sequence(unload_basket_green())

strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
strategy2.check_time(60)

strategy2.go_to_XY(1600, 2600, False)
strategy2.add_sequence(sortCakes(-40))

strategy2.move_door(190)
strategy2.move_pipe(170)
strategy2.check_time(1, "timeout")

# strategy2.back_all_on()
# strategy2.go_to_XY(1000, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1600, 1400, False, ss=0.5, bs=0.5, at=100, b=0)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1300, False)
# strategy2.rotate_to(0)

# strategy2.end()
# ================================================OBICNI UNLOAD-OVI

strategy2.skip_to_flag("unload_3")
strategy2.add_sequence(unload1())  # izbacuje pakove
strategy2.skip_to_flag("unload_2")
strategy2.add_sequence(unload2())
strategy2.skip_to_flag("unload_1")
strategy2.add_sequence(unload3())
strategy2.skip_to_flag("unload_0")

strategy2.move_door(190)
strategy2.move_pipe(170)
strategy2.check_time(1, "timeout")

# strategy2.back_all_on()
# strategy2.go_to_XY(1000, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1600, 1400, False, ss=0.5, bs=0.5, at=100, b=0)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1300, False)
# strategy2.rotate_to(0)

# strategy2.end()
# ======================================tajmoautTTT

strategy2.skip_to_flag("timeout")
strategy2.back_all_on()
strategy2.grip_cakes(48)
strategy2.move_door(190)
strategy2.move_pipe(170)
strategy2.go_to_XY(1000, 1600, False, ss=0, bs=0.2, at=100, b=10, ns=0)
strategy2.back_all_off()
strategy2.go_to_XY(1700, 1300, False, ss=0, bs=0, at=0, b=200)

strategy2.end()


# strategy2.front_all_on()
# strategy2.back_all_off()
# # strategy2.go_to_XY(185, 1795)
# strategy2.set_skip_flag(9)
# strategy2.add_sequence(cherry3())  # sisa po visnjicama
# strategy2.skip_to_flag("reset")
# strategy2.go_to_XY(180, 1200, ss=0.5, bs=2, at=1,
#                    b=0)  # odmakne se od dispensera
# strategy2.move_vacuum(173)

# # strategy2.front_all_off()

# strategy2.vacuum_cherry(0)
# # 1650 # zaobilazi sve pakove i ide u centar stola
# # ako detektuje u sredini nekoga ide okolo kako zna i ume
# strategy2.go_to_XY(1000, 1650, True, ss=0.5, bs=1, at=0, b=0)

# strategy2.go_to_XY(830, 2300, True, ss=0.5, bs=1, at=100,  # pokusava beskrajno da dodje do cheroa
#                    b=0)  # 810 # ide do druge visnje

# strategy2.set_skip_flag(1)
# strategy2.go_to_XY(830, 2500, True, ss=0.5, bs=0, at=0,
#                    b=100)  # ako je neko na cheroima ide dalje da sortira
# strategy2.front_all_off()

# # pali zadnje senzore kada krene u rikverc unutar ovog taska
# strategy2.skip_to_flag("reset")
# strategy2.add_sequence(cherry2())  # sisa po visnjama
# strategy2.back_all_off()
# # strategy2.go_to_XY(855, 2500, False, 0.1)
# strategy2.move_vacuum(173)

# strategy2.front_all_on()  # ide po pakove
# # ide na drugu stranu, nece da sortira ako skupi sve, tek iz nje moze da predje na verzije sa 1 ili 2 unload-a
# strategy2.set_skip_flag(5)
# strategy2.add_sequence(pink2())
# strategy2.back_all_on()
# strategy2.skip_to_flag("reset")
# strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy2.back_all_off()
# strategy2.front_all_on()
# strategy2.add_sequence(yellow2())
# strategy2.set_skip_flag(6)  # skace na drugi deo terena po druge braon pakove
# strategy2.add_sequence(brown2())
# strategy2.front_all_off()

# strategy2.front_all_on()
# strategy2.go_to_XY(1675, 2650, True, ss=0.5, bs=2,
#                    at=100, b=200)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
# strategy2.add_sequence(unload1())  # izbacuje pakove
# strategy2.add_sequence(unload2())
# strategy2.add_sequence(unload3())

# strategy2.back_all_on()
# strategy2.set_skip_flag(10)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.back_all_on()
# strategy2.skip_to_flag(10)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()
# # ==================================================== SKIP StrATEGIJA pokusace da sortira

# strategy2.skip_to_flag(9)
# strategy2.vacuum_cherry(0)
# strategy2.move_vacuum(173)
# strategy2.front_all_on()

# # 1650 # zaobilazi sve pakove i ide u centar stola
# # ako detektuje u sredini nekoga ide okolo kako zna i ume
# strategy2.go_to_XY(1000, 1650, True, ss=0.5, bs=1, at=0, b=0)

# strategy2.go_to_XY(830, 2300, True, ss=0.5, bs=1, at=100,  # pokusava beskrajno da dodje do cheroa
#                    b=0)  # 810 # ide do druge visnje

# strategy2.set_skip_flag(3)
# strategy2.go_to_XY(830, 2500, True, ss=0.5, bs=0, at=0,
#                    b=100)  # ako je neko na cheroima ide dalje da sortira
# strategy2.front_all_off()

# # pali zadnje senzore kada krene u rikverc unutar ovog taska
# strategy2.add_sequence(cherry2())  # sisa po visnjama
# strategy2.back_all_off()
# # strategy2.go_to_XY(855, 2500, False, 0.1)
# strategy2.move_vacuum(175)

# strategy2.skip_to_flag(1)
# strategy2.skip_to_flag(3)
# strategy2.move_vacuum(173)
# strategy2.vacuum_cherry(0)
# strategy2.front_all_on()  # ide po pakove
# # ide na drugu stranu, pokusace da sortira ako skupi sve, tek iz nje moze da predje na verzije sa 1 ili 2 unload-a
# strategy2.set_skip_flag(4)
# strategy2.add_sequence(pink2(0, 50))
# strategy2.back_all_on()
# strategy2.skip_to_flag("reset")
# strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy2.back_all_off()
# strategy2.front_all_on()
# strategy2.add_sequence(yellow2())
# strategy2.set_skip_flag(13)  # skace na druge braon pakove
# strategy2.add_sequence(brown2())
# strategy2.front_all_off()

# strategy2.front_all_on()
# strategy2.go_to_XY(1675, 2650, True, ss=0.5, bs=2,
#                    at=100, b=200)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.check_time(55, 21)  # (sekunde, index flag-a)

# strategy2.set_distance_angle(-100, 0)
# strategy2.go_to_XY(1600, 2600, False)
# strategy2.add_sequence(sortCakes(-35))

# strategy2.back_all_on()
# strategy2.set_skip_flag(15)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.skip_to_flag(15)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# # ================================================================================
# # druga strana kvadrant 1 idalje postoji sansa za sortiranje

# strategy2.skip_to_flag(4)
# strategy2.front_all_on()  # ide po pakove
# # ide na drugu stranu, pokusace da sortira ako skupi sve, tek iz nje moze da predje na verzije sa 1 ili 2 unload-a
# strategy2.set_skip_flag(12)  # skace na BRAON 1 i JEDAN anload
# strategy2.add_sequence(pink1(0, -100))
# strategy2.back_all_on()
# strategy2.skip_to_flag("reset")
# strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy2.back_all_off()
# strategy2.front_all_on()
# strategy2.add_sequence(yellow1())
# strategy2.skip_to_flag(6)
# strategy2.skip_to_flag(13)
# strategy2.set_skip_flag(11)  # skace na opciju sa dva unload-a
# strategy2.front_all_on()  # OVDE SU DUPLO UPALJENI SENZORI
# strategy2.add_sequence(brown1())
# strategy2.front_all_off()

# strategy2.back_all_on()
# strategy2.go_to_XY(1675, 2650, False, ss=0.5, bs=2,
#                    at=100, b=200)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.check_time(55, 20)  # (sekunde, index flag-a)

# strategy2.set_distance_angle(-100, 0)
# strategy2.go_to_XY(1600, 2600, False)
# strategy2.add_sequence(sortCakes(-35))

# strategy2.back_all_on()
# strategy2.set_skip_flag(16)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.skip_to_flag(16)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# # ==========================================================================
# # skip nema sortiranja zato sto je skupio oba dispensera

# strategy2.skip_to_flag(5)
# strategy2.front_all_on()
# strategy2.set_skip_flag(14)  # skace na braon 1 sa jednim anload-om
# strategy2.add_sequence(pink1(0, -100))
# strategy2.front_all_off()
# strategy2.back_all_on()
# strategy2.skip_to_flag("reset")
# strategy2.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy2.back_all_off()
# strategy2.front_all_on()
# strategy2.add_sequence(yellow1())
# strategy2.skip_to_flag(6)
# strategy2.set_skip_flag(8)
# strategy2.add_sequence(brown1())
# strategy2.front_all_off()

# strategy2.back_all_on()
# strategy2.go_to_XY(1675, 2650, False, ss=0.5, bs=2,
#                    at=100, b=200)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.skip_to_flag(20)
# strategy2.skip_to_flag(21)
# strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
# strategy2.add_sequence(unload1())  # izbacuje pakove
# strategy2.add_sequence(unload2())
# strategy2.add_sequence(unload3())

# strategy2.back_all_on()
# strategy2.set_skip_flag(17)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.skip_to_flag(17)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# # =========================================================================
# # sa dva unload-a

# strategy2.skip_to_flag(11)
# strategy2.skip_to_flag(8)

# strategy2.front_all_on()
# strategy2.go_to_XY(1675, 2650, True, ss=0.5, bs=2,
#                    at=100, b=200)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
# strategy2.add_sequence(unload1())  # izbacuje pakove
# strategy2.add_sequence(unload3())

# strategy2.back_all_on()
# strategy2.set_skip_flag(18)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.skip_to_flag(18)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()


# # =========================================================================
# # sa jednim unloadom

# strategy2.skip_to_flag(12)
# strategy2.skip_to_flag(14)
# strategy2.front_all_on()
# strategy2.add_sequence(brown1())
# strategy2.front_all_off()

# strategy2.back_all_on()
# strategy2.go_to_XY(1675, 2650, False)  # ide do basketa
# strategy2.start_step_actions()
# strategy2.move_pipe(110)
# strategy2.end_step_actions()
# strategy2.front_all_off()
# strategy2.go_to_XY(1725, 2680, True)  # 1775 #namesta poziciju
# # strategy2.back_all_on()

# strategy2.add_sequence(unload_basket_green())

# strategy2.go_to_XY(1725, 2600, False)  # 1775 #odmakne se od basketa
# strategy2.add_sequence(unload3())

# strategy2.back_all_on()
# strategy2.set_skip_flag(19)  # zaobilazno ide do tanjura
# strategy2.go_to_XY(1600, 1200, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()

# strategy2.skip_to_flag(19)
# strategy2.back_all_on()
# strategy2.go_to_XY(1200, 2000, False, ss=0, bs=0, at=0, b=200)
# strategy2.go_to_XY(1200, 1400, False, ss=0, bs=0, at=0, b=200)
# strategy2.back_all_off()
# strategy2.go_to_XY(1600, 1200, False)
# strategy2.rotate_to(0)

# strategy2.end()
