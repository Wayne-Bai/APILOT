import numpy as np
from scipy.ndimage import median_filter

def apply_multidimensional_median_filter(data, size):
    """
    Apply a multidimensional median filter to the input data.
    
    Parameters:
    - data: ndarray
        Input data to which the median filter will be applied.
    - size: int or tuple of ints
        The size of the filter to be applied. If an integer is provided,
        the same filter size is used in all dimensions. If a tuple, 
        each dimension can have a different size.
    
    Returns:
    - filtered_data: ndarray
        The filtered data after applying the median filter.
    """
    filtered_data = median_filter(data, size=size)
    return filtered_data

# Example usage
if __name__ == "__main__":
    # Create a sample 3D array
    sample_data = np.random.rand(5, 5, 5)
    filter_size = 3

    # Apply the median filter
    result = apply_multidimensional_median_filter(sample_data, filter_size)
    print("Filtered Data:\n", result)
