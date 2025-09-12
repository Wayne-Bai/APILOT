import numpy as np

def sorted_array(arr):
    return np.sort(arr)

# Example usage
original_array = np.array([3, 1, 4, 1, 5, 9])
sorted_copy = sorted_array(original_array)
print(sorted_copy)
