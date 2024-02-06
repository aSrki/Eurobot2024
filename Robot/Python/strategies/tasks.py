from strategies.steps import *
from strategies.strategy import Strategy
import data


def backing_steps(distance, angle=0, sleep=0, rotate_to_angle=0):
    backing = Strategy()

    backing.front_sensors_off()
    backing.back_sensors_on()
    backing.set_distance_angle(-distance, angle, s=sleep)
    backing.rotate_to(rotate_to_angle)

    return backing.operations


def forward_steps(distance, angle=0, sleep=0, rotate_to_angle=0):
    forward = Strategy()

    forward.back_sensors_off()
    forward.front_sensors_on()
    forward.set_distance_angle(distance, angle, s=sleep)
    forward.rotate_to(rotate_to_angle)

    return forward.operations


def pink1(xoff=0, yoff=0, attempts=0, off=data.offset):

    p1 = Strategy()

    p1.grip_cakes(48)
    p1.go_to_XY(1775+xoff, 2425+yoff, ss=0.5, bs=0,
                at=0+attempts, b=200, off=off)  # 1725 bilo za X
    p1.check_cake()
    p1.lift_cakes(10)
    p1.grip_cakes(60)
    p1.lift_cakes(180)
    p1.skip_to_flag("skip_grip")

    return p1.operations


def yellow1(xoff=0, yoff=0, attempts=0, off=data.offset):
    y1 = Strategy()

    y1.go_to_XY(1775+xoff, 2225+yoff, True, ss=0.5,
                bs=2, at=1+attempts, b=200, off=off)  # bilo 2175 za Y
    y1.check_cake()
    y1.grip_cakes(48)
    y1.lift_cakes(10)
    y1.grip_cakes(60)
    y1.lift_cakes(180)
    y1.skip_to_flag("skip_grip")

    return y1.operations


def brown1(xoff=0, yoff=0, attempts=0, off=data.offset):
    b1 = Strategy()

    b1.go_to_XY(1275+xoff, 1875+yoff, ss=0.5, bs=2,
                at=1+attempts, b=100, off=off)  # bilo 1875 za Y
    b1.check_cake()
    b1.grip_cakes(48)
    b1.lift_cakes(10)
    b1.grip_cakes(60)
    b1.skip_to_flag("skip_grip")
   # b1.lift_cakes(330)

    return b1.operations


def pink2(xoff=0, yoff=0, attempts=0, off=data.offset):
    p2 = Strategy()

    p2.grip_cakes(48)
    p2.go_to_XY(225+xoff, 2425+yoff, ss=0.5, bs=0,
                at=0+attempts, b=200, off=off)
    p2.check_cake()
    p2.lift_cakes(10)
    p2.grip_cakes(60)
    p2.lift_cakes(180)
    p2.skip_to_flag("skip_grip")

    return p2.operations


def yellow2(xoff=0, yoff=0, attempts=0, off=data.offset):
    y2 = Strategy()

    y2.go_to_XY(225+xoff, 2225+yoff, ss=0.5, bs=2,
                at=1+attempts, b=200, off=off)
    y2.check_cake()
    y2.grip_cakes(48)
    y2.lift_cakes(10)
    y2.grip_cakes(60)
    y2.lift_cakes(180)
    y2.skip_to_flag("skip_grip")

    return y2.operations


def brown2(xoff=0, yoff=0, attempts=0, off=data.offset):
    b2 = Strategy()

    b2.go_to_XY(725+xoff, 1875+yoff,  ss=0.5, bs=2,
                at=1+attempts, b=100, off=off)
    b2.check_cake()
    b2.grip_cakes(48)
    b2.lift_cakes(10)
    b2.grip_cakes(60)
    b2.skip_to_flag("skip_grip")

    return b2.operations


def pink3(xoff=0, yoff=0, off=data.offset):

    p3 = Strategy()

    p3.grip_cakes(48)
    p3.go_to_XY(225+xoff, 575+yoff, off=off)
    p3.check_cake()
    p3.lift_cakes(10)
    p3.grip_cakes(60)
    p3.lift_cakes(175)
    p3.skip_to_flag("skip_grip")

    return p3.operations


def yellow3(xoff=0, yoff=0, off=data.offset):
    y3 = Strategy()

    y3.go_to_XY(225+xoff, 775+yoff, off=off)
    y3.check_cake()
    y3.grip_cakes(48)
    y3.lift_cakes(10)
    y3.grip_cakes(60)
    y3.lift_cakes(175)
    y3.skip_to_flag("skip_grip")

    return y3.operations


def brown3(xoff=0, yoff=0, off=data.offset):
    b3 = Strategy()

    b3.go_to_XY(725+xoff, 1125+yoff, off=off)
    b3.check_cake()
    b3.grip_cakes(48)
    b3.lift_cakes(10)
    b3.grip_cakes(60)
    b3.skip_to_flag("skip_grip")

    return b3.operations


def pink4(xoff=0, yoff=0, off=data.offset):

    p4 = Strategy()

    p4.grip_cakes(48)
    p4.go_to_XY(1775+xoff, 575+yoff, off=off)
    p4.check_cake()
    p4.lift_cakes(10)
    p4.grip_cakes(60)
    p4.lift_cakes(175)
    p4.skip_to_flag("skip_grip")

    return p4.operations


def yellow4(xoff=0, yoff=0, off=data.offset):
    y4 = Strategy()

    y4.go_to_XY(1775+xoff, 775+yoff, off=off)
    y4.check_cake()
    y4.grip_cakes(48)
    y4.lift_cakes(10)
    y4.grip_cakes(60)
    y4.lift_cakes(175)
    y4.skip_to_flag("skip_grip")

    return y4.operations


def brown4(xoff=0, yoff=0, off=data.offset):
    b4 = Strategy()

    b4.go_to_XY(1275+xoff, 1125+yoff, off=off)
    b4.check_cake()
    b4.grip_cakes(48)
    b4.lift_cakes(10)
    b4.grip_cakes(60)
    b4.skip_to_flag("skip_grip")

    return b4.operations


def cherry1():
    c1 = Strategy()

    c1.rotate_to(0)
    c1.move_vacuum(145)
    c1.go_to_XY(1820, 1800, True, g=0.1, s=0.5, ss=0,
                bs=2, b=0, at=0)  # da prodje dispenser
    c1.add_points("cherry", 9)
    # c1.move_vacuum(165)

    return c1.operations


def cherry2(attempts=0, offs=0):
    c2 = Strategy()

    c2.rotate_to(0)
    c2.start_parallel()
    c2.lift_cakes(10)
    c2.move_vacuum(150)
    c2.end_parallel()

    c2.set_distance_angle(450-offs, 0, g=0.1, s=1.5)

    c2.back_lidar_on()
    c2.set_distance_angle(-450, -3, g=0.8, ss=0.5, bs=0, b=0, at=0+attempts)

    c2.add_points("cherry", 9)

    return c2.operations


def cherry3(xoffs=0, yoffs=0):
    c3 = Strategy()

    c3.rotate_to(180)
    c3.move_vacuum(145)
    c3.go_to_XY(185+xoffs, 1250+yoffs, True, g=0.1, s=0.5, ss=0.5,
                bs=2, b=0, at=0)  # da prodje dispenser

    c3.add_points("cherry", 9)

    # c3.move_vacuum(165)

    return c3.operations


def cherry4():
    c4 = Strategy()

    c4.rotate_to(180)
    c4.move_vacuum(150)

    c4.set_distance_angle(450, 0, g=0.15, s=1)

    c4.back_all_on()
    c4.set_distance_angle(-450, -3, ss=0.5, bs=0, b=0, at=0)

    return c4.operations


def unload1():
    u1 = Strategy()

    u1.grip_cakes(48, s=0.3)
    u1.lift_cakes(10)

    u1.lift_cakes(155, s=0.1)
    u1.grip_cakes(60)
    u1.lift_cakes(165)

    u1.start_parallel()
    u1.move_pipe(335)
    u1.push_cake(35)
    u1.load_cherry()
    u1.end_parallel(0.5)  # OVO AKO BUDE RADILO IJU IJU

    u1.add_points("unload", 3)
    u1.set_distance_angle(-100, 0)
    u1.start_step_actions()
    u1.push_cake(265)
    u1.end_step_actions()

    u1.add_points("unload", 3)

    return u1.operations


def unload2():
    u2 = Strategy()

    u2.lift_cakes(10)
    u2.grip_cakes(48, 0.3)

    u2.lift_cakes(155)
    u2.grip_cakes(60)
    u2.lift_cakes(165)

    u2.start_parallel()
    u2.move_pipe(335)
    u2.push_cake(35)
    u2.load_cherry()
    u2.end_parallel(0.5)
    u2.add_points("unload", 3)

    u2.set_distance_angle(-100, 0)
    u2.start_step_actions()
    u2.push_cake(265)
    u2.end_step_actions()

    u2.add_points("unload", 3)

    return u2.operations


def unload3():
    u3 = Strategy()

    u3.lift_cakes(10)

    u3.grip_cakes(48)

    u3.start_parallel()
    u3.move_pipe(335)
    u3.push_cake(35)
    u3.load_cherry()
    u3.end_parallel(0.5)
    u3.add_points("unload", 3)

    u3.push_cake(265)

    # u3.set_distance_angle(-70, 0, s=0.5)
    # u3.start_step_actions()
    # u3.push_cake(120, s=0.1)
    # u3.end_step_actions()

    u3.add_points("unload", 3)

    return u3.operations


def unload_basket_blue():
    ubb = Strategy()

    ubb.rotate_to(0)
    ubb.set_distance_angle(150, 0)  # 220
    ubb.start_step_actions()
    ubb.lift_cakes(10)
    ubb.end_step_actions()
    ubb.rotate_to(0)
    # ubb.move_pipe(1)
    ubb.move_door(235)

    ubb.add_points("sort", 5)

    return ubb.operations


def unload_basket_green():
    ubg = Strategy()

    # ubg.move_pipe(1)
    ubg.rotate_to(0)
    ubg.set_distance_angle(150, 0)
    ubg.start_step_actions()
    ubg.lift_cakes(10)
    ubg.end_step_actions()  # 220
    ubg.rotate_to(0)
    ubg.move_door(235)

    ubg.add_points("sort", 5)

    return ubg.operations


def sortCakes(angle_offset=0):
    sc = Strategy()

    sc.rotate_to(60 + angle_offset)
    sc.set_distance_angle(70, 0)
    sc.start_step_actions()
    sc.grip_cakes(48, s=0.2)
    sc.lift_cakes(55)
    sc.grip_cakes(60)
    sc.lift_cakes(60)
    sc.end_step_actions()
    sc.push_cake(35)
    sc.add_points("sort", 1)
    sc.set_distance_angle(-70, 0)
    sc.start_step_actions()
    sc.push_cake(265)
    sc.end_step_actions()

    sc.rotate_to(0 + angle_offset)
    sc.set_distance_angle(150, 0)
    sc.start_step_actions()
    # sc.lift_cakes(10)
    sc.grip_cakes(48)
    sc.lift_cakes(55)  # s=0.2
    sc.end_step_actions()
    sc.add_points("sort", 1)
    sc.set_distance_angle(-150, 0)
    sc.start_step_actions()
    sc.grip_cakes(60)
    sc.lift_cakes(60)
    sc.end_step_actions()

    sc.rotate_to(300 + angle_offset)
    sc.set_distance_angle(150, 0)
    sc.start_step_actions()
    # sc.lift_cakes(1)
    sc.grip_cakes(48)
    sc.lift_cakes(105, s=0.2)
    sc.end_step_actions()
    sc.add_points("sort", 2)
    sc.set_distance_angle(-150, 0)
    sc.start_step_actions()
    sc.grip_cakes(60)
    sc.lift_cakes(110)
    sc.end_step_actions()

    sc.rotate_to(10 + angle_offset)
    sc.set_distance_angle(170, 0)
    # sc.lift_cakes(100)
    sc.grip_cakes(48)
    sc.lift_cakes(105, s=0.2)
    sc.grip_cakes(60)
    sc.add_points("sort", 1)
    sc.set_distance_angle(-170, 0)
    sc.start_step_actions()
    sc.lift_cakes(110)
    sc.end_step_actions()

    sc.rotate_to(60 + angle_offset)
    sc.set_distance_angle(150, 0)
    # sc.lift_cakes(100)
    sc.grip_cakes(48)
    sc.lift_cakes(160, s=0.2)
    sc.grip_cakes(60)
    sc.add_points("sort", 6)
    sc.set_distance_angle(-110, 0)
    sc.start_step_actions()
    sc.start_parallel()
    sc.lift_cakes(170)
    sc.move_pipe(325)
    sc.load_cherry()
    sc.end_parallel(0.6)
    sc.end_step_actions()
    sc.set_distance_angle(-40, 0)
    sc.add_points("sort", 3)

    sc.rotate_to(0 + angle_offset)
    sc.set_distance_angle(190, 0)
    sc.lift_cakes(150)
    # sc.lift_cakes(200)
    sc.grip_cakes(48)
    sc.lift_cakes(160, s=0.2)
    sc.grip_cakes(60)
    sc.add_points("sort", 5)
    sc.set_distance_angle(-110, 0)
    sc.start_step_actions()
    sc.lift_cakes(170)
    sc.load_cherry()
    sc.end_step_actions()
    sc.set_distance_angle(-80, 0)
    sc.add_points("sort", 3)

    sc.rotate_to(300 + angle_offset)
    sc.set_distance_angle(150, 0)
    sc.lift_cakes(150)
    # sc.lift_cakes(200)
    sc.grip_cakes(48)
    # sc.lift_cakes(1)
    sc.add_points("sort", 5)
    sc.set_distance_angle(-110, 0)
    sc.start_step_actions()
    sc.load_cherry()
    sc.end_step_actions()
    sc.set_distance_angle(-40, 0)
    sc.add_points("sort", 3)

    return sc.operations

# load cherry 160 unload cherry 359
# uvucena pipa 80 izvucena pipa 260
