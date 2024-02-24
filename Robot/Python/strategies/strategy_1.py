from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy1 = Strategy()

strategy1.rotate_to(0)
strategy1.activate_triangle()
strategy1.go_to_XY(200, 735, g=0.2)  # rotira panele
strategy1.move_front_arm(110)  # podize ruke da ne pojebe potove
strategy1.deactivate_triangle()
strategy1.add_sequence(prepare_front_arm())  # priprema za hvatanje
strategy1.go_to_XY(500, 1170)  # dolazi do tanjira 4
strategy1.rotate_to(0)
strategy1.set_distance_angle(100, 0)
strategy1.add_sequence(grip_front_plant())
strategy1.rotate_to(180)
strategy1.add_sequence(prepare_back_arm())
strategy1.set_distance_angle(-130, 0)
strategy1.add_sequence(grip_back_plant())
strategy1.go_to_XY(400, 650)
strategy1.go_to_XY(1352, 650)  # 1352 je po crtezu -35mm da uhvati prve dve
strategy1.go_to_XY(1352, 300)
strategy1.rotate_to(180)
strategy1.set_distance_angle(50, 0)
strategy1.add_sequence(front_plant_in_pot())
strategy1.go_to_XY(1387, 300, False)
strategy1.rotate_to(0)
strategy1.set_distance_angle(-50, 0)
strategy1.add_sequence(back_plant_in_pot())
strategy1.go_to_XY(1387, 160, False)
strategy1.add_sequence(drop_back_plant())
strategy1.set_distance_angle(100, 0)
strategy1.go_to_XY(1387, 160)
strategy1.add_sequence(drop_front_plant())


strategy1.end()
