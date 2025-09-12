import numpy as np
from scipy.ndimage import generic_filter

def percentile_filter(arr, percentile, size):
    return generic_filter(arr, lambda x: np.percentile(x, percentile), size=size)
