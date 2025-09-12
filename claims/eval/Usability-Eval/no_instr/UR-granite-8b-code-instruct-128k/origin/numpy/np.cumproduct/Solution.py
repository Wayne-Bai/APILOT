import numpy as np

def cumulative_product(arr, axis=0):
    return np.cumprod(arr, axis=axis)