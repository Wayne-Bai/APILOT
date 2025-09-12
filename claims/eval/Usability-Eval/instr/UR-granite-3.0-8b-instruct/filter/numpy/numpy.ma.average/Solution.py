import numpy as np

def weighted_average(arr, weights, axis=None):
    # Calculate the sum of the array along the given axis
    sum_arr = np.sum(arr, axis=axis)

    # Calculate the sum of the weights along the given axis
    sum_weights = np.sum(weights, axis=axis)

    # Calculate the weighted average
    weighted_avg = np.true_divide(np.sum(arr * weights, axis=axis), sum_weights)

    return weighted_avg
