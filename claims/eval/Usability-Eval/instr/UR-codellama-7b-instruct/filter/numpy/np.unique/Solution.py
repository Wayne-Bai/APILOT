
import numpy as np

def find_unique(my_array):
    # Using the np.unique function with the axis parameter set to None returns the sorted unique elements of an array.
    unique_elements = np.unique(my_array, axis=None)
    
    # To also return the counts for each unique element, use the `return_counts` parameter.
    unique_elements, counts = np.unique(my_array, axis=None, return_counts=True)
    
    # To also return the indices of the original array where each unique element was found, use the `return_index` parameter.
    unique_elements, indices = np.unique(my_array, axis=None, return_index=True)
    
    # To also return the sort order of the unique elements in the original array, use the `return_inverse` parameter.
    unique_elements, inverse = np.unique(my_array, axis=None, return_inverse=True)
    
    # You can also use the `sort` function to sort the unique elements in descending order.
    sorted_unique_elements = np.sort(unique_elements)[::-1]
    
    return unique_elements
