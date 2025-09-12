
import numpy as np
from scipy import ndimage

def multidimensional_maximum_filter(img, size):
    """
    Apply a multidimensional maximum filter to an image.
    
    Parameters:
        img (np.array): The input image.
        size (int or tuple of ints): The size of the filter window.
        
    Returns:
        np.array: The output of the filter.
    """
    # Calculate the radius of the filter
    radius = (size - 1) // 2
    
    # Define the filter kernel
    kernel = np.ones((radius, radius), dtype=np.uint8)
    
    # Apply the maximum filter to the image using the defined kernel
    result = ndimage.maximum_filter(img, size=size, footprint=kernel)
    
    return result
