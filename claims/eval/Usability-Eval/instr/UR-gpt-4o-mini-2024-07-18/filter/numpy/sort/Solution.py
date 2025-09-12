import numpy as np

def sorted_array(arr):
    return np.sort(arr)

# Example usage
array = np.array([5, 2, 9, 1, 5, 6])
sorted_copy = sorted_array(array)
print(sorted_copy)
