#modelop.schema.0: input_schema.avsc
#modelop.slot.1: in-use

from utilities.helper_functions import square_root, global_var


#modelop.init
def begin():
    pass


#modelop.score
def action(data):
    yield {"global_var": global_var, "sqrt": square_root(data)}


#modelop.metrics
def metrics(data):
    yield{"AUC":1}
