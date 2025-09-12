import numpy as np

def weighted_average(arr, weights, axis=None):
    if axis is None:
        axis = np.ndim(arr) - 1

    weighted_sum = np.sum(arr * weights, axis=axis)
    return weighted_sum / np.sum(weights, axis=axis)
