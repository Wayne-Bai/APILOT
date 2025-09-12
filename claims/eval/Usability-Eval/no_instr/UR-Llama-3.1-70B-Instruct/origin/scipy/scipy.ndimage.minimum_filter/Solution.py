import numpy as np
from scipy import ndimage

def multidimensional_minimum_filter(data, size):
    """
    Apply a multidimensional minimum filter to the input data.

    Parameters:
    data (ndarray): The input data.
    size (int or tuple): The size of the filter.

    Returns:
    filtered_data (ndarray): The filtered data.
    """
    # If size is an integer, convert it to a tuple
    if isinstance(size, int):
        size = (size,) * len(data.shape)

    # Apply the minimum filter
    filtered_data = ndimage.minimum_filter(data, size=size)

    return filtered_data

# Example usage:
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    data = np.random.randint(0, 100, size=(5, 5))

    print("Original Data:")
    print(data)

    # Apply the minimum filter
    filtered_data = multidimensional_minimum_filter(data, size=2)

    print("\nFiltered Data:")
    print(filtered_data)
