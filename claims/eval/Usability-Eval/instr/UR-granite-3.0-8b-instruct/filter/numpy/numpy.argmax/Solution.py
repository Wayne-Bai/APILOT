import numpy as np

def find_max_indices(arr, axis=0):
    max_values = np.max(arr, axis=axis)
    max_indices = np.argwhere(arr == max_values[:, np.newaxis])
    return max_indices
