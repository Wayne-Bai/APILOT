import numpy as np

def sort_array(arr):
    sorted_arr = np.sort(arr)
    return sorted_arr

# Example usage:
original_arr = np.array([5, 2, 8, 1, 9])
sorted_arr = sort_array(original_arr)
print(sorted_arr)
