import numpy as np

def find_unique_elements(array):
    # Convert the input array to a numpy array
    np_array = np.array(array)
    
    # Use np.unique to find unique elements
    unique_elements, indices, inverse_indices, counts = np.unique(np_array, 
                                                                  return_index=True, 
                                                                  return_inverse=True, 
                                                                  return_counts=True)
    return unique_elements, indices, inverse_indices, counts

# Example usage:
array = [1, 2, 3, 4, 5, 3, 2, 1, 5, 6]
unique_elements, indices, inverse_indices, counts = find_unique_elements(array)
print("Unique elements:", unique_elements)
print("Indices of first occurrence in original array:", indices)
print("Indices to reconstruct original array:", inverse_indices)
print("Counts of each unique element:", counts)
