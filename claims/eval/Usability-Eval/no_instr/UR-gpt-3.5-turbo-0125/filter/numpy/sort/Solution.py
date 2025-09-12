import numpy as np

def sort_array(arr):
    sorted_arr = np.array(arr)
    sorted_arr.sort()
    return sorted_arr

# Example of how to use the function
arr = [3, 1, 2]
sorted_arr = sort_array(arr)
print(sorted_arr)
