# import data
# from strategies import strategy_0
# from strategies import strategy_1
# from strategies import strategy_2
# from strategies import strategy_3
# from strategies import strategy_4
# from strategies import strategy_5
# from strategies import strategy_6
# from strategies import strategy_7
# from strategies import strategy_8
# from strategies import strategy_9
# from strategies import strategy_13
# from strategies import strategy_15
# from strategies import strategy_16
# from strategies import strategy_14
# from strategies import strategy_13_agresivna1
# from strategies import strategy_test
# from strategies import strategy_15_agresivna1

from strategies.strategy_0 import strategy0
# from strategies.strategy_1 import strategy1
# from strategies.strategy_2 import strategy2
# from strategies.strategy_3 import strategy3
# from strategies.strategy_5 import strategy5
# from strategies.strategy3_brza import strategy3_brza
# from strategies.strategy5_brza import strategy5_brza
# from strategies.strategy_zuta_L import strategy_zuta_L
# from strategies.strategy_plava_L import strategy_plava_L
# from strategies.strategy_zuta_FULL import strategy_zuta_FULL
# from strategies.strategy_plava_FULL import strategy_plava_FULL
# from strategies.strategy_zuta_FULL_uski import strategy_zuta_FULL_uski
# from strategies.strategy_plava_FULL_uski import strategy_plava_FULL_uski
# from strategies.sest_solarana_zuta_siroka import sest_solarna_zuta_siroka
# from strategies.sest_solarna_plava_siroka import sest_solarna_plava_siroka
# from strategies.sest_solarna_plava_uska import sest_solarna_plava_uska
# from strategies.sest_solarna_zuta_uska import sest_solarna_zuta_uska
# from strategies.strategy_zuta_KAMERA import strategy_zuta_KAMERA
# from strategies.strategy_plava_KAMERA import strategy_plava_KAMERA
# from strategies.strategy_test import strategy_test

if __name__ == '__main__':
    import sys
    sys.path.append("..")

import data

debug = True


def choose_strategy():
    # data.log.add_info_message(f"Chosen strategy {data.chosen_strategy}")
    # data.log.add_info_message(f"Color of plate {data.color}")
    # data.log.add_info_message(f"Plate number: {data.plate}")

    if debug:
        print(f"Chosen strategy {data.chosen_strategy}")
        print(f"Color of plate {data.color}")

    # ovo treba izbaciti kad se krene sa strategijama !!!
    data.time_strategy_type = 97  # 95  ... 90
    data.x_current = 0
    data.y_current = 0
    data.f_current = 0
    
    data.x_start = 0
    data.y_start= 0
    data.f_start = 0
    return strategy0.operations
    

        # print(f"Plate number: {data.plate}")
    # table = "siroki"

    # if table == "siroki":
    #     if data.color == "blue":
    #         if data.type_of_strategy == "passive":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = -295  # -155
    #             data.f_current = 0
    #             return strategy_plava_KAMERA.operations  # strategy1
    #         elif data.type_of_strategy == "6solar":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = -295  # -155
    #             data.f_current = 0
    #             return sest_solarna_plava_siroka.operations  # strategy1
    #         elif data.type_of_strategy == "agressive":
    #             data.time_strategy_type = 97   # 95
    #             data.x_current = 1000  # 195
    #             data.y_current = -2705  # 295
    #             data.f_current = 0
    #             return strategy_plava_L.operations  # 2
    #     elif data.color == "yellow":
    #         if data.type_of_strategy == "passive":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = 295  # -155
    #             data.f_current = 0
    #             return strategy_zuta_KAMERA.operations  # 2
    #             # return strategy_zuta_FULL.operations  # strategy1
    #         if data.type_of_strategy == "6solar":

    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = 295  # -155
    #             data.f_current = 0
    #             return sest_solarna_zuta_siroka.operations  # strategy1
    #         elif data.type_of_strategy == "agressive":
    #             data.time_strategy_type = 97   # 95
    #             data.x_current = 1000  # 195
    #             data.y_current = 2705  # 295
    #             data.f_current = 0
    #             return strategy_zuta_L.operations  # 2

    # elif table == "uski":
    #     if data.color == "blue":
    #         if data.type_of_strategy == "passive":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = -295  # -155
    #             data.f_current = 0
    #             return strategy_plava_FULL_uski.operations
    #         elif data.type_of_strategy == "6solar":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = -295  # -155
    #             data.f_current = 0
    #             return sest_solarna_plava_uska.operations  # strategy1
    #         elif data.type_of_strategy == "agressive":
    #             data.time_strategy_type = 97   # 95
    #             data.x_current = 1000  # 195
    #             data.y_current = -2705  # 295
    #             data.f_current = 0
    #             return strategy_plava_L.operations  # 2
    #         elif data.type_of_strategy == "test":
    #             data.time_strategy_type = 100000   # 95
    #             data.x_current = 0  # 195
    #             data.y_current = 0  # 295
    #             data.f_current = 0
    #             return strategy0.operations  # 2
    #     elif data.color == "yellow":
    #         if data.type_of_strategy == "passive":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = 295  # -155
    #             data.f_current = 0
    #             return strategy_zuta_FULL_uski.operations
    #         elif data.type_of_strategy == "6solar":
    #             data.time_strategy_type = 97  # 95  ... 90
    #             data.x_current = 195
    #             data.y_current = 295  # -155
    #             data.f_current = 0
    #             return sest_solarna_zuta_uska.operations  # strategy1
    #         elif data.type_of_strategy == "agressive":
    #             data.time_strategy_type = 97   # 95
    #             data.x_current = 1000  # 195
    #             data.y_current = 2705  # 295
    #             data.f_current = 0
    #             return strategy_zuta_L.operations  # 2

    # if data.color == "blue":
    #     data.time_strategy_type = 97  # 95  ... 90
    #     data.x_current = 195
    #     data.y_current = -295  # -155
    #     data.f_current = 0
    #     return strategy_zuta_FULL.operations  # strategy1


# class choses_strategy():
#     chosen_steps = []
#     swap = 0

#     def __init__(self):
#         #self.chosen_steps = strategy_0.strategy0


#         print(f"data set:\n "
#               f"IZABRANA STRATEGIJA: {data.chosen_strategy_small} , \n")
#               # f" {data.is_table_1} ,\n"
#               # f" is table blue{data.is_table_side_blue} ,\n ")

#         # print(type(data.chosen_strategy_small))
#         # if int(data.chosen_strategy_small) == 0:
#         #     self.chosen_steps = strategy_0.strategy0
#         #     print("Izabrao strategiju 0!")
#         # elif int(data.chosen_strategy_small) == 1:
#         #     self.chosen_steps = strategy_1.strategy1
#         #     print("Izabrao strategiju 1!")
#         # elif int(data.chosen_strategy_small) == 2:
#         #     self.chosen_steps = strategy_2.strategy2
#         #     print("Izabrao strategiju 2!")
#         # elif int(data.chosen_strategy_small) == 3:
#         #     self.chosen_steps = strategy_3.strategy3
#         #     print("Izabrao strategiju 3!")
#         # elif int(data.chosen_strategy_small) == 4:
#         #     self.chosen_steps = strategy_4.strategy4
#         #     print("Izabrao strategiju 4!")
#         # elif int(data.chosen_strategy_small) == 5:
#         #     self.chosen_steps = strategy_5.strategy5
#         #     print("Izabrao strategiju 5!")
#         # elif int(data.chosen_strategy_small) == 6:
#         #     self.chosen_steps = strategy_5.strategy5
#         #     print("Izabrao strategiju 6!")
#         # elif int(data.chosen_strategy_small) == 7:
#         #     self.chosen_steps = strategy_5.strategy5
#         #     print("Izabrao strategiju 7!")
#         # elif int(data.chosen_strategy_small) == 8:
#         #     self.chosen_steps = strategy_5.strategy5
#         #     print("Izabrao strategiju 8!")
#         # elif int(data.chosen_strategy_small) == 13:
#         #     self.chosen_steps = strategy_5.strategy5
#         #     print("Izabrao strategiju 13!")

#         # else:
#         #     self.chosen_steps = strategy_9.strategy9
#         #     print("Izabrao strategiju 9!")

#         if int(data.is_table_1):
#             if int(data.is_table_side_blue):
#                 data.x_current = 1175
#                 data.f_current = 90

#                 if int(data.chosen_strategy_small) == 1:
#                     self.chosen_steps = strategy_16.strategy16
#                     print("S16 Fajl AGRESIVNA Ljubicast")

#                 elif int(data.chosen_strategy_small) == 2:
#                     self.chosen_steps = strategy_15.strategy15
#                     print("S15 Fajl PASIVNA LJUBICASTA")
#                 elif int(data.chosen_strategy_small) == 3:
#                     self.chosen_steps = strategy_15_agresivna1.strategy15_agresivna1
#                     print("TEST TEST Fajl PASIVNA LJUBICASTA")
#                 else:
#                     print("nani")
#             else:
#                 data.x_current = -1195
#                 data.f_current = -90

#                 if int(data.chosen_strategy_small) == 1:
#                     # self.chosen_steps = strategy_13_agresivna1.strategy13_agresivna1
#                     self.chosen_steps = strategy_14.strategy14
#                     print("S14 Fajl AGRESIVNA ZUTA")
#                 elif int(data.chosen_strategy_small) == 2:
#                     self.chosen_steps = strategy_13.strategy13
#                     print("S13 Fajl PASIVNA ZUTA")
#                 elif int(data.chosen_strategy_small) == 3:
#                     self.chosen_steps = strategy_13_agresivna1.strategy13_agresivna1
#                     print("S13 Fajl ULTRAAAAA")
#                 else:#3
#                     print("nani")
#         else:
#             if int(data.is_table_side_blue):
#                 data.x_current = 1175
#                 data.f_current = 90

#                 if int(data.chosen_strategy_small) == 1:
#                     self.chosen_steps = strategy_8.strategy8
#                     print("S8 Fajl")

#                 elif int(data.chosen_strategy_small) == 2:
#                     self.chosen_steps = strategy_1.strategy1
#                     print("S1 Fajl")
#                 else:#3
#                     print("nani")
#             else:
#                 data.x_current = -1195
#                 data.f_current = -90

#                 if int(data.chosen_strategy_small) == 1:
#                     self.chosen_steps = strategy_7.strategy7
#                     print("S7 Fajl")

#                 elif int(data.chosen_strategy_small) == 2:
#                     self.chosen_steps = strategy_2.strategy2
#                     print("S2 Fajl")
#                 else:#3
#                     print("nani")

# if __name__ == "__main__":
#     cs=choses_strategy()
