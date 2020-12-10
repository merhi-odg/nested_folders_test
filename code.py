#modelop.schema.0: input_schema.avsc
#modelop.slot.1: in-use

from utilities import *

#modelop.init
def begin():
    pass
    
#modelop.score
def action(data):
    yield {"global_var": global_var, "sqrt": square_root(data)}
