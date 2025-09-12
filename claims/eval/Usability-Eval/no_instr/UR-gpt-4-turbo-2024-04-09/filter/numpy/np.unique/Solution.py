import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example usage:
arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_elems = find_unique_elements(arr)
print("Unique elements:", unique_elems)
