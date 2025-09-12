import numpy as np

def cumulative_product(arr, axis=None):
    return np.cumprod(arr, axis=axis)
