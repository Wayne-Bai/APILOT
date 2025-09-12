import numpy as np
from scipy.ndimage import gaussian_filter1d

def max_filter(arr, size):
    """Calculates a multidimensional maximum filter using SciPy's gaussian_filter1d."""
    # Calculate the standard deviation of the filter
    std = (size - 1) / 2.0
    
    # Apply the filter to each dimension separately
    for i in range(arr.ndim):
        arr[:, :, i] = gaussian_filter1d(arr[:, :, i], std, mode='reflect')
    
    return arr
