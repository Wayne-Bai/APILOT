import numpy as np
def weighted_avg(arr, weights, axis):
    return np.average(arr, weights=weights, axis=axis)
