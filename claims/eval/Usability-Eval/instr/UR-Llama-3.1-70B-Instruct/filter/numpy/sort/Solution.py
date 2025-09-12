import numpy as np

def sorted_array_copy(array):
    # Use np.sort with the'stable' kind to avoid deprecated warning
    return np.sort(array, kind='stable')

# Test the function
array = np.array([4, 2, 9, 6, 1, 7])
print("Original array: ", array)
print("Sorted array: ", sorted_array_copy(array))
