import numpy as np

def unique_elements(array):
    unique_array = np.unique(array)  # Obtain unique elements
    sorted_unique_array = np.sort(unique_array)  # Sort the unique elements
    return sorted_unique_array

# Example usage
array = np.array([4, 2, 3, 2, 4, 1, 5, 3])
print(unique_elements(array))
