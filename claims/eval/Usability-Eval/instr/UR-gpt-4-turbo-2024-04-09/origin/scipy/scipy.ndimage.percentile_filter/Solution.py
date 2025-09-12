import numpy as np
from scipy.ndimage import generic_filter

def percentile_filter(input_array, size, percentile):
    """
    Apply a percentile filter to a multidimensional array.

    Parameters:
        input_array (ndarray): The input array.
        size (int or tuple): Specifies the shape of the filter.
        percentile (float): The percentile to compute (0-100).
    
    Returns:
        ndarray: The filtered array.
    """
    def percentile_func(buffer):
        return np.percentile(buffer, percentile)

    return generic_filter(input_array, percentile_func, size=size)

# Example usage:
input_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]])
size = 3
percentile = 50

result = percentile_filter(input_array, size=size, percentile=percentile)
print(result)
