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


strategy2.rotate_to(0)
# strategy2.set_distance_angle(95, 0) #ubaceno u task da bi bilo brze
strategy2.move_mechanism(130)
strategy2.add_sequence(grip_back_plant(-50))
strategy2.go_to_XY(700, -1320)
strategy2.rotate_to(3)
strategy2.move_mechanism(230)
strategy2.add_sequence(grip_front_plant(135))

strategy2.start_step_actions()
strategy2.move_front_arm(120, v=15)
strategy2.go_to_XY(612, -285)  # 350
strategy2.end_step_actions()

strategy2.move_mechanism(230)
strategy2.move_front_arm(80, v=30)
strategy2.set_distance_angle(-50, 0)
strategy2.set_distance_angle(0, 90, g=0.5)
strategy2.grip_front(120, 120, 120)
strategy2.move_front_arm(120, s=0.5, v=30)

strategy2.go_to_XY(1300, -762, False)

strategy2.start_step_actions()
strategy2.move_back_arm(210, v=15)
strategy2.go_to_XY(1850, -762, False) 
strategy2.end_step_actions()

strategy2.move_mechanism(90)
strategy2.move_back_arm(170, v=30)
strategy2.grip_back(120, 120, 120)
strategy2.move_back_arm(210)
strategy2.move_mechanism(180)


strategy2.end()









