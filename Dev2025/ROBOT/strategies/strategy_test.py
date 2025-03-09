# NOVA STRATEGIJA, ROKI GA POKUSAO NAPISAT'
from strategies.tasks import *
from strategies.steps import *
from strategies.strategy import Strategy

strategy_test = Strategy()

strategy_test.flip_left_hand(a=90, v=30)
strategy_test.flip_left_hand(a=180, v=30)
strategy_test.flip_left_hand(a=270, v=30)
#strategy_test.flip_left_hand(a=90, v=50)

# 
# 
# 
# 
strategy_test.end()
