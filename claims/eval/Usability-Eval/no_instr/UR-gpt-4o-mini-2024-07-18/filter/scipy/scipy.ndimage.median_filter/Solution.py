import numpy as np
from scipy.ndimage import median_filter

def multidimensional_median_filter(image, size):
    """
    Apply a multidimensional median filter to the given image.

    Args:
        image (ndarray): Input image array.
        size (int or tuple): The size of the filter. 
                             If an integer is provided, a square filter of that size is used.
                             If a tuple is provided, it defines the size along each dimension.

    Returns:
        ndarray: The filtered image.
    """
    return median_filter(image, size=size)

# Example usage:
# image = np.random.rand(100, 100)  # Create a random 2D image
# filtered_image = multidimensional_median_filter(image, size=3)
