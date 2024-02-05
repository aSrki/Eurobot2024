from strategies.steps import *
import data

strategy_zuta = []
strategy_ljubicanstvena = []

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.BEFORE
# step.direction_is_forward = False
# step.x = 1000
# step.y = 500
# izbacivanje_desnog_donjeg_paka(step)
# operation_append(step, 112, 0)
# operation_append(step, 111, 0)
# operation_append(step, 134, 1)
# operation_append(step, 132, 1)
# #izbacivanje_levog_donjeg_paka(step)
# # operation_append(step, 15, 220, 0.2, 500)
# strategy_ljubicanstvena.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# #step.execute_operations = OperationExecution.BEFORE
# # start_ruku2(step)
# step.angle = 90
# strategy_ljubicanstvena.append(step)
# #
# # step = Step()
# # step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# # step.execute_operations = OperationExecution.BEFORE
# # step.angle = 0
# # step.distance = 300
# # operation_append(step, 15, 220, 0.2, 500)
# # #izbacivanje_desnog_donjeg_paka(step)
# # strategy_ljubicanstvena.append(step)

step = Step()
step.type_of_parameters = TypesOfSendParameters.COORDINATE
step.x = 3
step.y = 1500
strategy_zuta.append(step)

step = Step()
step.type_of_parameters = TypesOfSendParameters.COORDINATE
step.x = 3
step.y = 1500
strategy_ljubicanstvena.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.COORDINATE
# step.execute_operations = OperationExecution.BEFORE
# # start_ruku(step)
# step.direction_is_forward = False
# step.x = -1000 #-1330
# step.y = 500
# izbacivanje_levog_donjeg_paka(step)
# operation_append(step, 111, 0)
# operation_append(step, 112, 0)
# operation_append(step, 134, 1)
# operation_append(step, 132, 1)
# # operation_append(step, 16, 220, 0.5, 500)
# strategy_zuta.append(step)

# step = Step()
# step.type_of_parameters = TypesOfSendParameters.ANGLE
# step.execute_operations = OperationExecution.BEFORE
# start_ruku2(step)
# step.angle = -90
# strategy_zuta.append(step)
# #
# # step = Step()
# # step.type_of_parameters = TypesOfSendParameters.DISTANCE_ANGLE
# # step.execute_operations = OperationExecution.BEFORE
# # step.angle = 0
# # step.distance = 300
# # # operation_append(step, 15, 220,0.5, 500)
# # #izbacivanje_desnog_donjeg_paka(step)
# # strategy_zuta.append(step)


def get_last_steps():
    if data.is_table_side_blue:
        return strategy_ljubicanstvena
    else:
        return strategy_zuta
