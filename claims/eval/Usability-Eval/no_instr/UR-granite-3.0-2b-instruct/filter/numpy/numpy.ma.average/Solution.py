import numpy as np

def weighted_average(arr, weights, axis=None):
    if axis is None:
        axis = np.ndim(arr) - 1

    if not np.issubdtype(arr.dtype, np.number):
        raise ValueError("Array elements must be numeric")

    if not np.issubdtype(weights.dtype, np.number) or weights.sum() == 0:
        raise ValueError("Weights must be numeric and non-zero")

    return np.average(arr, weights=weights, axis=axis)
