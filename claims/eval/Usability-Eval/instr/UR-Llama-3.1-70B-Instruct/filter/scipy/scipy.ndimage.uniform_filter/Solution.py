import scipy.ndimage as ndi
import numpy as np

def uniform_filter(data, size):
    """
    Apply a multidimensional uniform filter.

    Parameters:
    data (ndarray): The input data.
    size (int or tuple of ints): The size of the filter.

    Returns:
    filtered_data (ndarray): The filtered data.
    """
    # Ensure size is a tuple of ints to support multidimensional filters
    if isinstance(size, int):
        size = (size,) * len(data.shape)

    # Apply the uniform filter
    filtered_data = ndi.uniform_filter(data, size=size)

    return filtered_data

# Example usage:
data = np.random.rand(10, 10)
filtered_data = uniform_filter(data, size=3)
print(filtered_data)
