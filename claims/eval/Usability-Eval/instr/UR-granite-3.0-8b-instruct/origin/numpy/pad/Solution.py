import numpy as np

def pad_array(arr, pad_width, mode='constant'):
    return np.pad(arr, pad_width, mode)
