from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy0 = Strategy()

# strategy0.lift_cakes(10)
# strategy0.front_all_on()
# strategy0.add_sequence(pink2())  # -50, 25
# strategy0.go_to_XY(250, 2600, True, ss=1, bs=2, at=100, b=200)
# strategy0.lift_cakes(10, s=0.5)
# strategy0.grip_cakes(48)
# strategy0.push_cake(35)
# strategy0.push_cake(265)
# strategy0.front_all_off()

# strategy0.grip_cakes(48)
# strategy0.move_pipe(170)
# # strategy0.set_skip_flag(70)
# strategy0.back_all_on()  # izlazenje iz tanjira
# strategy0.go_to_XY(1000, 1600, False, ss=0, bs=0, at=0, b=0)
# # strategy0.skip_to_flag(70)
# strategy0.go_to_XY(300, 1400, False, ss=0, bs=0.1, at=100, b=0)
# # strategy0.back_all_off()

# strategy0.end()


strategy0.go_to_XY(3, 550)
strategy0.go_to_XY(3, 3, False)
strategy0.go_to_XY(3, 550)
strategy0.go_to_XY(3, 3, False)
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
strategy0.end()
