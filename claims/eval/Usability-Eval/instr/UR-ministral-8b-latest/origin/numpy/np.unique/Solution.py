import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    sorted_unique_elements = np.sort(unique_elements)
    return sorted_unique_elements

# Example usage
arr = np.array([5, 2, 5, 1, 4, 2, 5, 3])
print(find_unique_elements(arr))  # Output: [1 2 3 4 5]
