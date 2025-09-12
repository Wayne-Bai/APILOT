
import numpy as np

def get_max_indices(arr, axis=None):
    return np.argwhere(arr == np.amax(arr, axis=axis)).ravel()
