import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example Usage
arr = np.array([4, 9, 7, 9, 7, 8, 10, 8, 6, 9, 7])
unique_elements = find_unique_elements(arr)
print(unique_elements)
