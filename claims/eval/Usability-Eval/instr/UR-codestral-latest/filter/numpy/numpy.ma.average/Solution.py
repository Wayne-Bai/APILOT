import numpy as np

def weighted_average(array, weights, axis=None):
    return np.average(array, weights=weights, axis=axis)
