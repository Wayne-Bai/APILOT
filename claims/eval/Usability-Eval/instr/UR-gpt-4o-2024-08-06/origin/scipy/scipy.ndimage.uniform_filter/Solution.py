import numpy as np
from scipy.ndimage import uniform_filter

def multidimensional_uniform_filter(input_array, size):
    """
    Apply a multidimensional uniform filter to the input array.

    Parameters:
    - input_array: The input multidimensional array to be filtered.
    - size: The size of the uniform filter (e.g., 3, 5, etc.).

    Returns:
    - The filtered array.
    """
    # Apply the uniform filter with given size
    filtered_array = uniform_filter(input_array, size=size)
    return filtered_array

# Example usage
input_data = np.random.rand(5, 5)  # Example 2D array
filter_size = 3
result = multidimensional_uniform_filter(input_data, filter_size)
print("Original Array:\n", input_data)
print("Filtered Array:\n", result)
