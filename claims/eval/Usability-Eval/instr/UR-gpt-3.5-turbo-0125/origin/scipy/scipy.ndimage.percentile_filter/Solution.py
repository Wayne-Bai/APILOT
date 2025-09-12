
import numpy as np
from scipy.ndimage import generic_filter

def percentile_filter(data, percentile=50, size=3):
    def percentile_func(arr):
        return np.percentile(arr, percentile)

    result = generic_filter(data, percentile_func, size=size)
    return result
