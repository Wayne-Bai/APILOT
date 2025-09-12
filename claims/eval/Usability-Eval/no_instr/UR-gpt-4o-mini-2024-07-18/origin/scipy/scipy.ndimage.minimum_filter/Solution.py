import scipy.ndimage as ndimage
import numpy as np

def multidimensional_minimum_filter(input_array, size):
    """
    Apply a multidimensional minimum filter to an input array.
    
    Parameters:
    input_array (np.ndarray): The input array to filter.
    size (int or tuple of int): The size of the filter. If an integer is provided,
                                 it will create a filter of that size in all dimensions.
    
    Returns:
    np.ndarray: The filtered array.
    """
    return ndimage.minimum_filter(input_array, size=size)

# Example usage
if __name__ == "__main__":
    # Create a sample input array
    arr = np.random.rand(5, 5, 5)
    filter_size = 3  # Define the filter size
    filtered_arr = multidimensional_minimum_filter(arr, filter_size)
    
    print("Original Array:\n", arr)
    print("\nFiltered Array:\n", filtered_arr)
