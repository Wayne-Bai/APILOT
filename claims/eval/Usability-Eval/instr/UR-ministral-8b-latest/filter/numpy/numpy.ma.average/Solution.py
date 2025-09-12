import numpy as np

def weighted_average(arr, weights):
    arr = np.array(arr)
    weights = np.array(weights)

    weighted_sum = np.sum(arr * weights, axis=0)
    total_weight = np.sum(weights, axis=0)

    weighted_average = weighted_sum / total_weight
    return weighted_average
