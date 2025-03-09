from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy0 = Strategy()


strategy0.go_to_XY(0, 1000)

# strategy0.set_distance_angle(1000,0)

# strategy0.set_distance_angle(0,90)

# strategy0.set_distance_angle(0,-90)
# strategy0.set_distance_angle(1300,0)
# strategy0.set_distance_angle(-1000,0)
# strategy0.go_to_XY(1000, 1000)
# strategy0.go_to_XY(1000, 2000)
# strategy0.go_to_XY(0, 0)


# BITNO ZA PREDNJU STRANU RADIII TREBA UBRZATI 
# INIT
# strategy0.front_wall_off()
# strategy0.back_wall_off()
# strategy0.right_arm_off()
# strategy0.left_arm_off()

# strategy0.flip_left_hand(90)
# strategy0.flip_right_hand(270)
# strategy0.rotate_left_hand(90)
# strategy0.rotate_right_hand(180)
# strategy0.release()
# # ----------------- #
# print("STRATEGIJAAA")
# strategy0.front_wall_on()
# strategy0.left_arm_on()
# strategy0.right_arm_on()

# strategy0.move_front_wall(140)

# strategy0.start_parallel()
# strategy0.rotate_left_hand(145)
# strategy0.rotate_right_hand(125)
# strategy0.flip_left_hand(180)
# strategy0.flip_right_hand(180)
# strategy0.end_parallel(s = 1.5)

# strategy0.ram()
# strategy0.move_front_wall(0, s = 2)

# strategy0.start_parallel()
# strategy0.flip_left_hand(270)
# strategy0.flip_right_hand(90)
# strategy0.rotate_left_hand(90)
# strategy0.rotate_right_hand(180)
# strategy0.end_parallel(s = 0.5)

# strategy0.front_wall_off()
# strategy0.left_arm_off()
# strategy0.right_arm_off()
# strategy0.back_wall_off()
# strategy0.release()


strategy0.end()








# strategy0.object_sensor_on()

# strategy0.go_to_XY(195, 1000, at=100, b=0)
# strategy0.go_to_XY(195, 0, False, at=100, b=0)

# # strategy0.set_distance_angle(1300, 0, at=100, b=0)
# # strategy0.set_distance_angle(-1300, 0, at=100, b=0)

# strategy0.activate_prednja_desna_grtalca()
# strategy0.deactivate_prednja_desna_grtalca()
# strategy0.activate_prednja_leva_grtalca()
# strategy0.deactivate_prednja_leva_grtalca()

# strategy0.activate_zadnja_desna_grtalca()
# strategy0.deactivate_zadnja_desna_grtalca()
# strategy0.activate_zadnja_leva_grtalca()
# strategy0.deactivate_zadnja_leva_grtalca()

# strategy0.activate_prednja_grtalca()
# strategy0.deactivate_prednja_grtalca()
# strategy0.activate_zadnja_grtalca()
# strategy0.deactivate_zadnja_grtalca()

# =========================test strategija========================

# strategy0.add_sequence(prepare_front_arm())
# strategy0.go_to_XY(700, 2300)
# strategy0.rotate_to(180)
# strategy0.set_distance_angle(130, 0)
# strategy0.add_sequence(grip_front_plant())
# # strategy0.set_distance_angle(-320,0)
# strategy0.rotate_to(0)
# strategy0.add_sequence(prepare_back_arm())
# strategy0.set_distance_angle(-270, 0)
# strategy0.add_sequence(grip_back_plant())
# # strategy0.set_distance_angle(-40,0)
# # strategy0.set_distance_angle(0,90)
# # strategy0.set_distance_angle(400,0)
# strategy0.go_to_XY(340, 2045)
# strategy0.rotate_to(90)
# strategy0.set_distance_angle(90, 0)
# strategy0.add_sequence(front_plant_in_pot())
# strategy0.go_to_XY(270, 2010, False)
# strategy0.rotate_to(-90)
# strategy0.set_distance_angle(-20, 0)
# strategy0.add_sequence(back_plant_in_pot())


# =====TRANSLACIJA=====
# strategy0.rotate_to(0)
# strategy0.go_to_XY(3, 1003)
# strategy0.go_to_XY(3, 3, False)
# # strategy0.rotate_to(180)
# # strategy0.go_to_XY(3, 1103)
# # strategy0.go_to_XY(3, 3, False)
# # strategy0.go_to_XY(3, 1103)
# # strategy0.go_to_XY(3, 3, False)
# # strategy0.go_to_XY(3, 1103)
# # strategy0.go_to_XY(3, 3, False)
# strategy0.rotate_to(0)

# strategy0.end()

# # =====KOCKA=====
# strategy0.rotate_to(0)

# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.go_to_XY(0, 2000)
# strategy0.go_to_XY(0, 0, False)
# strategy0.rotate_to(180)
# strategy0.go_to_XY(0, 1500)
# strategy0.go_to_XY(-1000, 1000)
# strategy0.go_to_XY(-1000, 0)
# strategy0.go_to_XY(0, 0)
# strategy0.end()


# =====ROTACIJA=====
# strategy0.rotate_to(0)
# strategy0.rotate_to(180, s=1)
# strategy0.rotate_to(0, s = 1)
# strategy0.rotate_to(180, s = 1)
# strategy0.rotate_to(0, s = 1)
# strategy0.rotate_to(180, s = 1)
# strategy0.rotate_to(0, s = 1)
# strategy0.rotate_to(180, s = 1)
# strategy0.rotate_to(0, s = 1)
# ==========================DIStance angle translacija=======================
# strategy0.rotate_to(0)
# strategy0.set_distance_angle(2500, 0)
# strategy0.rotate_to(0)
# strategy0.set_distance_angle(-2500, 0)
# strategy0.rotate_to(0)
# strategy0.set_distance_angle(1200, 0)
# strategy0.rotate_to(0)
# strategy0.set_distance_angle(-1200, 0)
# strategy0.rotate_to(0)
# ========DISTANCE ANGLE ROTACIJA===================

# strategy0.set_distance_angle(-2000, 0)
# strategy0.set_distance_angle(2000, 0)
# strategy0.set_distance_angle(-2000, 0)

# strategy0.set_distance_angle(0, 180)
# strategy0.set_distance_angle(0, 180)
# strategy0.set_distance_angle(0, 180)
# strategy0.set_distance_angle(0, 180)
# strategy0.set_distance_angle(0, 180)
# strategy0.set_distance_angle(0, 90)
# strategy0.set_distance_angle(0, 90)
# strategy0.set_distance_angle(0, 90)


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


# ==============test ruke prednja=================
# strategy0.add_sequence(init_servos())

# strategy0.add_sequence(prepare_front_arm())
# strategy0.add_sequence(grip_front_plant())
# strategy0.add_sequence(front_plant_in_pot())

strategy0.end()

# =================test ruke zadnja===================
# strategy0.add_sequence(init_servos())

# strategy0.add_sequence(prepare_back_arm())
# strategy0.add_sequence(grip_back_plant())
# strategy0.add_sequence(back_plant_in_pot())


# ===========test trougao==================
# strategy0.activate_triangle(s=10)
# strategy0.deactivate_triangle()


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
