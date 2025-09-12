import numpy as np

def unique_sorted_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example usage
array = np.array([1, 2, 3, 2, 1, 4, 5])
result = unique_sorted_elements(array)
print(result)
