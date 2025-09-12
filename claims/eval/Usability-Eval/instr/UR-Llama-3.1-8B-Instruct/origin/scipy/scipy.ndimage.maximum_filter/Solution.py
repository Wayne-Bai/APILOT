# Import necessary libraries from scipy
from scipy import signal

# Define a 2D array to perform the maximum filter on
def calculate_max_filter(image, kernel_size):
    """
    Calculate a multidimensional maximum filter.

    Args:
    image (numpy.ndarray): The input image to apply the filter on.
    kernel_size (tuple): The size of the kernel in each dimension.

    Returns:
    numpy.ndarray: The filtered image.
    """
    # Use the signal.convolve2d function to apply the maximum filter
    # The mode='same' ensures the output image is the same size as the input
    kernel = np.ones(kernel_size)
    filtered_image = signal.convolve2d(image, kernel, mode='same', boundary='fill')
    
    # Replace values at the boundary with the maximum value in the image
    filtered_image[:kernel_size[0]//2] = np.max(image)
    filtered_image[-kernel_size[0]//2:] = np.max(image)
    filtered_image[:, :kernel_size[1]//2] = np.max(image, axis=0)
    filtered_image[:, -kernel_size[1]//2:] = np.max(image, axis=0)

    return filtered_image

# Import necessary libraries
import numpy as np

# Generate a sample 2D array to perform the maximum filter on
image = np.random.randint(0, 100, size=(10, 10))

# Define the kernel size
kernel_size = (3, 3)

# Calculate the maximum filter
filtered_image = calculate_max_filter(image, kernel_size)

print("Original Image:")
print(image)

print("\nFiltered Image:")
print(filtered_image)
