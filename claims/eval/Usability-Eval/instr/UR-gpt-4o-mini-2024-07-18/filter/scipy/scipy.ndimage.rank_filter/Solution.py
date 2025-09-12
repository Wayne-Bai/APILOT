import numpy as np
from scipy.ndimage import generic_filter

def rank_filter(input_array, rank):
    """
    Apply a multidimensional rank filter to the input array.
    
    Parameters:
    input_array (ndarray): The input array to be filtered.
    rank (int): The rank of the value to return from the neighborhood.
    
    Returns:
    ndarray: The filtered array.
    """
    # Define a function to compute the rank filter
    def rank_func(input_patch):
        return np.partition(input_patch, rank)[rank]
    
    # Apply the filter using generic_filter
    filtered_array = generic_filter(input_array, rank_func, size=(3, 3, 3), mode='reflect')
    
    return filtered_array

# Example usage
if __name__ == "__main__":
    # Create a sample 3D array
    sample_array = np.random.rand(5, 5, 5)
    
    # Apply the rank filter with rank 1 (second smallest value)
    filtered_result = rank_filter(sample_array, rank=1)
    
    print("Original Array:\n", sample_array)
    print("Filtered Array:\n", filtered_result)
