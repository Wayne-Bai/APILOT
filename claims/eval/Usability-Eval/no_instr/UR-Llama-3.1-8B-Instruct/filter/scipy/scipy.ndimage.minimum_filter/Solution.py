# Import necessary libraries
from scipy.ndimage import minimum_filter

# Define a function to apply the minimum filter
def apply_minimum_filter(image, size):
    """
    Applies a multidimensional minimum filter to the given image.

    Args:
    - image (numpy array): The input image.
    - size (int or tuple): The size of the filter.

    Returns:
    - filtered_image (numpy array): The image with the minimum filter applied.
    """
    # Apply the minimum filter to the image
    filtered_image = minimum_filter(image, size=size)

    return filtered_image

# Example usage
import numpy as np

# Generate a sample 2D image
image = np.random.rand(10, 10)

# Define the size of the filter (in this case, a 3x3 filter)
filter_size = 3

# Apply the minimum filter to the image
filtered_image = apply_minimum_filter(image, filter_size)

# Print the original and filtered images
print("Original Image:")
print(image)
print("\nFiltered Image:")
print(filtered_image)
