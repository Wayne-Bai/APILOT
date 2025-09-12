import numpy as np

def pad_array(arr, pad_width, mode='constant', constant_values=0):
    return np.pad(arr, pad_width, mode=mode, constant_values=constant_values)
