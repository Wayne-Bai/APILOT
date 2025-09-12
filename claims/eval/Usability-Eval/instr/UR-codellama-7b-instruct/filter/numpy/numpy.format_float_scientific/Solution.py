
import numpy as np

def format_float_scientific(value, precision=None):
    return np.format_float_positional(value, precision, "e", suppress_small=True)
