from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy1 = Strategy()

strategy1.rotate_to(0)
strategy1.activate_triangle()
strategy1.go_to_XY(200, 735, g = 0.2) #rotira panele
strategy1.move_front_arm(110) #podize ruke da ne pojebe potove
strategy1.deactivate_triangle()
strategy1.add_sequence(prepare_front_arm())# priprema za hvatanje
strategy1.go_to_XY(500, 1170) #dolazi do tanjira 4
strategy1.rotate_to(0)
strategy1.set_distance_angle(100,0)
strategy1.add_sequence(grip_front_plant())
strategy1.set_distance_angle(-270, 0)
strategy1.set_distance_angle(0, 180)
strategy1.add_sequence(prepare_back_arm())
strategy1.rotate_to(180)
strategy1.set_distance_angle(-130, 0)
strategy1.set_distance_angle(0, 180)
strategy1.add_sequence(grip_back_plant())

strategy1.end()