import scipy
import numpy as np

def median_filter(input_array, kernel_size):
    """
    Apply a multidimensional median filter to the input array using the given kernel size.

    Parameters:
    input_array (np.ndarray): The input array to be filtered.
    kernel_size (int): The size of the median filter kernel.

    Returns:
    np.ndarray: The filtered output array.
    """

    if not isinstance(input_array, np.ndarray):
        raise TypeError("Input array must be a numpy array.")
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel size must be an integer.")
    if kernel_size <= 0:
        raise ValueError("Kernel size must be greater than 0.")

    return scipy.signal.medfilt(input_array, kernel_size=kernel_size)
