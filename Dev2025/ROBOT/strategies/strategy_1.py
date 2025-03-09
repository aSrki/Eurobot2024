# NOVA STRATEGIJA, ROKI GA POKUSAO NAPISAT'
from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy1 = Strategy()

# pocetne koordinate x=1775 y=175

# strategy1.move_front_wall() 
#     # podize zid gore da bi mogao da nasadi baner
#     # mozda je bolje ako bi u pocetnom polozaju, inicijalizacija ili nesto
#     # namestili da se zid drzi podignut da moze sto pre nasaditi baner

# strategy1.go_to_XY(1775, 160, False) # pomeri se za 15mm unazad
# strategy1.move_front_wall() # spusta baner na ivicu zida
# strategy1.magnets_off() # gasi magnete da moze dalje
# strategy1.go_to_XY(1775, 300)
# strategy1.go_to_XY(1900, 650)
# strategy1.go_to_XY(1900, 773.5) # ispravio je putanju i dosao do konzervi

# strategy1.add_sequence(catch_two()) # funkcija za hvatanje prva dva, treba je napraviti u tasks
# strategy1.go_to_XY(1900, 623.5)
# strategy1.set_distance_angle(0, 90)
# strategy1.go_to_XY(1100, 623.5)
# strategy1.set_distance_angle(150, 90) # namesta se za hvatanje zadnjim zidom
# strategy1.add_sequence(catch_third()) # uhvatio treci sprat

# strategy1.go_to_XY(1175, 600)
# # strategy1.rotate_to()
# strategy1.go_to_XY(1775, 260)
# strategy1.add_sequence(level_two())
# strategy1.go_to_XY(1775, 360, False)
# strategy1.set_distance_angle(0, 180)
# strategy1.go_to_XY(1755, 260)
# strategy1.add_sequence(level_three())

# # /////// gotova prva trospratnica 

# strategy1.set_distance_angle(-300, 0)
# strategy1.go_to_XY(2225, 560)
# strategy1.set_distance_angle(-90)
# strategy1.go_to_XY(2225, 426.5) # prilazi sledecem steku i treba da ga pokupi
# strategy1.add_sequence(catch_two())
# strategy1.go_to_XY(2225, 190)
# strategy1.add_sequence(level_two()) # slozio dvospratnicu

# strategy1.go_to_XY(2225, 400, False)
# strategy1.set_distance_angle(0, -90)
# strategy1.go_to_XY(2750, 400, False)
# strategy1.add_sequence(catch_third())
# strategy1.set_distance_angle(100, 0)
# strategy1.go_to_XY(2225, 560)
# strategy1.go_to_XY(2225, 190, False) # treba da se zarotira i pridje zadnjom stranom
# strategy1.add_sequence(level_three())

# # /////// gotova druga trospratnica

# strategy1.go_to_XY(2175, 1560) # prednjom stranom hvatamo reserved stek
# strategy1.add_sequence(catch_two()) # ALI MORAMO PAZITI jer se ovaj stek mora izvuci
#     # pa odraditi flip i sve da ne bi udarili/sjebali binu i sve 
# strategy1.go_to_XY(2175, 1200, False)
# strategy1.go_to_XY(2500, 1325, False)
# strategy1.go_to_XY(2750, 1325, False)
# strategy1.add_sequence(catch_third()) 
# strategy1.go_to_XY(1775, 900)
# strategy1.go_to_XY(1775, 490)

# strategy1.add_sequence(level_two())
# strategy1.go_to_XY(1775, 690, False)
# strategy1.set_distance_angle(0, 180)
# strategy1.go_to_XY(1775, 490, False)
# strategy1.add_sequence(level_three()) 

# # /////// gotova treca trospratnica

# strategy1.go_to_XY(2480, 1200)
# strategy1.go_to_XY(2480, 1800)

# # /////// mali se uparkir'o

# # strategy1.rotate_to(0)
# # strategy1.start_step_actions()
# # strategy1.go_to_XY(195, 750, g=0.4, s=1.5)  # rotira panele #y = 750
# # strategy1.activate_triangle()
# # strategy1.end_step_actions()
# # # strategy1.move_front_arm(110)  # podize ruke da ne pojebe potove

# # strategy1.start_step_actions()
# # strategy1.go_to_XY(500, 1210)  # dolazi do tanjira 4
# # strategy1.deactivate_triangle()
# # # strategy1.add_sequence(prepare_arms())  # priprema za hvatanje
# # strategy1.end_step_actions()


# # strategy1.rotate_to(0)
# # # strategy1.set_distance_angle(95, 0) #ubaceno u task da bi bilo brze
# # strategy1.add_sequence(grip_front_plant())
# # strategy1.set_distanc100e_angle(0, 179)
# # strategy1.rotate_to(180)
# # # strategy1.set_distance_angle(-230, 0) #ubaceno u task da bi bilo brze
# # strategy1.add_sequence(grip_back_plant())
# # strategy1.go_to_XY(250, 300)  # 350
# # strategy1.add_sequence(release_front_plant())
# # strategy1.set_distance_angle(-170, 0)
# # strategy1.rotate_to(-30)  # 0
# # strategy1.add_sequence(release_back_plant())
# # # strategy1.set_distance_angle(100, 0)

# # strategy1.go_to_XY(700, 680)  # 690
# # # strategy1.add_sequence(prepare_arms())

# # strategy1.rotate_to(6)
# # # strategy1.set_distance_angle(95, 0) # ubaceno u task
# # strategy1.add_sequence(grip_front_plant())  # 30
# # strategy1.rotate_to(180)
# # # strategy1.add_sequence(prepare_back_arm())
# # # strategy1.set_distance_angle(-230, -3, s=0.1) #ubaceno u task
# # strategy1.add_sequence(grip_back_plant())

# # # strategy1.go_to_XY(1342, 600)  # 1352 je po crtezu -35mm da uhvati prve dve
# # # strategy1.go_to_XY(1342, 285)  # 275

# # # ======================== stara dobra radi lepo =================
# # # strategy1.add_sequence(front_plant_in_pot())
# # # strategy1.go_to_XY(1377, 305, False) #295
# # # strategy1.rotate_to(3)
# # # strategy1.set_distance_angle(-100, 0) #-120
# # # strategy1.add_sequence(back_plant_in_pot())
# # # strategy1.go_to_XY(1377, 152, False)
# # # strategy1.add_sequence(drop_back_plant())
# # # strategy1.set_distance_angle(100, 0)
# # # strategy1.go_to_XY(1400, 245)
# # # strategy1.rotate_to(177)
# # # strategy1.set_distance_angle(80, 0)
# # # strategy1.add_sequence(drop_front_plant())
# # # -==================== kraj stare dobre =========================

# # # ====================NOVO BOLJE TESTIRANO ====================
# # # strategy1.add_sequence(front_plant_in_pot())
# # # strategy1.go_to_XY(1342, 215)  # 205
# # # strategy1.add_sequence(drop_front_plant())
# # # strategy1.set_distance_angle(-100, 0)
# # # strategy1.go_to_XY(1377, 305, False)
# # # strategy1.rotate_to(0)
# # # strategy1.set_distance_angle(-120, 0)  # -120
# # # strategy1.set_distance_angle(30, 0)
# # # strategy1.add_sequence(back_plant_in_pot())
# # # strategy1.go_to_XY(1377, 152, False)
# # # strategy1.add_sequence(drop_back_plant())
# # # ======================KRAJ ================================

# # strategy1.go_to_XY(1382, 600)  # 1377 je po crtezu -35mm da uhvati prve dve
# # strategy1.start_step_actions()
# # strategy1.go_to_XY(1382, 285)
# # strategy1.move_front_arm(120)
# # strategy1.end_step_actions()

# # strategy1.add_sequence(memristor_front())
# # strategy1.set_distance_angle(-85, 0)
# # strategy1.go_to_XY(1377, 210, False)  # x = 305 bilo je i 240
# # strategy1.rotate_to(0)
# # strategy1.add_sequence(memristor_back())


# # strategy1.start_step_actions()
# # strategy1.go_to_XY(1300, 700)
# # # strategy1.add_sequence(prepare_arms())
# # strategy1.end_step_actions()

# # strategy1.rotate_to(0)
# # # strategy1.set_distance_angle(100, 0)
# # strategy1.add_sequence(grip_front_plant())
# # strategy1.rotate_to(180)
# # # strategy1.set_distance_angle(-230, -3, s=0.1) #ubaceno u task
# # strategy1.add_sequence(grip_back_plant())
# # strategy1.go_to_XY(1300, 812)
# # strategy1.go_to_XY(1850, 812)  # 762
# # strategy1.add_sequence(leave_front_plant())
# # strategy1.set_distance_angle(-50, 0)
# # strategy1.go_to_XY(1700, 712, False)  # 762
# # strategy1.go_to_XY(1850, 712, False)  # 762
# # strategy1.add_sequence(leave_back_plant())
# # strategy1.set_distance_angle(100, 0)
# # strategy1.go_to_XY(1775, 700)
# # # strategy1.go_to_XY(195, 1655)

strategy1.end()
