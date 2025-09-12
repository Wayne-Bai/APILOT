
import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example
arr = np.array([1, 2, 3, 3, 4, 4, 5])
unique_arr = find_unique_elements(arr)
print(unique_arr)
