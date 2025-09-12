import numpy as np

def cumulative_product_along_axis(arr, axis):
    return np.cumprod(arr, axis=axis)
