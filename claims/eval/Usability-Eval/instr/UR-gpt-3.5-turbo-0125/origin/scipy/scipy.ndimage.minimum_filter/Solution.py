
import numpy as np
from scipy.ndimage import generic_filter

def min_filter(data, size):
    result = generic_filter(data, np.min, size=size)
    return result
