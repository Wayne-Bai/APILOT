import numpy as np
from scipy.ndimage import uniform_filter, uniform_filter1d

def apply_uniform_filter_nd(array, size):
    """
    Apply a multidimensional uniform filter to the array.

    Parameters:
    -----------
    array : ndarray
        Input array to which the filter will be applied.
    size : int
        Size of the filter in each dimension.

    Returns:
    --------
    ndarray
        The array after applying the uniform filter.
    """
    if not isinstance(array, np.ndarray):
        raise ValueError("Input array should be of type ndarray")

    # Convert the input array to float to avoid overflow issues
    array = array.astype(np.float32)

    # Apply the uniform filter in each dimension
    filtered_array = uniform_filter1d(array, size, axis=0)  # Apply along the first axis as an example
    filtered_array = uniform_filter1d(filtered_array, size, axis=1)  # Apply along the second axis as an example

    return filtered_array

# Example usage:
input_array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
filtered_array = apply_uniform_filter_nd(input_array, size=2)
print(filtered_array)
