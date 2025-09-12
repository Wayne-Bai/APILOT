import scipy.ndimage as ndimage
import numpy as np

def multidimensional_median_filter(data, size):
    """
    Apply a multidimensional median filter to the data.

    Parameters:
    data (numpy.ndarray): The data to be filtered.
    size (int or tuple): The size of the filter.

    Returns:
    filtered_data (numpy.ndarray): The filtered data.
    """
    # Ensure size is a tuple
    if isinstance(size, int):
        size = (size,) * data.ndim
    
    # Apply the median filter
    filtered_data = ndimage.median_filter(data, size=size)
    
    return filtered_data

# Example usage
if __name__ == "__main__":
    # Generate some noisy data
    data = np.random.normal(0, 1, (10, 10))
    
    # Apply the median filter
    filtered_data = multidimensional_median_filter(data, size=3)
    
    # Print the original and filtered data
    print("Original Data:")
    print(data)
    print("\nFiltered Data:")
    print(filtered_data)
