from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

# Zuta strana 3 solarna, 4 seta biljaka zbog plus 5 na simu

strategy5 = Strategy()

strategy5.rotate_to(0)
strategy5.front_sensors_on()
strategy5.start_step_actions()
strategy5.go_to_XY(195, 800, g=0.4)  # rotira panele #y = 750
strategy5.activate_triangle()
strategy5.deactivate_prednja_grtalca()
strategy5.deactivate_zadnja_grtalca()
strategy5.add_sequence(prepare_front_arm())
strategy5.end_step_actions()

strategy5.add_points("unload", 15)

strategy5.set_skip_flag(1)

strategy5.start_step_actions()
strategy5.go_to_XY(500, 1500, off=120)  # dolazi do tanjira 4 -1210
strategy5.deactivate_triangle()
# strategy5.move_mechanism(260)
strategy5.activate_prednja_grtalca()
strategy5.end_step_actions()

strategy5.add_sequence(grip_front_plant())  # -20 #110

strategy5.front_sensors_off()
strategy5.back_sensors_on()

strategy5.skip_to_flag(1)

strategy5.start_step_actions()
strategy5.go_to_XY(1500, 1500, False, off=120)  # 1320 ide do biljaka kod sime
strategy5.add_sequence(prepare_back_arm())
strategy5.deactivate_prednja_grtalca()
# strategy5.move_mechanism(100)
strategy5.activate_zadnja_grtalca()
strategy5.end_step_actions()

# strategy5.rotate_to(90)

strategy5.add_sequence(grip_back_plant())  # 0 #-80

strategy5.start_step_actions()
strategy5.go_to_XY(1750, 762, False)  # dolazi ispred plantera
strategy5.deactivate_zadnja_grtalca()
strategy5.end_step_actions()

strategy5.back_sensors_off()

strategy5.start_step_actions()  # dolazi i priprema ruku
strategy5.go_to_XY(1820, 762)
strategy5.move_front_arm(120, v=15)
strategy5.end_step_actions()

strategy5.move_mechanism(270)  # ostavlja prednje u planter bez saksija
strategy5.move_front_arm(85, v=15)
strategy5.ungrip_front()
strategy5.move_front_arm(120, v=30)
strategy5.move_mechanism(180)

strategy5.add_points("unload", 24)

strategy5.back_sensors_on()
strategy5.go_to_XY(1382, 650, False)  # ide unapred prema sledecem planteru

strategy5.start_step_actions()  # podize ruku
strategy5.go_to_XY(1382, 185, False)  # -285
strategy5.move_back_arm(210, v=15)
strategy5.end_step_actions()

strategy5.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy5.move_back_arm(170, v=15)
strategy5.ungrip_back()
strategy5.move_back_arm(210, v=30)
strategy5.move_mechanism(180)

strategy5.add_points("unload", 24)

strategy5.back_sensors_off()
strategy5.front_sensors_on()

strategy5.start_step_actions()  # ide na sledece biljke
strategy5.go_to_XY(1300, 720)
strategy5.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy5.add_sequence(prepare_arms6())
strategy5.end_step_actions()

# strategy5.rotate_to(0)  # hvata biljke 6 komada
strategy5.add_sequence(grip3_front_plant())  # -70
strategy5.front_sensors_off()

strategy5.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA

strategy5.back_sensors_on()
# strategy5.activate_zadnja_grtalca()
strategy5.set_distance_angle(-230, 0)
strategy5.add_sequence(grip_back_plant())  # 130
# strategy5.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy5.rotate_to(-90)

strategy5.back_sensors_off()
strategy5.front_sensors_on()

strategy5.go_to_XY(612, 600)  # ide da ih ostavi kako zna i ume
strategy5.start_step_actions()
strategy5.go_to_XY(612, 285)  # 350
strategy5.move_front_arm(120, v=15)  # podize ruku
strategy5.end_step_actions()

strategy5.front_sensors_off()

strategy5.rotate_to(180)
# strategy5.set_distance_angle(-10, 0)
strategy5.move_mechanism(220)  # 180
strategy5.move_front_arm(100, v=30)  # 100
strategy5.ungrip_front()
strategy5.move_front_arm(110, v=30)

strategy5.start_step_actions()
strategy5.set_distance_angle(-100, 0)
strategy5.grip_front()
strategy5.deactivate_zadnja_grtalca()
strategy5.end_step_actions()


strategy5.move_back_arm(210, v=30)
strategy5.go_to_XY(624, 300, False)  # 285
# strategy5.move_back_arm(190, v=15)
strategy5.move_mechanism(200)  # izbaci ruku
strategy5.move_back_arm(180, v=30)
strategy5.ungrip_back()
strategy5.move_back_arm(210, v=30)

strategy5.deactivate_zadnja_grtalca(20, 20)
strategy5.set_distance_angle(-50, 0)
strategy5.set_distance_angle(0, -90, g=0.3)  # zatorira ka tanjiru
strategy5.set_distance_angle(-100, 0, g=0.5)  # udje u tanjur
strategy5.deactivate_zadnja_grtalca()

strategy5.add_points("unload", 20)

strategy5.set_distance_angle(100, 0)
strategy5.move_mechanism(180)

strategy5.front_sensors_on()

strategy5.start_step_actions()  # ide da zgrne poslednje
strategy5.go_to_XY(700, 1000, off=120)
strategy5.activate_prednja_grtalca()
strategy5.move_mechanism(280)
strategy5.end_step_actions()

strategy5.move_front_arm(75, v=30)  # uhvati poslednje biljke


strategy5.go_to_XY(1500, 400)  # ide kuci i podize ruku

strategy5.start_parallel()
strategy5.move_front_arm(120, v=10)
strategy5.deactivate_prednja_grtalca()
strategy5.move_mechanism(180)
strategy5.end_parallel()

strategy5.add_points("unload", 16)

strategy5.all_off()

strategy5.end()
