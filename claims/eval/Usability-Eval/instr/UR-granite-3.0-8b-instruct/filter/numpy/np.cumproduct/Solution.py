import numpy as np

def cumulative_product(arr, axis):
    return np.cumprod(arr, axis=axis)
