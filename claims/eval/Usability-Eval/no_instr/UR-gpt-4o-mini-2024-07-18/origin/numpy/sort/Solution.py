import numpy as np

def sorted_copy(arr):
    return np.sort(arr)

# Example usage
array = np.array([3, 1, 4, 1, 5, 9])
sorted_array = sorted_copy(array)
print(sorted_array)
