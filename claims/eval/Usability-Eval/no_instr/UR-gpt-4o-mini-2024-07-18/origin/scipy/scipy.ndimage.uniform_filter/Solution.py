import numpy as np
from scipy.ndimage import uniform_filter

def apply_uniform_filter(data, size):
    """
    Apply a multidimensional uniform filter to the input data.
    
    Parameters:
    data (ndarray): Input array.
    size (int or tuple of ints): Size of the filter. It can be a single integer for a square filter or a 
                                  tuple to specify different sizes for different dimensions.
    
    Returns:
    ndarray: Filtered output array.
    """
    return uniform_filter(data, size=size)

# Example usage
if __name__ == "__main__":
    # Creating a sample 2D array
    sample_data = np.random.rand(5, 5)
    print("Original Data:\n", sample_data)

    # Applying a uniform filter with a size of 3
    filtered_data = apply_uniform_filter(sample_data, size=3)
    print("Filtered Data:\n", filtered_data)
