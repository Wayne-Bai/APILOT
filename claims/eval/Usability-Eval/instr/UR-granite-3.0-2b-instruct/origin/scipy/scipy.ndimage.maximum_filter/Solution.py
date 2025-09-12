from scipy import ndimage
import numpy as np

def multidimensional_maximum_filter(image, size):
    """
    This function applies a multidimensional maximum filter to the input image.

    Parameters:
    image (numpy.ndarray): The input multidimensional image.
    size (int): The size of the filtering kernel.

    Returns:
    numpy.ndarray: The filtered image.
    """
    return ndimage.maximum_filter(image, size)
