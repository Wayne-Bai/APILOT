import numpy as np
from scipy.ndimage import minimum_filter

def apply_multidimensional_minimum_filter(input_array, size):
    """
    Apply a multidimensional minimum filter to the input array.

    Parameters:
    input_array (numpy.ndarray): The input array to filter.
    size (int or tuple): The size of the filter kernel.

    Returns:
    numpy.ndarray: The filtered array.
    """
    return minimum_filter(input_array, size=size)

# Example usage
if __name__ == "__main__":
    # Create a sample 2D array
    sample_array = np.array([[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12],
                              [13, 14, 15, 16]])

    # Apply the minimum filter with a kernel size of (3, 3)
    filtered_array = apply_multidimensional_minimum_filter(sample_array, size=(3, 3))
    print(filtered_array)
