from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy


strategy0 = Strategy()

#=====TRANSLACIJA=====
strategy0.go_to_XY(3, 500)
strategy0.go_to_XY(3, 3, False)
strategy0.go_to_XY(3, 500)
strategy0.go_to_XY(3, 3, False)
strategy0.go_to_XY(3, 500)
strategy0.go_to_XY(3, 3, False)
strategy0.go_to_XY(3, 500)
strategy0.go_to_XY(3, 3, False)
strategy0.rotate_to(0)

#=====KOCKA=====
# strategy0.go_to_XY(3, 700)
# strategy0.rotate_to(90)
# strategy0.go_to_XY(-700, 700)
# strategy0.rotate_to(180)
# strategy0.go_to_XY(-700, 3)
# strategy0.rotate_to(-90)
# strategy0.go_to_XY(3, 3)
# strategy0.rotate_to(0)

# =====ROTACIJA=====
# strategy0.rotate_to(90)
# strategy0.rotate_to(0)
# strategy0.rotate_to(-90)
# strategy0.rotate_to(0)
# strategy0.rotate_to(180)
# strategy0.rotate_to(0)

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
