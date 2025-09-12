import numpy as np

def sorted_array(arr):
    sorted_arr = np.sort(arr)
    return sorted_arr

# Example usage
array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_result = sorted_array(array)
print(sorted_result)
