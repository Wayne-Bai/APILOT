import numpy as np
from scipy.ndimage import percentile_filter

def multidimensional_percentile_filter(data, percentile):
    """
    This function applies a multidimensional percentile filter to the input data.

    Parameters:
    data (numpy.ndarray): The input data as a multidimensional numpy array.
    percentile (float): The percentile value to use for the filter.

    Returns:
    numpy.ndarray: The filtered data as a multidimensional numpy array.
    """
    return percentile_filter(data, percentile)
