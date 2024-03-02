from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy2 = Strategy()

strategy2.rotate_to(0) #startna pozicija (195, 2845)
strategy2.activate_triangle()
strategy2.go_to_XY(195, 2275, False, g=0.4, s=1.5) #rotira panele

strategy2.start_step_actions()
strategy2.go_to_XY(500, 1210, False)  # dolazi do tanjira 4
strategy2.add_sequence(prepare_arms6())  # priprema za hvatanje
strategy2.deactivate_triangle()
strategy2.end_step_actions()

strategy2.rotate_to(0)
strategy2.set_distance_angle(-95, 0)
strategy2.add_sequence(grip_back_plant())
strategy2.rotate_to(180)

strategy2.set_distance_angle(230, 3, s=0.1)
strategy2.add_sequence(grip_front_plant)
strategy2.go_to_XY(250, 300)
strategy2.add_sequence(release_front_plant())
strategy2.set_distance_angle(-170, 0)
strategy2.rotate_to(-30)  # 0
strategy2.add_sequence(release_back_plant())
strategy2.end()