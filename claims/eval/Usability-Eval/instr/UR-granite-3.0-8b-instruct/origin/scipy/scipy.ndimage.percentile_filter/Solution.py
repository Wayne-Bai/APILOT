import numpy as np
from scipy.ndimage import generic_filter

def percentile_filter(image, percentile=50, window_size=3):
    """
    Calculate a multidimensional percentile filter.

    Parameters:
    image (numpy.ndarray): The input image.
    percentile (int): The percentile to use for the filter.
    window_size (int): The size of the window for the filter.

    Returns:
    numpy.ndarray: The filtered image.
    """
    def percentile_func(arr):
        return np.percentile(arr, percentile, axis=None)

    return generic_filter(image, percentile_func, size=window_size)
