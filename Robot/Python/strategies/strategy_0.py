from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy0 = Strategy()

strategy0.add_sequence(prepare_front_arm())
strategy0.go_to_XY(720,2300)
strategy0.rotate_to(180)
strategy0.set_distance_angle(120,0)
strategy0.add_sequence(grip_front_plant())
# strategy0.set_distance_angle(-320,0)
strategy0.rotate_to(0)
strategy0.add_sequence(prepare_back_arm())
strategy0.set_distance_angle(-250,0)
strategy0.add_sequence(grip_back_plant())
# strategy0.set_distance_angle(-40,0)
# strategy0.set_distance_angle(0,90)
# strategy0.set_distance_angle(400,0)
strategy0.go_to_XY(340,2010)
strategy0.rotate_to(90)
strategy0.set_distance_angle(20,0) #30 staro
strategy0.add_sequence(front_plant_in_pot())



# =====TRANSLACIJA=====
# strategy0.go_to_XY(3, 200)
# strategy0.go_to_XY(3, 3, False)
# strategy0.go_to_XY(3, 500)
# strategy0.go_to_XY(3, 3, False)
# strategy0.go_to_XY(3, 800)
# strategy0.go_to_XY(3, 3, False)
# strategy0.go_to_XY(3, 1200)
# strategy0.go_to_XY(3, 3, False)
# strategy0.rotate_to(0)

# =====KOCKA=====
# strategy0.go_to_XY(3, 500)
# # strategy0.rotate_to(-90)
# strategy0.go_to_XY(500, 500)
# # strategy0.rotate_to(180)
# strategy0.go_to_XY(500, 3)
# # strategy0.rotate_to(-90)
# strategy0.go_to_XY(3, 3)
# strategy0.rotate_to(0)

# =====ROTACIJA=====
# strategy0.rotate_to(0)
# strategy0.rotate_to(180)
# strategy0.rotate_to(0)
# strategy0.rotate_to(180)
# strategy0.rotate_to(0)
# strategy0.rotate_to(180)
# strategy0.rotate_to(0)
# strategy0.rotate_to(180)
# strategy0.rotate_to(0)
# strategy0.rotate_to(-90)
# strategy0.rotate_to(0)
# strategy0.rotate_to(180, s=1)
# strategy0.rotate_to(0)

# ========TEST unapred===========================

# strategy0.add_sequence(prepare_front_arm())

# strategy0.go_to_XY(3, 500)
# strategy0.add_sequence(grip_front_plant())

# strategy0.go_to_XY(3, 900)
# strategy0.add_sequence(front_plant_in_pot())

# strategy0.add_sequence(drop_front_plant())

# ========TEST unazad===========================
# strategy0.rotate_to(data.f_current)
# strategy0.add_sequence(prepare_back_arm())

# strategy0.go_to_XY(3, 500, False)
# strategy0.add_sequence(grip_back_plant())

# strategy0.go_to_XY(3, 900, False)
# strategy0.add_sequence(back_plant_in_pot())

# strategy0.add_sequence(drop_back_plant())

#==============test ruke=================

# strategy0.move_front_arm(120, s=0.1)
# strategy0.move_back_arm(190)
# strategy0.move_mechanism(180)
# strategy0.grip_front(90, 90, 180, s=1)

# strategy0.move_front_arm(80, s=0.1)
# strategy0.grip_front(175, 175, 265, s=0.1)
# strategy0.move_front_arm(120, s=3)

# strategy0.move_front_arm(100)
# strategy0.grip_front(90, 90, 180)
# strategy0.move_front_arm(120, s=3)

# strategy0.grip_front(180, 180, 270)
# strategy0.move_front_arm(65, s=3)

# strategy0.move_mechanism(280)
# strategy0.move_front_arm(80)
# strategy0.move_front_arm(100,s = 1)

# strategy0.grip_front(165, 165, 255, s=0.1)




#===========test trougao==================
# strategy0.activate_triangle(s=10)
# strategy0.deactivate_triangle()

strategy0.end()

# strategy0.go_to_XY(3, 550, s=1)
# strategy0.go_to_XY(3, 3, False, s=1)
# strategy0.go_to_XY(3, 250, s=1)
# strategy0.go_to_XY(3, 3, False, s=1)
# strategy0.go_to_XY(3, 250, s=1)
# strategy0.go_to_XY(3, 3, False, s=1)
# strategy0.go_to_XY(3, 250, s=1)
# strategy0.go_to_XY(3, 3, False, s = 1)
# strategy0.go_to_XY(3, 550, s = 1)
# strategy0.go_to_XY(3, 3, False, s = 1)
# strategy0.go_to_XY(3, 550, s = 1)
# strategy0.go_to_XY(3, 3, False, s = 1)
# strategy0.go_to_XY(3, 550, s = 1)
# strategy0.go_to_XY(3, 3, False, s = 1)
# strategy0.go_to_XY(3, 350, s = 1)
# strategy0.go_to_XY(3, 3, False, s = 1)
# strategy0.go_to_XY(3, 50, s = 1)
# strategy0.go_to_XY(3, 3, False)

# strategy0.add_sequence(unload1())  # izbaci pakove
# strategy0.add_sequence(unload2())
# strategy0.add_sequence(unload3())

# strategy0.add_sequence(sortCakes(0))
# strategy0.rotate_to(0)
# strategy0.move_pipe(170)
