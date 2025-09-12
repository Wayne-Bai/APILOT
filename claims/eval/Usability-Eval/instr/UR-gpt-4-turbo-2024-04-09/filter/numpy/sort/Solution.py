import numpy as np

def sorted_array(arr):
    return np.sort(arr)

# Example usage:
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_arr = sorted_array(arr)
print("Sorted Array:", sorted_arr)
