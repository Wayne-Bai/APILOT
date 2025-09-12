import numpy as np

def sort_array(arr):
    return np.sort(arr)

# Example usage
array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_array = sort_array(array)
print(sorted_array)
