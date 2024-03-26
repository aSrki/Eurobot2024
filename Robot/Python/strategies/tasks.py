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

    ini.grip_back()
    ini.grip_front()

    ini.move_front_arm(65, v=30)
    ini.move_back_arm(155, v=30)

    ini.deactivate_prednja_grtalca()
    ini.deactivate_zadnja_grtalca()

    return ini.operations


def prepare_arms6():
    # podigne i otvori prednji mehanizam kada skupljamo 6 biljki
    pa = Strategy()

    pa.move_front_arm(120, s=0.1)
    pa.move_back_arm(210)
    pa.ungrip_front(s=0.1)
    pa.ungrip_back(s=0.1)
    pa.move_mechanism(180)

    return pa.operations


def prepare_front_arm():
    # podigne i otvori prednji mehanizam
    pfa = Strategy()

    pfa.move_front_arm(120)
    pfa.ungrip_front()
    pfa.move_back_arm(200, v=15)
    pfa.move_mechanism(260)

    return pfa.operations


def prepare_back_arm():
    # podigne i otvori zadnji mehanizam
    pba = Strategy()

    pba.move_back_arm(210)
    pba.move_front_arm(110, v=15)
    pba.ungrip_back()
    pba.move_mechanism(100)

    return pba.operations


def grip_front_plant(check=False):
    gfp = Strategy()

    # gfp.set_distance_angle(95 + p, 0)

    # gfp.start_parallel()
    gfp.move_front_arm(72, v=30)  # 72
    gfp.grip_front()
    if check:
        gfp.check_object()
    # gfp.end_parallel(0.2)

    # gfp.set_distance_angle(-60, 0)  # -80 stavljeno da ne smeta drugim biljkama
    gfp.move_front_arm(110, v=15)  # 95
    return gfp.operations


def grip3_front_plant(p=0):
    gfp3 = Strategy()

    gfp3.set_distance_angle(95 + p, 0)

    # gfp.start_parallel()
    gfp3.move_front_arm(72, v=30)  # 87 #72
    gfp3.grip_front()
    # gfp.end_parallel(0.2)
    gfp3.set_distance_angle(-60, 0)
    # gfp.set_distance_angle(-60, 0)  # -80 stavljeno da ne smeta drugim biljkama
    gfp3.move_front_arm(110, v=15)  # 95
    return gfp3.operations


def grip_back_plant(check=False):
    gbp = Strategy()

    # gbp.set_distance_angle(-230 - p, 0)  # -230
    # gbp.start_parallel()
    gbp.move_back_arm(159, v=30)  # 162
    gbp.grip_back()
    if check:
        gbp.check_object()
    # gbp.set_distance_angle(20,0)
    # gbp.end_parallel(0.2)
    gbp.move_back_arm(200, v=15)  # 185

    return gbp.operations


def grip3_back_plant(p=0):
    gbp3 = Strategy()

    gbp3.set_distance_angle(-230 - p, 0)  # -230
    # gbp3.start_parallel()
    gbp3.move_back_arm(159, v=30)  # 162
    gbp3.grip_back()
    gbp3.set_distance_angle(60, 0)
    # gbp3.end_parallel(0.2)
    gbp3.move_back_arm(200, v=15)  # 185

    return gbp3.operations


def release_front_plant():  # u terenu biljke bez saksija
    rfp = Strategy()

    rfp.move_mechanism(160)  # 20 #60
    rfp.move_front_arm(85, v=30, s=0.1)  # 85
    rfp.ungrip_front()
    rfp.move_front_arm(120, s=0.5)

    return rfp.operations


def release_back_plant():  # u terenu biljke bez saksija
    rbp = Strategy()

    rbp.move_mechanism(200)
    rbp.move_back_arm(175, v=30, s=0.1)
    rbp.ungrip_back()
    rbp.move_back_arm(210, s=0.5)

    return rbp.operations


def leave_front_plant():  # van terena biljke bez saksija
    lfp = Strategy()

    lfp.move_front_arm(120)
    lfp.move_mechanism(340)
    lfp.move_front_arm(80, v=30, s=0.1)
    lfp.ungrip_front()
    lfp.move_front_arm(120, s=0.5)
    lfp.move_mechanism(180)

    return lfp.operations


def leave_back_plant():  # van terena biljke bez saksija
    lbp = Strategy()
    lbp.move_back_arm(210)
    lbp.move_mechanism(150)
    lbp.move_back_arm(190, v=30, s=0.1)
    lbp.ungrip_back()
    lbp.move_back_arm(210, s=0.5)
    lbp.move_mechanism(180)

    return lbp.operations


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
