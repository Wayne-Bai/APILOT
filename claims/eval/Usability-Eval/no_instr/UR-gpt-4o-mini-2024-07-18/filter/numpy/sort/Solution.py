import numpy as np

def sorted_copy(array):
    return np.sort(array)

# Example usage
arr = np.array([5, 2, 9, 1, 5, 6])
sorted_arr = sorted_copy(arr)
print(sorted_arr)
