
import numpy as np

def sort_array(arr):
    """Return a sorted copy of the input array"""
    # Use the NumPy sorting function to sort the array
    return np.sort(arr)

# Test the function with an example array
arr = np.array([3, 1, 2, 4])
sorted_arr = sort_array(arr)
print(sorted_arr)  # [1, 2, 3, 4]
