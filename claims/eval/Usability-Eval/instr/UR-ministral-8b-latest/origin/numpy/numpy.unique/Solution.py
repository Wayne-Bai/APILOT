import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example usage
arr = np.array([1, 2, 2, 3, 4, 4, 5])
print(find_unique_elements(arr))
