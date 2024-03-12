from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy4 = Strategy()

strategy4.rotate_to(0)
strategy4.front_sensors_on()
strategy4.start_step_actions()
strategy4.go_to_XY(195, 1200, g=0.4)  # rotira panele #y = 750
strategy4.activate_triangle()
strategy4.deactivate_prednja_grtalca()
strategy4.deactivate_zadnja_grtalca()
strategy4.end_step_actions()

strategy4.start_step_actions()
strategy4.go_to_XY(195, 1850, g=0.4)
strategy4.add_sequence(prepare_arms6())  # priprema za hvatanje
strategy4.end_step_actions()

strategy4.deactivate_triangle()

strategy4.start_step_actions()
strategy4.go_to_XY(500, 1500, off=290)  # dolazi do tanjira 4 -1210
strategy4.move_mechanism(260)
strategy4.activate_prednja_grtalca()
strategy4.end_step_actions()


# strategy4.start_step_actions()
# strategy4.rotate_to(0)  # uzima biljke iz donjeg tanjira
# strategy4.end_step_actions()
strategy4.add_sequence(grip_front_plant(110))  # -20

strategy4.front_sensors_off()
strategy4.back_sensors_on()

strategy4.start_step_actions()
strategy4.go_to_XY(1270, 1500, False)  # 1320 ide do biljaka kod sime
strategy4.deactivate_prednja_grtalca()
strategy4.move_mechanism(100)
strategy4.activate_zadnja_grtalca()
strategy4.end_step_actions()

strategy4.rotate_to(90)

strategy4.add_sequence(grip_back_plant(-80))  # 0

strategy4.start_step_actions()
strategy4.go_to_XY(1750, 762, False)  # dolazi ispred plantera
strategy4.deactivate_zadnja_grtalca()
strategy4.end_step_actions()

strategy4.back_sensors_off()

strategy4.start_step_actions()  # dolazi i priprema ruku
strategy4.go_to_XY(1850, 762)
strategy4.move_front_arm(120, v=15)
strategy4.end_step_actions()

strategy4.move_mechanism(270)  # ostavlja prednje u planter bez saksija
strategy4.move_front_arm(85, v=15)
strategy4.ungrip_front()
strategy4.move_front_arm(120)
strategy4.move_mechanism(180)

strategy4.back_sensors_on()
strategy4.go_to_XY(1382, 650, False)  # ide unapred prema sledecem planteru

strategy4.start_step_actions()  # podize ruku
strategy4.go_to_XY(1382, 185, False)  # -285
strategy4.move_back_arm(210, v=15)
strategy4.end_step_actions()

strategy4.move_mechanism(20)  # ostavlja biljke u drugi plenter
strategy4.move_back_arm(167, v=15)
strategy4.ungrip_back()
strategy4.move_back_arm(210, v=30)
strategy4.move_mechanism(180)

strategy4.back_sensors_off()
strategy4.front_sensors_on()

strategy4.start_step_actions()  # ide na sledece biljke
strategy4.go_to_XY(1300, 700)
strategy4.rotate_to(3)  # OVO IZVADITI AKO IDEMO NA 3 TANJIRA
strategy4.add_sequence(prepare_arms6())
strategy4.end_step_actions()

# strategy4.rotate_to(0)  # hvata biljke 6 komada
strategy4.add_sequence(grip_front_plant())  # -70
strategy4.set_distance_angle(-60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy4.front_sensors_off()

strategy4.rotate_to(180)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA

strategy4.back_sensors_on()
strategy4.activate_zadnja_grtalca()
strategy4.add_sequence(grip_back_plant())  # 130
# strategy4.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy4.rotate_to(-90)

strategy4.back_sensors_off()
strategy4.front_sensors_on()

strategy4.go_to_XY(612, 600)  # ide da ih ostavi kako zna i ume
strategy4.start_step_actions()
strategy4.go_to_XY(612, 285)  # 350
strategy4.move_front_arm(120, v=15)  # podize ruku
strategy4.end_step_actions()

strategy4.front_sensors_off()

strategy4.rotate_to(180)
# strategy4.set_distance_angle(-10, 0)
strategy4.move_mechanism(230)  # 180
strategy4.move_front_arm(80, v=30)
strategy4.ungrip_front()
strategy4.move_front_arm(110, v=30)

strategy4.start_step_actions()
strategy4.set_distance_angle(-220, 0)
strategy4.grip_front()
strategy4.end_step_actions()


strategy4.move_back_arm(210, v=30)
strategy4.go_to_XY(600, 325, False)  # 285
# strategy4.move_back_arm(190, v=15)
strategy4.move_mechanism(190)  # izbaci ruku
strategy4.move_back_arm(170, v=30)
strategy4.ungrip_back()
strategy4.move_back_arm(210, v=30)

strategy4.set_distance_angle(-20, 0, g=0.5)
strategy4.set_distance_angle(0, -90, g=0.3)  # zatorira ka tanjiru
strategy4.set_distance_angle(-100, 0, g=0.5)  # udje u tanjur
# strategy4.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
strategy4.deactivate_zadnja_grtalca()
strategy4.move_mechanism(180)
# # strategy4.set_distance_angle(-100, 0)
# # strategy4.rotate_to(-90)  # zarotira

# strategy4.add_sequence(release_back_plant())  # ostavi i zadnje bilje

# vraca se kuci skloniti false ako ostavlja dva seta (6 ili 3)
strategy4.front_sensors_on()

strategy4.start_step_actions()
strategy4.go_to_XY(1500, 400)
strategy4.add_sequence(init_servos())
strategy4.end_step_actions()

strategy4.all_off()

strategy4.end()
