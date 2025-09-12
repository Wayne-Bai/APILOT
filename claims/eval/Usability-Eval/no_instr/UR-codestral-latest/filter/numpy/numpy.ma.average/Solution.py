import numpy as np

def weighted_avg(arr, weights):
    return np.average(arr, axis=0, weights=weights)
