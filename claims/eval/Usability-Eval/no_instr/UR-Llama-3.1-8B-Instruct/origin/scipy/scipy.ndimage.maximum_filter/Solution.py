import numpy as np
from scipy import ndimage

def calculate_max_filter(image, kernel_size):
    """
    Calculate the multidimensional maximum filter of an image.

    Parameters:
    image (numpy array): The input image.
    kernel_size (tuple): The size of the kernel.

    Returns:
    filtered_image (numpy array): The filtered image.
    """
    # Create a kernel of ones with the specified size
    kernel = np.ones(kernel_size)

    # Calculate the maximum filter using the maximum filter function from scipy
    filtered_image = ndimage.maximum_filter(image, size=kernel_size, mode='constant')

    return filtered_image

# Example usage:
image = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

kernel_size = (2, 2)

filtered_image = calculate_max_filter(image, kernel_size)
print("Filtered Image:")
print(filtered_image)
