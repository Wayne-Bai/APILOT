import numpy as np
from scipy.ndimage import median_filter

def multidimensional_median_filter(data, size):
    """
    Apply a multidimensional median filter to the input data.

    Parameters:
    data (ndarray): The input array to apply the filter to.
    size (int): The size of the filter. This should be a positive odd integer.
                For instance, size=3 results in a 1x1x3 filter in general.

    Returns:
    ndarray: The filtered array.
    """
    # Apply median filter in the specified direction
    filtered_data = median_filter(data, size=(size, size, size))

    return filtered_data

# Example usage:
if __name__ == "__main__":
    # Create a simple 3D data example
    data = np.random.rand(10, 10, 10)

    # Define the filter size
    filter_size = 3

    # Apply the filter
    filtered_data = multidimensional_median_filter(data, filter_size)

    # Print the filtered data
    print(filtered_data)
