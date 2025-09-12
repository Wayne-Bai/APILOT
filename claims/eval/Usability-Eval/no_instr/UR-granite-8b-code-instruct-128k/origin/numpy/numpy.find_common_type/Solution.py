import numpy as np

def determine_common_type(values):
    common_type = np.result_type(*values)
    return common_type
