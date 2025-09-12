import scipy.ndimage as ndi
import numpy as np

def multidimensional_minimum_filter(data, size):
    """
    Calculate a multidimensional minimum filter.

    Parameters:
    - data (numpy.ndarray): Input data.
    - size (int or tuple): Size of the filter.

    Returns:
    - filtered_data (numpy.ndarray): Minimum filtered data.
    """
    # Ensure size is a tuple
    if isinstance(size, int):
        size = (size,) * len(data.shape)

    # Apply minimum filter
    filtered_data = ndi.minimum_filter(data, size=size)

    return filtered_data

# Example usage
if __name__ == "__main__":
    # Generate random 3D data
    np.random.seed(0)
    data = np.random.rand(10, 10, 10)

    # Apply minimum filter with a size of 3
    filtered_data = multidimensional_minimum_filter(data, size=3)

    # Print original and filtered data shapes
    print("Original data shape:", data.shape)
    print("Filtered data shape:", filtered_data.shape)
