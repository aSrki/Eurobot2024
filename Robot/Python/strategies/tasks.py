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


def test_task():
    tt = Strategy()

    tt.activate_triangle()
    tt.deactivate_triangle()

    tt.move_front_arm(60)
    tt.move_back_arm(150)

    tt.move_mechanism(180)

    tt.grip_back(180, 180, 270)
    tt.grip_front(180, 180, 90)

    return tt.operations

def prepare_front_arm():
    # podigne i otvori prednji mehanizam
    pfa = Strategy()

    pfa.move_front_arm(120, s=0.1)
    pfa.move_back_arm(190)
    pfa.grip_front(90, 90, 180, s=0.1)
    pfa.move_mechanism(120)

    return pfa.operations

def prepare_back_arm():
    # podigne i otvori zadnji mehanizam
    pba = Strategy()

    pba.move_back_arm(210, s=0.1)
    pba.move_front_arm(110)
    pba.grip_back(90, 90, 0, s=0.1)
    pba.move_mechanism(100)

    return pba.operations

def grip_front_plant():
    gfp = Strategy()

    gfp.move_mechanism(100)
    gfp.move_front_arm(80, s=0.1)
    gfp.grip_front(175, 175, 265, s=0.1)
    gfp.move_mechanism(80)
    gfp.set_distance_angle(-80,0)
    gfp.move_front_arm(120)

    return gfp.operations

def grip_back_plant():
    gbp = Strategy()

    gbp.move_back_arm(160, s=0.1)
    gbp.grip_back(175, 175, 85, s=0.1)
    gbp.move_back_arm(210)

    return gbp.operations

def front_plant_in_pot():
    fpip = Strategy()

    fpip.move_mechanism(55, s=0.2)
    fpip.move_front_arm(110)
    fpip.grip_front(180, 90, 180)
    fpip.move_front_arm(120)
    fpip.move_mechanism(200) #180
    fpip.set_distance_angle(-100, 0)
    fpip.grip_front(180, 180, 270)
    fpip.move_front_arm(65) #60 staro
    fpip.set_distance_angle(70, 0)
    fpip.move_mechanism(260, s=0.5, v=50)
    # fpip.move_front_arm(60,s=0.5)
    fpip.move_mechanism(180)
    fpip.set_distance_angle(-100,0)
    fpip.move_front_arm(120, s=0.5, v=15)

    return fpip.operations

def back_plant_in_pot():
    bpip = Strategy()

    bpip.move_mechanism(270, s=0.2)
    bpip.move_back_arm(165)
    bpip.grip_back(90, 90, 1)
    bpip.move_back_arm(210)
    bpip.move_mechanism(180)
    bpip.set_distance_angle(100, 0)
    bpip.grip_back(180, 180, 90)
    bpip.move_back_arm(155)
    bpip.set_distance_angle(-100, 0)
    bpip.move_mechanism(40)
    bpip.move_back_arm(170, s=0.5)
    bpip.move_mechanism(180)
    bpip.move_back_arm(210, s=0.5)

    return bpip.operations

def drop_front_plant():
    dfp = Strategy()

    dfp.move_mechanism(310)
    dfp.move_front_arm(75)
    dfp.grip_front(165, 165, 255, s=0.1)
    dfp.move_front_arm(120)
    dfp.move_mechanism(180)

    return dfp.operations

def drop_back_plant():
    dbp = Strategy()

    dbp.move_mechanism(10)
    dbp.move_back_arm(165)
    dbp.grip_back(165, 165, 75, s=0.1)
    dbp.move_back_arm(210)
    dbp.move_mechanism(180)

    return dbp.operations


# def pink1(xoff=0, yoff=0, attempts=0, off=data.offset):

#     p1 = Strategy()

#     p1.grip_cakes(48)
#     p1.go_to_XY(1775+xoff, 2425+yoff, ss=0.5, bs=0,
#                 at=0+attempts, b=200, off=off)  # 1725 bilo za X
#     p1.check_cake()
#     p1.lift_cakes(10)
#     p1.grip_cakes(60)
#     p1.lift_cakes(180)
#     p1.skip_to_flag("skip_grip")

#     return p1.operations



