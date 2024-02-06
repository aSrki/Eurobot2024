from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy1 = Strategy()

# # plavi tanjir kvadrant 1

# strategy1.lift_cakes(10)

strategy1.front_all_off()  # ide da usisava
strategy1.back_all_on()
strategy1.set_skip_flag(1)  # ide na dispenser 2
strategy1.go_to_XY(1820, 1270, False, ss=0.5, bs=0, at=0, b=0)
strategy1.skip_to_flag("reset")
strategy1.back_all_off()
strategy1.front_all_on()
strategy1.add_sequence(cherry1())  # sisa po visnjama

strategy1.go_to_XY(1820, 1900, True, ss=0.5, bs=0, at=0,
                   b=50)  # odmakne se od dispensera
strategy1.move_vacuum(173)

# ide do pinka 1
strategy1.go_to_XY(1300, 2500, True, ss=0.5, bs=2, at=100, b=100)

strategy1.set_skip_flag(3)
strategy1.front_all_on()  # ide po pakove
strategy1.add_sequence(pink1())
strategy1.skip_to_flag("reset")
strategy1.front_all_off()
strategy1.back_all_on()
strategy1.set_distance_angle(-200, 0, ss=0, bs=1, at=1, b=0)
strategy1.back_all_off()
strategy1.front_all_on()
strategy1.add_sequence(yellow1())
strategy1.set_skip_flag(10)  # ide na drugi set braona preko puta
strategy1.add_sequence(brown1())
strategy1.front_all_off()

strategy1.front_all_on()  # dodje do basketa
strategy1.go_to_XY(250, 2680, True, ss=0.5, bs=2, at=100, b=200)  # 225, 2700
strategy1.front_all_off()

strategy1.add_sequence(unload_basket_blue())

strategy1.go_to_XY(250, 2650, False)  # odmakne se od basketa
strategy1.check_time(60)

strategy1.go_to_XY(400, 2600, False)
strategy1.add_sequence(sortCakes(40))

strategy1.move_door(190)
strategy1.move_pipe(170)
strategy1.check_time(1, "timeout")

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.go_to_XY(800, 1500, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()
# strategy1.go_to_XY(450, 1375, False)

# strategy1.end()

# =============================================================ide na drugi dispenzer
# ide na drugi dispenser

strategy1.skip_to_flag(1)
strategy1.front_all_on()
strategy1.go_to_XY(1820, 1850, True, ss=0.5, bs=0, at=0,
                   b=50)  # odmakne se od dispensera
strategy1.move_vacuum(173)

# ide do drugog dispensera
strategy1.go_to_XY(860, 2400, True, ss=0.5, bs=2, at=100, b=100)

# OVO VODI NA PARALELNU OD MOMENTA PINK 2 I Pokusace da sortira ako detektuje
strategy1.set_skip_flag(4)
strategy1.go_to_XY(860, 2600, True, g=0.7, ss=0.5, bs=0, at=0, b=0)
strategy1.front_all_off()

# sisa po drugoj visnji, ovde se pale zadnji senzori unutar taska
strategy1.add_sequence(cherry2())
strategy1.back_all_off()

strategy1.skip_to_flag(3)
strategy1.skip_to_flag(4)
strategy1.move_vacuum(173)
strategy1.front_all_on()  # ide po pakove
strategy1.set_skip_flag(9)
strategy1.add_sequence(pink2(0, 0, attempts=100))
strategy1.skip_to_flag("reset")
strategy1.front_all_off()
strategy1.back_all_on()
strategy1.set_distance_angle(-200, 0, ss=0, bs=1, at=1, b=0)
strategy1.back_all_off()
strategy1.front_all_on()
strategy1.add_sequence(yellow2())  # 0, 60
# ovde dolazi iz druge strane stola pokusava zaobici robota
strategy1.skip_to_flag(10)
strategy1.front_all_on()
strategy1.go_to_XY(725, 2300, True, ss=0.5, bs=0, at=0, b=200)
strategy1.skip_to_flag(9)  # ovde skace
strategy1.front_all_on()
strategy1.add_sequence(brown2())  # 0, 60
strategy1.front_all_off()

strategy1.back_all_on()  # dodje do basketa
strategy1.go_to_XY(250, 2680, False, ss=0.5, bs=2, at=100, b=200)  # 225, 2700
strategy1.start_step_actions()
strategy1.move_pipe(170)
strategy1.end_step_actions()
strategy1.front_all_off()

strategy1.add_sequence(unload_basket_blue())

strategy1.go_to_XY(250, 2650, False)  # odmakne se od basketa
strategy1.check_time(60)

strategy1.go_to_XY(400, 2600, False)
strategy1.add_sequence(sortCakes(40))

strategy1.move_door(190)
strategy1.move_pipe(170)
strategy1.check_time(1, "timeout")

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.go_to_XY(800, 1500, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()
# strategy1.go_to_XY(450, 1375, False)

# strategy1.end()

# ===================NOSORT NO SOET NE SORTIRA NIKAKOOOOO NE SME

strategy1.skip_to_flag("unload_3")
strategy1.add_sequence(unload1())  # izbaci pakove
strategy1.skip_to_flag("unload_2")
strategy1.add_sequence(unload2())
strategy1.skip_to_flag("unload_1")
strategy1.add_sequence(unload3())
strategy1.skip_to_flag("unload_0")

strategy1.move_door(190)
strategy1.move_pipe(170)
strategy1.check_time(1, "timeout")

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_door(180)
# strategy1.go_to_XY(800, 1500, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()
# strategy1.go_to_XY(450, 1375, False)

# strategy1.end()

# ==================================================TAJMAOUT

strategy1.skip_to_flag("timeout")
strategy1.back_all_on()  # izlazenje iz tanjira
strategy1.grip_cakes(48)
strategy1.move_pipe(170)
strategy1.go_to_XY(1000, 1600, False, ss=0, bs=0.2, at=100, b=10, ns=0)
strategy1.back_all_off()
strategy1.go_to_XY(300, 1400, False, ss=0, bs=0.1, at=100, b=0)

strategy1.end()

# strategy1.front_all_off()  # ide da usisava
# strategy1.back_all_on()
# strategy1.set_skip_flag(9)  # ako detektuje ovde ide da soritra
# strategy1.go_to_XY(1820, 1270, False, ss=0.5, bs=0, at=0, b=0)
# strategy1.skip_to_flag("reset")
# strategy1.back_all_off()
# strategy1.front_all_on()
# strategy1.add_sequence(cherry1())  # sisa po visnjama

# strategy1.go_to_XY(1820, 1850, True, ss=0.5, bs=0, at=0,
#                    b=50)  # odmakne se od dispensera
# strategy1.move_vacuum(173)

# # ide do drugog dispensera
# strategy1.go_to_XY(850, 2500, True, ss=0.5, bs=2, at=100, b=100)

# # OVO VODI NA PARALELNU OD MOMENTA PINK 2 I Pokusace da sortira
# strategy1.set_skip_flag(1)
# strategy1.go_to_XY(850, 2600, True, ss=0.5, bs=0.5, at=0, b=100)
# strategy1.front_all_off()

# # sisa po drugoj visnji, ovde se pale zadnji senzori unutar taska
# strategy1.set_skip_flag(5)
# strategy1.add_sequence(cherry2())
# strategy1.move_vacuum(173)
# strategy1.back_all_off()

# # strategy1.grip_cakes(82) #protiv upadanje cherija u plocu

# strategy1.front_all_on()  # ide po pakove
# strategy1.add_sequence(pink1())
# strategy1.front_all_off()
# strategy1.back_all_on()
# strategy1.skip_to_flag("reset")
# strategy1.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy1.back_all_off()
# strategy1.front_all_on()
# strategy1.add_sequence(yellow1())
# strategy1.set_skip_flag(2)
# strategy1.add_sequence(brown1())
# strategy1.front_all_off()

# strategy1.front_all_on()  # dodje do basketa
# strategy1.go_to_XY(250, 2680, True, ss=0.5, bs=2, b=200, at=100)  # 225, 2700
# strategy1.start_step_actions()
# strategy1.move_pipe(110)
# strategy1.end_step_actions()
# strategy1.front_all_off()

# strategy1.add_sequence(unload_basket_blue())

# strategy1.go_to_XY(250, 2600, False)  # odmakne se od basketa
# strategy1.add_sequence(unload1())  # izbaci pakove
# strategy1.add_sequence(unload2())
# strategy1.add_sequence(unload3())

# # strategy1.set_distance_angle(-100, 0)
# # strategy1.go_to_XY(400, 2600, False)
# # strategy1.add_sequence(sortCakes(35))

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.set_skip_flag(3)
# strategy1.go_to_XY(225, 1375, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()

# strategy1.skip_to_flag(3)
# strategy1.back_all_on()
# strategy1.go_to_XY(600, 2300, False)  # tajmaut
# strategy1.go_to_XY(450, 1375, False)
# strategy1.back_all_off()

# strategy1.end()

# # =======================================================================
# # SKIP STRAT 1

# strategy1.skip_to_flag(9)
# strategy1.add_sequence(cherry1())
# strategy1.front_all_on()
# strategy1.go_to_XY(1820, 1850, True, ss=0.5, bs=0, at=0,
#                    b=50)  # odmakne se od dispensera
# strategy1.move_vacuum(173)

# # ide do drugog dispensera
# strategy1.go_to_XY(850, 2500, True, ss=0.5, bs=2, at=100, b=100)

# # OVO VODI NA PARALELNU OD MOMENTA PINK 2 I Pokusace da sortira ako detektuje
# strategy1.set_skip_flag(4)
# strategy1.go_to_XY(850, 2600, True, ss=0.5, bs=0, at=0, b=0)
# strategy1.front_all_off()

# # sisa po drugoj visnji, ovde se pale zadnji senzori unutar taska
# strategy1.add_sequence(cherry2())
# strategy1.move_vacuum(173)
# strategy1.back_all_off()

# strategy1.skip_to_flag(4)
# strategy1.skip_to_flag(1)
# strategy1.front_all_on()  # ide po pakove
# strategy1.set_skip_flag(10)
# strategy1.add_sequence(pink2(0, 60))
# strategy1.front_all_off()
# strategy1.back_all_on()
# strategy1.skip_to_flag("reset")
# strategy1.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy1.back_all_off()
# strategy1.front_all_on()
# strategy1.add_sequence(yellow2(0, 60))
# strategy1.set_skip_flag(11)
# strategy1.add_sequence(brown2(0, 60))
# strategy1.front_all_off()

# strategy1.skip_to_flag("reset")
# strategy1.front_all_on()  # dodje do basketa
# strategy1.go_to_XY(250, 2680, True, ss=0.5, bs=2, b=200, at=100)  # 225, 2700
# strategy1.start_step_actions()
# strategy1.move_pipe(110)
# strategy1.end_step_actions()
# strategy1.front_all_off()

# strategy1.add_sequence(unload_basket_blue())

# strategy1.set_distance_angle(-100, 0)
# strategy1.go_to_XY(400, 2600, False)
# strategy1.add_sequence(sortCakes(35))

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.set_skip_flag(7)
# strategy1.go_to_XY(225, 1375, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()

# strategy1.skip_to_flag(7)
# strategy1.back_all_on()
# strategy1.go_to_XY(600, 2300, False)  # tajmaut
# strategy1.go_to_XY(450, 1375, False)
# strategy1.back_all_off()

# strategy1.end()


# # =======================================================================
# # SKIP STRAT 2 NEMA SORTA,
# # sluzi za menjanje pakova koje uzima ako detektuje nekoga kod prvih pakova

# strategy1.skip_to_flag(5)
# strategy1.move_vacuum(173)
# strategy1.front_all_on()
# strategy1.set_skip_flag(8)
# strategy1.add_sequence(pink2(0, 100))
# strategy1.front_all_off()
# strategy1.back_all_on()
# strategy1.skip_to_flag("reset")
# strategy1.set_distance_angle(-200, 0, ss=0, bs=0, at=0, b=0)
# strategy1.back_all_off()
# strategy1.front_all_on()
# strategy1.add_sequence(yellow2(0, 60))
# strategy1.set_skip_flag(2)
# strategy1.add_sequence(brown2(0, 60))
# strategy1.front_all_off()

# strategy1.skip_to_flag("reset")
# strategy1.back_all_on()  # dodje do basketa
# strategy1.go_to_XY(250, 2680, False, ss=0.5, bs=2, b=200, at=100)  # 225, 2700
# strategy1.start_step_actions()
# strategy1.move_pipe(110)
# strategy1.end_step_actions()
# strategy1.back_all_off()

# strategy1.add_sequence(unload_basket_blue())

# strategy1.go_to_XY(250, 2650, False)  # odmakne se od basketa
# strategy1.add_sequence(unload1())  # izbaci pakove
# strategy1.add_sequence(unload2())
# strategy1.add_sequence(unload3())

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.set_skip_flag(6)
# strategy1.go_to_XY(225, 1375, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()

# strategy1.skip_to_flag(6)
# strategy1.back_all_on()
# strategy1.go_to_XY(600, 2300, False)  # tajmaut
# strategy1.go_to_XY(450, 1375, False)
# strategy1.back_all_off()

# strategy1.end()

# # =======================================================================
# # SA DVA UNLOAD-a
# strategy1.skip_to_flag(11)
# strategy1.skip_to_flag(2)
# strategy1.back_all_on()  # dodje do basketa
# strategy1.skip_to_flag("reset")
# strategy1.go_to_XY(250, 2680, False, ss=0.5, bs=2, b=200, at=100)  # 225, 2700
# strategy1.start_step_actions()
# strategy1.move_pipe(110)
# strategy1.end_step_actions()
# strategy1.back_all_off()

# strategy1.add_sequence(unload_basket_blue())

# strategy1.go_to_XY(250, 2600, False)  # odmakne se od basketa
# strategy1.add_sequence(unload1())
# strategy1.add_sequence(unload3())  # izbaci pakove

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.set_skip_flag(6)
# strategy1.go_to_XY(225, 1375, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()

# strategy1.skip_to_flag(6)
# strategy1.back_all_on()
# strategy1.go_to_XY(600, 2300, False)  # tajmaut
# strategy1.go_to_XY(450, 1375, False)
# strategy1.back_all_off()

# # OVDE IMA VREMENSKOG MESTA ZA KRADJU

# strategy1.end()

# # ==========================================================================
# # SA JEDNIM UNLOAD-om
# strategy1.set_skip_flag(10)
# strategy1.skip_to_flag(8)
# strategy1.front_all_on()
# strategy1.add_sequence(brown2(0, 60))
# strategy1.front_all_off()

# strategy1.skip_to_flag("reset")
# strategy1.back_all_on()  # dodje do basketa
# strategy1.go_to_XY(250, 2680, False, ss=0.5, bs=2, b=200, at=100)  # 225, 2700
# strategy1.start_step_actions()
# strategy1.move_pipe(110)
# strategy1.end_step_actions()
# strategy1.back_all_off()

# strategy1.add_sequence(unload_basket_blue())

# strategy1.go_to_XY(250, 2600, False)  # odmakne se od basketa
# strategy1.add_sequence(unload1())  # izbaci pakove

# strategy1.back_all_on()  # izlazenje iz tanjira
# strategy1.move_pipe(110)
# strategy1.move_door(180)
# strategy1.set_skip_flag(6)
# strategy1.go_to_XY(225, 1375, False, ss=0.5, at=0, b=100)
# strategy1.back_all_off()

# strategy1.skip_to_flag(6)
# strategy1.back_all_on()
# strategy1.go_to_XY(600, 2300, False)  # tajmaut
# strategy1.go_to_XY(450, 1375, False)
# strategy1.back_all_off()

# # OVDE IMA VREMENSKOG MESTA ZA KRADJU

# strategy1.end()

# plavi tanjir kvadrant 1
# NOVA STRATEGIJA ===============================================NOVA NOVA NOVA NOVA


# strategy1.rotate_to(5, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(10, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(25, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(45, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(90, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(135, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(180, s= 0)
# strategy1.rotate_to(0, s= 0)
# strategy1.rotate_to(270)
# strategy1.rotate_to(0)

# strategy1.go_to_XY(3, 2003, True)
# strategy1.go_to_XY(3, 3, False)
# strategy1.go_to_XY(3, 1503, True)
# strategy1.go_to_XY(3, 3, False)
# strategy1.go_to_XY(3, 1003, True)
# strategy1.go_to_XY(3, 3, False)
# strategy1.go_to_XY(3, 503, True)
# strategy1.go_to_XY(3, 3, False)
# strategy1.go_to_XY(3, 203, True)
# strategy1.go_to_XY(3, 3, False)
# strategy1.go_to_XY(3, 103, True)
# strategy1.go_to_XY(3, 3, False)


# strategy1.go_to_XY(3, 1003, True)
# strategy1.go_to_XY(-1003, 1003, True)
# strategy1.go_to_XY(-1003, 3, True)
# strategy1.go_to_XY(3, 3, True)
# strategy1.rotate_to(0, 0)
# =========================================================
# =========================================================
# strategy1.go_to_XY(3, 1003, True, 2)
# strategy1.go_to_XY(3, 3, False)

# strategy1.rotate_to(180, 4)
# strategy1.rotate_to(0, 0)

# strategy1.rotate_to(180, 3)
# strategy1.rotate_to(0, 0)

# strategy1.add_sequence(collectCherries())

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.execute_operations = OperationExecution.WHILE_MOVE
# start_ruku(step)
# step.angle = 0
# step.distance = 180
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 240
# step.y = 690
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 5
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 180
# step.y = 1200
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 0
# strategy1.append(step)

# doda korake za obaranje otpornosti u niz
# for i in range(0, 7):
#     step = Step()
#     step.type_of_parameters = TypesOfSendParameters.COORDINATE
#     if i == 0:
#         step.execute_operations = OperationExecution.WHILE_MOVE
#         start_ruku(step)
#     step.x = 200 - (4*i)  # 250
#     step.y = 670 + i*181  # 1775 #669
#     step.use_skip = 1
#     step.distance_when_backing = 150 - i*12.5
#     step.stop_sleep = 0.5  # sleep pri stajanju u sec
#     step.backing_sleep = 1  # sleep pri vracanju nazad u sec
#     step.sensor = all.FRONT_ON
#     strategy1.append(step)

#     step = Step()
#     step.type_of_parameters = TypesOfSendParameters.ANGLE
#     step.use_skip = 1
#     step.angle = 0
#     strategy1.append(step)

#     step = Step()
#     step.type_of_parameters = TypesOfSendParameters.NEITHER
#     operation_append(step, 151, 1, 0.1, i)
#     step.use_skip = 1
#     if i == 3:
#         step.skip_steps = 6
#     strategy1.append(step)


# # pripremi se za skupljanje 3 random paka
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 650
# step.skip_flag = 1
# step.y = 1450
# step.sensor = all.FRONT_ON
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 180
# strategy1.append(step)

# # prodje kroz 3 random paka polako
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.WHILE_MOVE
# step.translate_pojacanje = .4
# step.sensor = all.FRONT_ON
# drzi_3_paka(step)
# step.x = 600
# step.y = 650
# strategy1.append(step)

# # okrene se ka mestu za guranje
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 135
# step.sensor = all.FRONT_ON
# step.rotate_pojacanje = 0.6
# strategy1.append(step)

# # skupi ruke kako ne bi udario gore
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# start_ruku2(step)
# strategy1.append(step)

# # pridje
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.WHILE_MOVE
# step.x = 380
# step.y = 320
# strategy1.append(step)

# # zarotira se kako bi bio paralelan sa preckom
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 135
# strategy1.append(step)

# # udje jos malo
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.angle = 0
# step.distance = 15
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# operation_append(step, 35, 270, 1.8)
# operation_append(step, 35, 0, 1.8)
# strategy1.append(step)


# # pripremi ruke za skupljanje 2 paka sa visine
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# step.sensor = all.ALL_OFF
# skupi_pak_sa_visine(step)
# strategy1.append(step)

# # #odalji se kako bi mogao da skupi pakove sa visine
# # step = Step()
# # step.type_of_parameters = TypesOfSendParameters.COORDINATE
# # step.direction_is_forward = False
# # step.x = 420
# # step.y = 380
# # strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.angle = 0
# step.distance = -130
# step.sensor = all.BACK_ON
# strategy1.append(step)

# # zarotira se ka desnom i uzme ga
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 124
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.angle = 0
# step.distance = 65
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# zaleip_pak_sa_visine_desna(step)
# strategy1.append(step)


# # zarotira se ka desnom i uzme ga
# # step = Step()
# # step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# # step.angle = 35
# # step.distance = 1
# # strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 156
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# zaleip_pak_sa_visine_leva(step)
# strategy1.append(step)


# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.direction_is_forward = False
# step.x = 550
# step.y = 480
# step.skip_flag = 1
# strategy1.append(step)

# # zalepi ruke za 2 paka na podu
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# utovarivanje_paka_sa_visine_leva(step)
# strategy1.append(step)

# # zalepi ruke za 2 paka na podu
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# utovarivanje_paka_sa_visine_desna(step)
# strategy1.append(step)


# # dodje do baze sa strane
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 890
# step.y = 320
# strategy1.append(step)

# # poravna se kako treba
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = -120
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.angle = 0
# step.distance = 90
# strategy1.append(step)

# # izbaci pakove
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# izbacivanje_desnog_donjeg_paka(step)
# strategy1.append(step)

# # poravna se kako treba
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = -90
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.angle = 0
# step.distance = -60
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# izbacivanje_levog_donjeg_paka(step)
# strategy1.append(step)

# # poravna se kako treba
# # step = Step()
# # step.type_of_parameters = TypesOfSendParameters.ANGLE
# # step.angle = -90
# # strategy1.append(step)

# # ode malo u nazad kako ne bi udario pakove
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.WHILE_MOVE
# start_ruku(step)
# step.direction_is_forward = False
# step.x = 580
# step.y = 285
# strategy1.append(step)

# # skupi ruke radi kretanja
# step = Step()
# step.execute_operations = OperationExecution.WHILE_MOVE
# step.sensor = all.FRONT_ON
# step.x = 1090  # 1155
# step.y = 600
# start_ruku(step)
# strategy1.append(step)

# # orijentise se ka 3 paka sa poznatom pozicijom
# step = Step()
# step.angle = -30
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.sensor = all.FRONT_ON
# strategy1.append(step)

# # zalepi ruke za 2 paka na podu
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.execute_operations = OperationExecution.AFTER
# step.angle = 0
# step.distance = 225
# step.sensor = all.FRONT_ON
# zalepi_pakove(step)
# strategy1.append(step)

# # utovari ih u sebe
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# utovarivanje_pakova(step)
# strategy1.append(step)


# # okrene se ka trecem preostalom paku
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.distance = 60
# step.angle = 0
# step.sensor = all.FRONT_ON
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = -70
# # step.sensor = all.FRONT_ON
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.distance = 270
# step.angle = 0
# step.sensor = all.FRONT_ON
# strategy1.append(step)


# # uhvati i utovari ga
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# hvatanje_sa_stola_lijeva_2(step)
# strategy1.append(step)


# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# # step.sensor = all.FRONT_ON
# step.x = 1430
# step.y = 300
# strategy1.append(step)

# # poravna se i izbaci pakove iz sebe
# step = Step()
# step.angle = 180
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.execute_operations = OperationExecution.AFTER
# izbacivanje_levog_donjeg_paka(step)
# strategy1.append(step)

# # izadje malo i izbaci 3ci pak iz sebe
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.AFTER
# step.direction_is_forward = False
# step.x = 1430
# step.y = 465
# izbacivanje_desnog_donjeg_paka(step)
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# utovari_sa_stola_leva(step)
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.direction_is_forward = False
# step.x = 1430
# step.y = 620
# izbacivanje_levog_donjeg_paka(step)
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.execute_operations = OperationExecution.AFTER
# start_ruku(step)
# # operation_append(step, 15, 220, 0.1, 1000)
# # operation_append(step, 16, 220, 0.1, 1000)
# step. angle = 90
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# step.execute_operations = OperationExecution.WHILE_MOVE
# step.distance = 300
# step.angle = 0
# strategy1.append(step)


#### --------------------------------------------------------####
# step = Step()
# step.angle = -90
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy1.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.NEITHER
# operation = Operation()
# operation.angle = 55
# operation.servo_ID = 29
# operation.time = 0.2
# step.operations.append(operation)
# strategy0.append(step)


#
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 3
# step.y = 900
# strategy0.append(step)
#
#
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.direction_is_forward = False
# step.x = 3
# step.y = 3
# strategy0.append(step)
#
#
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.x = 3
# step.y = 900
# strategy0.append(step)
#
#
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.direction_is_forward = False
# step.x = 3
# step.y = 3
# strategy0.append(step)
#
# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.angle = 0
# strategy0.append(step)


# ************************ TEODOR

# step = Step()
# step.y = 1400
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 800
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 400
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 300
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 200
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 100
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
#
# step = Step()
# step.y = 50
# step.x = 3
# strategy0.append(step)
#
# step = Step()
# step.x = 3
# step.y = 3
# step.direction_is_forward = False
# strategy0.append(step)
# ************************************
# step = Step()
# step.angle = 0
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
#
# ROTACIJA
# step = Step()
# step.angle = 170
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
#
# step = Step()
# step.angle = 250
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
#
# step = Step()
# step.angle = 300
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
# step = Step()
# step.angle = 330
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
#
# step = Step()
# step.angle = 350
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
#
# step = Step()
# step.angle = 0
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# strategy0.append(step)
