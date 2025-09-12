import numpy as np
from scipy.ndimage import generic_filter

def rank_filter(input, size=3, rank=5):
    """
    Calculate a multidimensional rank filter.

    Parameters:
    input (numpy.ndarray): The input array to be filtered.
    size (int): The size of the filter window.
    rank (int): The rank of the filter.

    Returns:
    numpy.ndarray: The filtered array.
    """
    # Define the rank filter function
    def rank_filter_func(sub_array):
        return np.percentile(sub_array, rank)

    # Apply the rank filter to the input array
    filtered_array = generic_filter(input, rank_filter_func, size=size)

    return filtered_array
