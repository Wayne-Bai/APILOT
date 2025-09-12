import numpy as np

def find_common_type(*args):
    # Find the common type by iterating over the input arguments
    common_type = None
    for arg in args:
        if common_type is None:
            common_type = np.dtype(type(arg))
        else:
            common_type = np.find_common_type([common_type, np.dtype(type(arg))], [])
    return common_type
