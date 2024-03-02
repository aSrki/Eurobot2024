from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy1 = Strategy()

strategy1.rotate_to(0)
strategy1.activate_triangle()
strategy1.go_to_XY(195, 750, g = 0.4, s = 1.5)  # rotira panele
# strategy1.move_front_arm(110)  # podize ruke da ne pojebe potove

strategy1.start_step_actions()
strategy1.go_to_XY(500, 1210)  # dolazi do tanjira 4
strategy1.add_sequence(prepare_arms6())  # priprema za hvatanje
strategy1.end_step_actions()
strategy1.deactivate_triangle()


strategy1.rotate_to(3)
strategy1.set_distance_angle(95, 0)
strategy1.add_sequence(grip_front_plant())
strategy1.rotate_to(180)
# strategy1.add_sequence(prepare_back_arm())
strategy1.set_distance_angle(-230, -3, s = 0.1)
strategy1.add_sequence(grip_back_plant())
strategy1.go_to_XY(250, 300)
strategy1.add_sequence(release_front_plant())
strategy1.set_distance_angle(-170, 0)
strategy1.rotate_to(-30) #0
strategy1.add_sequence(release_back_plant())
#strategy1.set_distance_angle(100, 0)

strategy1.start_step_actions()
strategy1.go_to_XY(690,710)
strategy1.add_sequence(prepare_arms5())
strategy1.end_step_actions()

strategy1.rotate_to(6)
strategy1.set_distance_angle(95, 0)
strategy1.add_sequence(grip_front_plant())
strategy1.rotate_to(180)
# strategy1.add_sequence(prepare_back_arm())
strategy1.set_distance_angle(-230, -3, s = 0.1)
strategy1.add_sequence(grip_back_plant())

strategy1.go_to_XY(1342, 600)  # 1352 je po crtezu -35mm da uhvati prve dve
strategy1.go_to_XY(1342, 285) #275

# ======================== stara dobra radi lepo =================
# strategy1.add_sequence(front_plant_in_pot())
# strategy1.go_to_XY(1377, 305, False) #295
# strategy1.rotate_to(3)
# strategy1.set_distance_angle(-100, 0) #-120
# strategy1.add_sequence(back_plant_in_pot())
# strategy1.go_to_XY(1377, 152, False)
# strategy1.add_sequence(drop_back_plant())
# strategy1.set_distance_angle(100, 0)
# strategy1.go_to_XY(1400, 245)
# strategy1.rotate_to(177)
# strategy1.set_distance_angle(80, 0)
# strategy1.add_sequence(drop_front_plant())
#-==================== kraj stare dobre =========================

strategy1.add_sequence(front_plant_in_pot())
strategy1.go_to_XY(1342, 215)#205
strategy1.add_sequence(drop_front_plant())
strategy1.set_distance_angle(-100,0)
strategy1.go_to_XY(1377, 305, False) 
strategy1.rotate_to(0)
strategy1.set_distance_angle(-120, 0) #-120
strategy1.set_distance_angle(30, 0)
strategy1.add_sequence(back_plant_in_pot())
strategy1.go_to_XY(1377, 152, False)
strategy1.add_sequence(drop_back_plant())


strategy1.start_step_actions()
strategy1.go_to_XY(1300,700)
strategy1.add_sequence(prepare_arms6())
strategy1.end_step_actions()

strategy1.rotate_to(0)
strategy1.set_distance_angle(100,0)
strategy1.add_sequence(grip_front_plant())
strategy1.rotate_to(180)
# strategy1.add_sequence(prepare_back_arm())
strategy1.set_distance_angle(-230, -3, s = 0.1)
strategy1.add_sequence(grip_back_plant())
strategy1.go_to_XY(1300,762)
strategy1.go_to_XY(1850,832)#762
strategy1.add_sequence(leave_front_plant())
strategy1.go_to_XY(1700, 692, False) #762
strategy1.go_to_XY(1850, 692, False) #762
strategy1.add_sequence(leave_back_plant())
strategy1.set_distance_angle(100,0)
strategy1.go_to_XY(1775,225)



strategy1.end()