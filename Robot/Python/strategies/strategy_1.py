from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy1 = Strategy()

strategy1.rotate_to(0)
strategy1.activate_triangle()
strategy1.go_to_XY(195, 735, g = 0.4, s = 1.5)  # rotira panele
# strategy1.move_front_arm(110)  # podize ruke da ne pojebe potove
strategy1.deactivate_triangle()
strategy1.add_sequence(prepare_arms())  # priprema za hvatanje
strategy1.go_to_XY(500, 1210)  # dolazi do tanjira 4
strategy1.rotate_to(3)
strategy1.set_distance_angle(95, 0)
strategy1.add_sequence(grip_front_plant())
strategy1.rotate_to(180)
# strategy1.add_sequence(prepare_back_arm())
strategy1.set_distance_angle(-230, 0, s = 0.1)
strategy1.add_sequence(grip_back_plant())
strategy1.go_to_XY(300, 650)
strategy1.go_to_XY(1342, 600)  # 1352 je po crtezu -35mm da uhvati prve dve
strategy1.go_to_XY(1342, 280)
# strategy1.rotate_to(180)
# strategy1.set_distance_angle(20, 0)
strategy1.add_sequence(front_plant_in_pot())
strategy1.go_to_XY(1377, 300, False)
strategy1.rotate_to(0)
strategy1.set_distance_angle(-100, 0) #-120
strategy1.add_sequence(back_plant_in_pot())
strategy1.go_to_XY(1377, 157, False)
strategy1.add_sequence(drop_back_plant())
strategy1.set_distance_angle(100, 0)
strategy1.go_to_XY(1400, 250)
strategy1.rotate_to(180)
strategy1.set_distance_angle(80, 0)
strategy1.add_sequence(drop_front_plant())


strategy1.end()


# ==============================================TEST
# strategy1.rotate_to(0)
# strategy1.go_to_XY(3, 500)
# # strategy1.rotate_to(-90)
# strategy1.go_to_XY(500, 500)
# # strategy1.rotate_to(180)
# strategy1.go_to_XY(500, 3)
# # strategy1.rotate_to(-90)
# strategy1.go_to_XY(3, 3)
# strategy1.rotate_to(0)
# strategy1.end()

