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


def init_servos():
    ini = Strategy()

    ini.move_front_arm(110)
    ini.move_back_arm(200)

    ini.move_mechanism(180)

    ini.grip_back(180, 180, 90)
    ini.grip_front(180, 180, 270)

    ini.move_front_arm(65)
    ini.move_back_arm(155)

    return ini.operations


def prepare_arms():
    # podigne i otvori prednji mehanizam
    pa = Strategy()

    pa.start_parallel()
    pa.move_front_arm(120, s=0.1)
    pa.move_back_arm(210)
    pa.grip_front(90, 90, 180, s=0.1) #ignorisemo onu sto nas smara
    pa.grip_back(90, 90, 0, s=0.1)
    pa.move_mechanism(180)
    pa.end_parallel()

    return pa.operations

# def prepare_front_arm():
#     # podigne i otvori prednji mehanizam
#     pfa = Strategy()

#     pfa.move_front_arm(120, s=0.1)
#     pfa.move_back_arm(210)
#     pfa.grip_front(180, 90, 180, s=0.1) #ignorisemo onu sto nas smara
#     pfa.move_mechanism(180)

#     return pfa.operations


# def prepare_back_arm():
#     # podigne i otvori zadnji mehanizam
#     pba = Strategy()

#     pba.move_back_arm(210, s=0.1)
#     pba.move_front_arm(120)
#     pba.grip_back(90, 90, 0, s=0.1)
#     pba.move_mechanism(180)

#     return pba.operations


def grip_front_plant():
    gfp = Strategy()

    gfp.move_front_arm(78, s=0.1, v=30) #87
    gfp.grip_front(177, 177, 267, s=0.1)
    gfp.set_distance_angle(-80, 0)  # stavljeno da ne smeta drugim biljkama
    gfp.move_front_arm(120)

    return gfp.operations


def grip_back_plant():
    gbp = Strategy()

    gbp.move_back_arm(168, s=0.1, v=30) #177
    gbp.grip_back(177, 177, 87, s=0.1)
    gbp.move_back_arm(210)

    return gbp.operations


def front_plant_in_pot():
    fpip = Strategy()

    fpip.move_front_arm(120)
    fpip.move_mechanism(30) #20 #60
    fpip.move_front_arm(90, v=30, s=0.1) #85
    fpip.grip_front(180, 100, 180)
    fpip.move_front_arm(120, s=0.5)
    fpip.move_mechanism(180)
    fpip.set_distance_angle(-120, 0)
    fpip.grip_front(180, 180, 270)
    fpip.move_front_arm(68)
    #fpip.set_distance_angle(60, 0)
    fpip.set_distance_angle(45, 0) #50 #45
    fpip.move_mechanism(315, s=0.5) #345 
    fpip.move_front_arm(73, s=0.5, v=30)
    # fpip.grip_front(90, 180, 270)
    fpip.set_distance_angle(-100, 0, s=0.1)
    fpip.move_front_arm(120, v=20)
    fpip.move_mechanism(180)
    #fpip.move_front_arm(120, s=0.5, v=20)

    return fpip.operations


def back_plant_in_pot():
    bpip = Strategy()

    bpip.move_back_arm(210, s=0.5)
    bpip.move_mechanism(300)
    # dodati v = 50 ako cimaju biljke kada padaju
    bpip.move_back_arm(180, v=30)
    bpip.grip_back(90, 90, 1)
    # bpip.move_mechanism(270, s=0.5)
    bpip.move_back_arm(210, s=0.5, v=20)
    bpip.move_mechanism(180)
    bpip.set_distance_angle(130, 0)
    bpip.grip_back(180, 180, 90)
    bpip.move_back_arm(155, v=20)
    bpip.set_distance_angle(-100, 0)  # -60
   # bpip.move_mechanism(120)
    bpip.move_back_arm(165)
    bpip.set_distance_angle(100, 0)
   # bpip.move_back_arm(180, s=0.5, v=30)
   # bpip.move_mechanism(180)
    bpip.move_back_arm(210, v=20)  # v=30

    return bpip.operations


def drop_front_plant():
    dfp = Strategy()

    dfp.move_mechanism(160)
    dfp.move_front_arm(88)
    dfp.grip_front(110, 165, 255, s=0.1)
    dfp.move_front_arm(120)
    dfp.move_mechanism(180)

    return dfp.operations


def drop_back_plant():
    dbp = Strategy()

    dbp.move_mechanism(10)
    dbp.move_back_arm(168)
    dbp.grip_back(165, 165, 75, s=0.1)
    dbp.move_mechanism(75)
    dbp.move_back_arm(210, v=40)
    #dbp.move_mechanism(180)

    return dbp.operations


# def pink1(xoff=0, yoff=0, ainiempts=0, off=data.offset):

#     p1 = Strategy()

#     p1.grip_cakes(48)
#     p1.go_to_XY(1775+xoff, 2425+yoff, ss=0.5, bs=0,
#                 at=0+ainiempts, b=200, off=off)  # 1725 bilo za X
#     p1.check_cake()
#     p1.lift_cakes(10)
#     p1.grip_cakes(60)
#     p1.lift_cakes(180)
#     p1.skip_to_flag("skip_grip")

#     return p1.operations
