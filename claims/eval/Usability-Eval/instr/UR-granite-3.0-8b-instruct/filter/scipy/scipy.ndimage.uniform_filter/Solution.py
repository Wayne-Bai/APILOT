import numpy as np
from scipy.ndimage import uniform_filter1d, uniform_filter

def multidimensional_uniform_filter(image, size):
    """
    Apply a multidimensional uniform filter to an image.

    Parameters:
    image (numpy.ndarray): The input image.
    size (int or tuple): The size of the filter.

    Returns:
    numpy.ndarray: The filtered image.
    """
    if isinstance(size, int):
        size = (size, size)

    # Apply 1D uniform filter along each axis
    filtered_image = image.copy()
    for axis in range(image.ndim):
        filtered_image = uniform_filter1d(filtered_image, size[axis], axis=axis)

    return filtered_image
