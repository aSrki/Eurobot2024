from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy2 = Strategy()

strategy2.rotate_to(0)
strategy2.start_step_actions()
strategy2.go_to_XY(195, -750, False, g=0.4, s=1.5)  # rotira panele #y = 750
strategy2.activate_triangle()
strategy2.end_step_actions()
# strategy2.move_front_arm(110)  # podize ruke da ne pojebe potove

strategy2.start_step_actions()
strategy2.go_to_XY(500, -1210, False)  # dolazi do tanjira 4
strategy2.deactivate_triangle()
strategy2.add_sequence(prepare_arms6())  # priprema za hvatanje
strategy2.end_step_actions()


strategy2.rotate_to(0)  # uzima biljke iz donjeg tanjira
strategy2.move_mechanism(130)
strategy2.add_sequence(grip_back_plant(-50))

strategy2.go_to_XY(1320, -1500)  # ide do biljaka kod sime
strategy2.rotate_to(-90)
strategy2.move_mechanism(230)
strategy2.add_sequence(grip_front_plant())

# strategy2.start_step_actions()
# strategy2.move_front_arm(120, v=15)
# strategy2.go_to_XY(612, -285)  # 350
# strategy2.end_step_actions()

strategy2.go_to_XY(1700, -762)  # dolazi ispred plantera

strategy2.start_step_actions()  # dolazi i priprema ruku
strategy2.move_back_arm(210, v=15)
strategy2.go_to_XY(1850, -762, False)
strategy2.end_step_actions()

strategy2.move_mechanism(90)  # ostavlja zadnje u planter bez saksija
strategy2.move_back_arm(175, v=15)
strategy2.grip_back(120, 120, 120)
strategy2.move_back_arm(210)
strategy2.move_mechanism(180)

strategy2.go_to_XY(1382, -600)  # ide unapred prema sledecem planteru

strategy2.start_step_actions()  # podize ruku
strategy2.move_front_arm(120, v=15)
strategy2.go_to_XY(1382, -195)  # -285
strategy2.end_step_actions()

strategy2.move_mechanism(340)  # ostavlja biljke u drugi plenter
strategy2.move_front_arm(80, v=15)
strategy2.grip_front(120, 120, 120, s=0.1)
strategy2.move_front_arm(120, v=30)
strategy2.move_mechanism(180)

strategy2.start_step_actions()  # ide na sledece biljke
strategy2.go_to_XY(1300, -700)
strategy2.add_sequence(prepare_arms6())
strategy2.end_step_actions()

strategy2.rotate_to(180)  # hvata biljke 6 komada
strategy2.add_sequence(grip_front_plant())
strategy2.set_distance_angle(-60, 0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy2.rotate_to(0)  # OVO IZVADITI AKO IDEMO NA 4 TANJIRA
strategy2.add_sequence(grip_back_plant())
# strategy2.go_to_XY(980, -1000, False)  # pa na jos 6 komada
# strategy2.rotate_to(-90)

strategy2.go_to_XY(612, -600)  # ide da ih ostavi kako zna i ume
strategy2.start_step_actions()
strategy2.move_front_arm(120, v=15)  # podize ruku
strategy2.go_to_XY(612, -285)  # 350
strategy2.end_step_actions()

strategy2.move_back_arm(190, v=15)
strategy2.move_mechanism(270)  # izbaci ruku
strategy2.move_front_arm(80, v=30)
strategy2.grip_front(120, 120, 120)
strategy2.move_front_arm(120, v=30)
strategy2.set_distance_angle(-100, 0)
strategy2.rotate_to(180)
strategy2.set_distance_angle(-100, 0)
strategy2.move_mechanism(180)
strategy2.move_back_arm(170, v=30)
strategy2.grip_back(120, 120, 120)
strategy2.move_back_arm(210, v=30)
strategy2.set_distance_angle(100, 0)
strategy2.grip_back(215, 215, 215)
strategy2.move_back_arm(165, v=30)
strategy2.set_distance_angle(-60, 0)
strategy2.move_mechanism(60)
strategy2.move_mechanism(180)
strategy2.set_distance_angle(0, 90)
strategy2.grip_back(190, 190, 190)
strategy2.set_distance_angle(0, 90)
strategy2.grip_front(215, 215, 215)
strategy2.move_back_arm(190, v=30)
strategy2.move_mechanism(340)
strategy2.move_mechanism(180)
strategy2.set_distance_angle(0, 90, g=0.5)
strategy2.grip_front(190, 190, 190)

# strategy2.move_front_arm(90, v=30)  # spusta bilje
# strategy2.grip_front(120, 120, 120)  # ispusti ih iz saka
# strategy2.grip_front(215, 215, 215)  # zatvori sake
# strategy2.move_mechanism(320)  # pruzi ruku
# strategy2.move_front_arm(75, v=30)  # obgrli biljke
# strategy2.set_distance_angle(-150, 0)  # ode unazad
# strategy2.set_distance_angle(0, 90, g=0.5)  # zatorira ka tanjiru
# strategy2.set_distance_angle(200, 0)  # udje u tanjur
# strategy2.move_front_arm(120, s=0.5, v=30)  # ostavi biljke
# strategy2.set_distance_angle(-100, 0)
# strategy2.rotate_to(-90)  # zarotira

# strategy2.add_sequence(release_back_plant())  # ostavi i zadnje bilje

strategy2.go_to_XY(1800, -400)  # vraca se kuci

strategy2.end()
