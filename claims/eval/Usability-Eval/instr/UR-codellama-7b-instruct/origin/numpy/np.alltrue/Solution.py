import numpy as np

def all_true(arr, axis):
    return np.all(arr == True, axis=axis)
