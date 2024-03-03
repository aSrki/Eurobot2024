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

    ini.grip_back(215, 180, 215)
    ini.grip_front(180, 180, 270)

    ini.move_front_arm(65)
    ini.move_back_arm(155)

    return ini.operations


def prepare_arms5():
    # podigne i otvori prednji mehanizam kada skupljamo 5 biljki
    pa = Strategy()

    pa.move_front_arm(120, s=0.1)
    pa.move_back_arm(210)
    pa.grip_front(180, 90, 180, s=0.1)  # ignorisemo onu sto nas smara
    pa.grip_back(215, 90, 120, s=0.1)
    pa.move_mechanism(180)

    return pa.operations


def prepare_arms6():
    # podigne i otvori prednji mehanizam kada skupljamo 6 biljki
    pa = Strategy()

    pa.move_front_arm(120, s=0.1)
    pa.move_back_arm(210)
    pa.grip_front(90, 90, 180, s=0.1)
    pa.grip_back(120, 90, 120, s=0.1)
    pa.move_mechanism(180)

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
#     pba.grip_back(120, 90, 120, s=0.1)
#     pba.move_mechanism(180)

#     return pba.operations


def grip_front_plant():
    gfp = Strategy()

    gfp.set_distance_angle(95, 0)

    gfp.start_parallel()
    gfp.move_front_arm(77, v=30)  # 87
    gfp.grip_front(173, 173, 263)
    gfp.end_parallel(0.2)

    gfp.set_distance_angle(-60, 0)  # -80 stavljeno da ne smeta drugim biljkama
    gfp.move_front_arm(120, v=30)

    return gfp.operations


def grip_back_plant():
    gbp = Strategy()

    gbp.set_distance_angle(-230, 0)
    gbp.start_parallel()
    gbp.move_back_arm(170, v=30)
    gbp.grip_back(208, 173, 208)
    gbp.end_parallel(0.2)
    gbp.move_back_arm(210)

    return gbp.operations


def front_plant_in_pot():
    fpip = Strategy()

    fpip.move_front_arm(120)
    fpip.move_mechanism(30)  # 20 #60
    fpip.move_front_arm(90, v=30, s=0.1)  # 85
    fpip.grip_front(180, 120, 180)
    fpip.move_front_arm(120, s=0.5)
    fpip.move_mechanism(180)
    fpip.set_distance_angle(-120, 0)
    fpip.grip_front(185, 185, 275)
    fpip.move_front_arm(68)
    # fpip.set_distance_angle(60, 0)
    fpip.set_distance_angle(48, 0)
    fpip.move_mechanism(315, s=0.5)  # 345
    fpip.move_front_arm(73, s=0.5, v=30)
    # fpip.grip_front(90, 180, 270)
    fpip.set_distance_angle(-50, 0, s=0.1)
    fpip.move_front_arm(120, v=20)
    fpip.move_mechanism(180)
    # fpip.move_front_arm(120, s=0.5, v=20)

    return fpip.operations


def back_plant_in_pot():
    bpip = Strategy()

    bpip.move_back_arm(210, s=0.5)
    bpip.move_mechanism(300)
    # dodati v = 50 ako cimaju biljke kada padaju
    bpip.move_back_arm(180, v=30)
    bpip.grip_back(120, 90, 120)
    # bpip.move_mechanism(270, s=0.5)
    bpip.move_back_arm(210, s=0.5, v=20)
    bpip.move_mechanism(180)
    bpip.set_distance_angle(130, 0)
    bpip.grip_back(215, 180, 215)
    # bpip.move_back_arm(155, v=20)
    bpip.move_back_arm(162)
    bpip.set_distance_angle(-105, 0)  # -60
   # bpip.move_mechanism(120)
    bpip.set_distance_angle(100, 0)
   # bpip.move_back_arm(180, s=0.5, v=30)
   # bpip.move_mechanism(180)
    bpip.move_back_arm(210, v=20)  # v=30

    return bpip.operations


def memristor_front():  # za saksije van stola i biljke u limu
    mmsf = Strategy()

    mmsf.start_parallel()  # treba snimati i vaditi stvari iz paralela ako ne rade
    mmsf.move_front_arm(120, v=30)
    mmsf.move_back_arm(210, v=30)
    mmsf.move_mechanism(270)
    mmsf.end_parallel(0.1)

    mmsf.move_front_arm(93, v=30)
    mmsf.grip_front(90, 120, 180, s=0.1)

    mmsf.start_parallel()
    mmsf.move_front_arm(120, v=30)
    mmsf.grip_front(180, 180, 270, s=0.1)
    mmsf.move_mechanism(180)
    mmsf.end_parallel(0.1)

    mmsf.set_distance_angle(-100, 0)

    mmsf.set_distance_angle(30, 0)


    mmsf.move_front_arm(75, v=30)
    mmsf.move_mechanism(180)

    return mmsf.operations


def memristor_back():  # nastavak ovog gore
    mmsb = Strategy()

    mmsb.start_parallel()
    mmsb.move_back_arm(210, v=30)
    mmsb.move_front_arm(120, v=30)
    mmsb.move_mechanism(15)
    mmsb.end_parallel(0.1)

    mmsb.start_parallel()
    mmsb.move_back_arm(175, v=15)
    mmsb.grip_back(150, 120, 150)
    mmsb.end_parallel(0.1)

    mmsb.start_parallel()
    mmsb.move_back_arm(200, v=30)
    mmsb.grip_back(215, 180, 215, s=0.1)
    mmsb.move_mechanism(180)
    mmsb.move_mechanism(280)
    mmsb.end_parallel(0.1)
    mmsb.start_parallel()
    mmsb.set_distance_angle(100, 0)
    mmsb.move_back_arm(165, v=30)
    mmsb.move_front_arm(100, v=30)
    mmsb.end_parallel(0.1)

    mmsb.set_distance_angle(-120, 0)
    mmsb.set_distance_angle(50, 0)

    
    mmsb.move_back_arm(210, v=15)
    mmsb.move_mechanism(7)
    
    mmsb.set_distance_angle(-120, 0)

    mmsb.move_back_arm(175, v=15)  # 180
    mmsb.grip_back(190, 155, 190, s=0.1)

    mmsb.start_parallel()
    mmsb.move_back_arm(210, v=30)
    mmsb.move_mechanism(180)
    mmsb.end_parallel(0.1)

    return mmsb.operations


def drop_front_plant():  # ne koriste se sada
    dfp = Strategy()

    dfp.move_mechanism(350)  # 170
    dfp.move_front_arm(95)  # 88
    dfp.grip_front(110, 165, 255, s=0.1)
    dfp.move_front_arm(120)
    dfp.move_mechanism(180)

    return dfp.operations


def drop_back_plant():  # ne koriste se sada
    dbp = Strategy()

    dbp.move_mechanism(180)  # 25
    dbp.move_back_arm(190)  # 168
    # dbp.move_mechanism(8)
    dbp.grip_back(200, 165, 200, s=0.1)
    # dbp.move_mechanism(75) #75
    dbp.move_back_arm(210, v=40)
    # dbp.move_mechanism(180)

    return dbp.operations


def release_front_plant():  # u terenu biljke bez saksija
    rfp = Strategy()

    rfp.move_front_arm(120)
    rfp.move_mechanism(180)  # 20 #60
    rfp.move_front_arm(80, v=30, s=0.1)  # 85
    rfp.grip_front(90, 90, 180)
    rfp.move_front_arm(120, s=0.5)
    rfp.move_mechanism(180)

    return rfp.operations


def release_back_plant():  # u terenu biljke bez saksija
    rbp = Strategy()

    rbp.move_back_arm(210)
    rbp.move_mechanism(180)  # 20 #60
    rbp.move_back_arm(170, v=30, s=0.1)  # 85
    rbp.grip_back(120, 90, 120)
    rbp.move_back_arm(210, s=0.5)
    rbp.move_mechanism(180)

    return rbp.operations


def leave_front_plant():  # van terena biljke bez saksija
    lfp = Strategy()

    lfp.move_front_arm(120)
    lfp.move_mechanism(340)
    lfp.move_front_arm(80, v=30, s=0.1)
    lfp.grip_front(90, 90, 180)
    lfp.move_front_arm(120, s=0.5)
    lfp.move_mechanism(180)

    return lfp.operations


def leave_back_plant():  # van terena biljke bez saksija
    lbp = Strategy()
    lbp.move_back_arm(210)
    lbp.move_mechanism(150)
    lbp.move_back_arm(190, v=30, s=0.1)
    lbp.grip_back(120, 90, 120)
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
