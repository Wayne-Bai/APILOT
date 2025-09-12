import numpy as np
from scipy.ndimage import generic_filter

def multidimensional_median_filter(image, size):
    return generic_filter(image, np.median, size=size)
