import numpy as np

def pad_array(array, pad_width, mode, constant_values=0):
    return np.pad(array, pad_width, mode, constant_values=constant_values)
