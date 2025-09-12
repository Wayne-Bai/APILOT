import numpy as np
from scipy.ndimage import maximum_filter

def apply_maximum_filter(input_array, size):
    """
    Apply a multidimensional maximum filter to the input array.

    Parameters:
    input_array (ndarray): Input array to which the maximum filter will be applied.
    size (int or tuple): Size of the filter. If an int is provided, it will be used in all dimensions.

    Returns:
    ndarray: The result of the maximum filter.
    """
    return maximum_filter(input_array, size=size)

# Example usage
if __name__ == "__main__":
    data = np.random.random((5, 5))
    print("Original Data:\n", data)
    filtered_data = apply_maximum_filter(data, size=3)
    print("Filtered Data:\n", filtered_data)
