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


def grip3_front_plant(p=0, check=False):
    gfp3 = Strategy()

    gfp3.set_distance_angle(95 + p, 0)

    # gfp.start_parallel()
    gfp3.move_front_arm(75, v=30)  # 87 #72
    gfp3.grip_front()
    if check:
        gfp3.check_object()
    # gfp.end_parallel(0.2)
    gfp3.set_distance_angle(-60, 0)
    # gfp.set_distance_angle(-60, 0)  # -80 stavljeno da ne smeta drugim biljkama
    gfp3.move_front_arm(110, v=15)  # 95
    return gfp3.operations


def grip3_back_plant(p=0, check=False):
    gbp3 = Strategy()

    gbp3.set_distance_angle(-230 - p, 0)  # -230
    # gbp3.start_parallel()
    gbp3.move_back_arm(162, v=30)  # 162
    gbp3.grip_back()
    if check:
        gbp3.check_object()
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


def univerzalni_kraj_zuta():
    ukz = Strategy()

    # ==========================univerzalni kraj zuta=======================
    ukz.front_all_off()
    ukz.back_all_on()

    ukz.set_skip_flag("brzi_istovar")
    ukz.check_time(72, "brzi_istovar")

    ukz.start_step_actions()
    ukz.go_to_XY(1542, 270, False, at=100, b=200)  # 350
    ukz.move_back_arm(210, v=15)  # podize rukzu
    ukz.deactivate_prednja_grtalca()
    ukz.deactivate_zadnja_grtalca()
    ukz.end_step_actions()
    ukz.skip_to_flag("reset")
    ukz.back_all_off()

    ukz.rotate_to(0)
    # ukz.set_distance_angle(-10, 0)
    ukz.move_mechanism(160)  # 220
    ukz.move_back_arm(190, v=30)  # 100
    ukz.ungrip_back()
    ukz.move_back_arm(210, v=30)

    ukz.front_all_on()

    ukz.start_step_actions()
    ukz.set_distance_angle(200, 0, at=100, b=0)
    ukz.grip_back()
    ukz.deactivate_prednja_grtalca()
    ukz.deactivate_zadnja_grtalca()
    ukz.end_step_actions()

    ukz.move_front_arm(120, v=30)
    ukz.go_to_XY(1312, 270, at=100, b=0)  # 285
    ukz.rotate_to(180)
    ukz.move_mechanism(200)  # izbaci rukzu
    ukz.move_front_arm(100, v=30)
    ukz.ungrip_front()
    ukz.move_front_arm(120, v=30)

    ukz.start_step_actions()
    ukz.set_distance_angle(60, 0)
    ukz.activate_prednja_desna_grtalca()
    ukz.end_step_actions()

    ukz.add_points("unload", 20)

    ukz.set_distance_angle(0, 95, g=0.3)  # zatorira ka tanjiru

    ukz.start_step_actions()
    ukz.set_distance_angle(350, 0, g=0.5)  # udje u tanjur
    # ukz.deactivate_prednja_grtalca()
    ukz.end_step_actions()

    ukz.all_off()

    ukz.end()

    return ukz.operations


def univerzalni_kraj_plava():
    ukp = Strategy()

    # ==========================univerzalni kraj plava=======================
    ukp.back_all_off()
    ukp.front_all_on()

    ukp.set_skip_flag("brzi_istovar")
    ukp.check_time(72, "brzi_istovar")

    ukp.start_step_actions()
    ukp.go_to_XY(1542, -270, at=100, b=200)  # 350
    ukp.move_front_arm(120, v=15)  # podize rukpu
    ukp.deactivate_zadnja_grtalca()
    ukp.deactivate_prednja_grtalca()
    ukp.end_step_actions()
    ukp.skip_to_flag("reset")
    ukp.back_all_off()

    ukp.rotate_to(0)
    # ukp.set_distance_angle(-10, 0)
    ukp.move_mechanism(240)  # 220
    ukp.move_front_arm(100, v=30)  # 100
    ukp.ungrip_front()
    ukp.move_front_arm(120, v=30)

    ukp.back_all_on()

    ukp.start_step_actions()
    ukp.set_distance_angle(-200, 0, at=100, b=0)
    ukp.grip_front()
    ukp.deactivate_zadnja_grtalca()
    ukp.deactivate_prednja_grtalca()
    ukp.end_step_actions()

    ukp.move_back_arm(210, v=30)
    ukp.go_to_XY(1312, -270, False, at=100, b=0)  # 285
    ukp.rotate_to(180)
    ukp.move_mechanism(120)  # izbaci rukpu
    ukp.move_back_arm(190, v=30)
    ukp.ungrip_back()
    ukp.move_back_arm(210, v=30)

    ukp.start_step_actions()
    ukp.set_distance_angle(-60, 0)
    ukp.activate_zadnja_desna_grtalca()
    ukp.end_step_actions()

    ukp.add_points("unload", 20)  # dodaje poene za pet u metale

    ukp.set_distance_angle(0, -95, g=0.3)  # zatorira ka tanjiru

    ukp.set_distance_angle(-350, 0, g=0.5)  # udje u tanjur
    # ukp.deactivate_prednja_grtalca()

    ukp.all_off()

    ukp.end()

    return ukp.operations


def blue_get_1_front(check=False, off=120):
    bg1f = Strategy()

    bg1f.back_all_off()
    bg1f.front_all_on()

    bg1f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg1f.go_to_XY(1500, -1500, off=off, at=0, b=100)
    bg1f.add_sequence(prepare_front_arm())
    bg1f.deactivate_zadnja_grtalca()
    bg1f.activate_prednja_grtalca()
    bg1f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg1f.add_sequence(grip_front_plant(check))

    return bg1f.operations


def blue_get_1_back(check=False, off=120):
    bg1b = Strategy()

    bg1b.front_all_off()
    bg1b.back_all_on()

    bg1b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg1b.go_to_XY(1500, -1500, False, off=off, at=0, b=100)
    bg1b.add_sequence(prepare_back_arm())
    bg1b.deactivate_prednja_grtalca()
    bg1b.activate_zadnja_grtalca()
    bg1b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg1b.add_sequence(grip_back_plant(check))

    return bg1b.operations


def blue_get_2_front(check=False, off=120):
    bg2f = Strategy()

    bg2f.back_all_off()
    bg2f.front_all_on()

    bg2f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg2f.go_to_XY(1300, -1000, off=off, at=0, b=100)
    bg2f.add_sequence(prepare_front_arm())
    bg2f.deactivate_zadnja_grtalca()
    bg2f.activate_prednja_grtalca()
    bg2f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg2f.add_sequence(grip_front_plant(check))

    return bg2f.operations


def blue_get_2_back(check=False, off=120):
    bg2b = Strategy()

    bg2b.front_all_off()
    bg2b.back_all_on()

    bg2b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg2b.go_to_XY(1300, -1000, False, off=off, at=0, b=100)
    bg2b.add_sequence(prepare_back_arm())
    bg2b.deactivate_prednja_grtalca()
    bg2b.activate_zadnja_grtalca()
    bg2b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg2b.add_sequence(grip_back_plant(check))

    return bg2b.operations


def blue_get_3_front(check=False, off=120):
    bg3f = Strategy()

    bg3f.back_all_off()
    bg3f.front_all_on()

    bg3f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg3f.go_to_XY(700, -1000, off=off, at=0, b=100)
    bg3f.add_sequence(prepare_front_arm())
    bg3f.deactivate_zadnja_grtalca()
    bg3f.activate_prednja_grtalca()
    bg3f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg3f.add_sequence(grip_front_plant(check))

    return bg3f.operations


def blue_get_3_back(check=False, off=120):
    bg3b = Strategy()

    bg3b.front_all_off()
    bg3b.back_all_on()

    bg3b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg3b.go_to_XY(700, -1000, False, off=off, at=0, b=100)
    bg3b.add_sequence(prepare_back_arm())
    bg3b.deactivate_prednja_grtalca()
    bg3b.activate_zadnja_grtalca()
    bg3b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg3b.add_sequence(grip_back_plant(check))

    return bg3b.operations


def blue_get_4_front(check=False, off=120):
    bg4f = Strategy()

    bg4f.back_all_off()
    bg4f.front_all_on()

    bg4f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg4f.go_to_XY(500, -1500, off=off, at=0, b=100)
    bg4f.add_sequence(prepare_front_arm())
    bg4f.deactivate_zadnja_grtalca()
    bg4f.activate_prednja_grtalca()
    bg4f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg4f.add_sequence(grip_front_plant(check))

    return bg4f.operations


def blue_get_4_back(check=False, off=120):
    bg4b = Strategy()

    bg4b.front_all_off()
    bg4b.back_all_on()

    bg4b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg4b.go_to_XY(500, -1500, False, off=off, at=0, b=100)
    bg4b.add_sequence(prepare_back_arm())
    bg4b.deactivate_prednja_grtalca()
    bg4b.activate_zadnja_grtalca()
    bg4b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg4b.add_sequence(grip_back_plant(check))

    return bg4b.operations


def blue_get_5_front(check=False, off=120):
    bg5f = Strategy()

    bg5f.back_all_off()
    bg5f.front_all_on()

    bg5f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg5f.go_to_XY(700, -2000, off=off, at=0, b=100)
    bg5f.add_sequence(prepare_front_arm())
    bg5f.activate_prednja_grtalca()
    bg5f.deactivate_zadnja_grtalca()
    bg5f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg5f.add_sequence(grip_front_plant(check))

    return bg5f.operations


def blue_get_5_back(check=False, off=120):
    bg5b = Strategy()

    bg5b.front_all_off()
    bg5b.back_all_on()

    bg5b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg5b.go_to_XY(700, -2000, False, off=off, at=0, b=100)
    bg5b.add_sequence(prepare_back_arm())
    bg5b.deactivate_prednja_grtalca()
    bg5b.activate_zadnja_grtalca()
    bg5b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg5b.add_sequence(grip_back_plant(check))

    return bg5b.operations


def blue_get_6_front(check=False, off=120):
    bg6f = Strategy()

    bg6f.back_all_off()
    bg6f.front_all_on()

    bg6f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg6f.go_to_XY(1300, -2000, off=off, at=0, b=100)
    bg6f.add_sequence(prepare_front_arm())
    bg6f.deactivate_zadnja_grtalca()
    bg6f.activate_prednja_grtalca()
    bg6f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg6f.add_sequence(grip_front_plant(check))

    return bg6f.operations


def blue_get_6_back(check=False, off=120):
    bg6b = Strategy()

    bg6b.front_all_off()
    bg6b.back_all_on()

    bg6b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    bg6b.go_to_XY(1300, -2000, False, off=off, at=0, b=100)
    bg6b.add_sequence(prepare_back_arm())
    bg6b.deactivate_prednja_grtalca()
    bg6b.activate_zadnja_grtalca()
    bg6b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    bg6b.add_sequence(grip_back_plant(check))

    return bg6b.operations


def yellow_get_1_front(check=False, off=120):
    g1f = Strategy()

    g1f.back_all_off()
    g1f.front_all_on()

    g1f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g1f.go_to_XY(1500, 1500, off=off, at=0, b=100)
    g1f.add_sequence(prepare_front_arm())
    g1f.deactivate_zadnja_grtalca()
    g1f.activate_prednja_grtalca()
    g1f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g1f.add_sequence(grip_front_plant(check))

    return g1f.operations


def yellow_get_1_back(check=False, off=120):
    g1b = Strategy()

    g1b.front_all_off()
    g1b.back_all_on()

    g1b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g1b.go_to_XY(1500, 1500, False, off=off, at=0, b=100)
    g1b.add_sequence(prepare_back_arm())
    g1b.deactivate_prednja_grtalca()
    g1b.activate_zadnja_grtalca()
    g1b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g1b.add_sequence(grip_back_plant(check))

    return g1b.operations


def yellow_get_2_front(check=False, off=120):
    g2f = Strategy()

    g2f.back_all_off()
    g2f.front_all_on()

    g2f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g2f.go_to_XY(1300, 1000, off=off, at=0, b=100)
    g2f.add_sequence(prepare_front_arm())
    g2f.deactivate_zadnja_grtalca()
    g2f.activate_prednja_grtalca()
    g2f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g2f.add_sequence(grip_front_plant(check))

    return g2f.operations


def yellow_get_2_back(check=False, off=120):
    g2b = Strategy()

    g2b.front_all_off()
    g2b.back_all_on()

    g2b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g2b.go_to_XY(1300, 1000, False, off=off, at=0, b=100)
    g2b.add_sequence(prepare_back_arm())
    g2b.deactivate_prednja_grtalca()
    g2b.activate_zadnja_grtalca()
    g2b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g2b.add_sequence(grip_back_plant(check))

    return g2b.operations


def yellow_get_3_front(check=False, off=120):
    g3f = Strategy()

    g3f.back_all_off()
    g3f.front_all_on()

    g3f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g3f.go_to_XY(700, 1000, off=off, at=0, b=100)
    g3f.add_sequence(prepare_front_arm())
    g3f.deactivate_zadnja_grtalca()
    g3f.activate_prednja_grtalca()
    g3f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g3f.add_sequence(grip_front_plant(check))

    return g3f.operations


def yellow_get_3_back(check=False, off=120):
    g3b = Strategy()

    g3b.front_all_off()
    g3b.back_all_on()

    g3b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g3b.go_to_XY(700, 1000, False, off=off, at=0, b=100)
    g3b.add_sequence(prepare_back_arm())
    g3b.deactivate_prednja_grtalca()
    g3b.activate_zadnja_grtalca()
    g3b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g3b.add_sequence(grip_back_plant(check))

    return g3b.operations


def yellow_get_4_front(check=False, off=120):
    g4f = Strategy()

    g4f.back_all_off()
    g4f.front_all_on()

    g4f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g4f.go_to_XY(500, 1500, off=off, at=0, b=100)
    g4f.add_sequence(prepare_front_arm())
    g4f.deactivate_zadnja_grtalca()
    g4f.activate_prednja_grtalca()
    g4f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g4f.add_sequence(grip_front_plant(check))

    return g4f.operations


def yellow_get_4_back(check=False, off=120):
    g4b = Strategy()

    g4b.front_all_off()
    g4b.back_all_on()

    g4b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g4b.go_to_XY(500, 1500, False, off=off, at=0, b=100)
    g4b.add_sequence(prepare_back_arm())
    g4b.deactivate_prednja_grtalca()
    g4b.activate_zadnja_grtalca()
    g4b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g4b.add_sequence(grip_back_plant(check))

    return g4b.operations


def yellow_get_5_front(check=False, off=120):
    g5f = Strategy()

    g5f.back_all_off()
    g5f.front_all_on()

    g5f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g5f.go_to_XY(700, 2000, off=off, at=0, b=100)
    g5f.add_sequence(prepare_front_arm())
    g5f.deactivate_zadnja_grtalca()
    g5f.activate_prednja_grtalca()
    g5f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g5f.add_sequence(grip_front_plant(check))

    return g5f.operations


def yellow_get_5_back(check=False, off=120):
    g5b = Strategy()

    g5b.front_all_off()
    g5b.back_all_on()

    g5b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g5b.go_to_XY(700, 2000, False, off=off, at=0, b=100)
    g5b.add_sequence(prepare_back_arm())
    g5b.deactivate_prednja_grtalca()
    g5b.activate_zadnja_grtalca()
    g5b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g5b.add_sequence(grip_back_plant(check))

    return g5b.operations


def yellow_get_6_front(check=False, off=120):
    g6f = Strategy()

    g6f.back_all_off()
    g6f.front_all_on()

    g6f.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g6f.go_to_XY(1300, 2000, off=off, at=0, b=100)
    g6f.add_sequence(prepare_front_arm())
    g6f.deactivate_zadnja_grtalca()
    g6f.activate_prednja_grtalca()
    g6f.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g6f.add_sequence(grip_front_plant(check))

    return g6f.operations


def yellow_get_6_back(check=False, off=120):
    g6b = Strategy()

    g6b.front_all_off()
    g6b.back_all_on()

    g6b.start_step_actions()
    # ide do biljaka kod sime to jest prvi tanjir
    g6b.go_to_XY(1300, 2000, False, off=off, at=0, b=100)
    g6b.add_sequence(prepare_back_arm())
    g6b.deactivate_prednja_grtalca()
    g6b.activate_zadnja_grtalca()
    g6b.end_step_actions()

    # provjerava da li postoje biljke na prvom tanjiru
    g6b.add_sequence(grip_back_plant(check))

    return g6b.operations


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
