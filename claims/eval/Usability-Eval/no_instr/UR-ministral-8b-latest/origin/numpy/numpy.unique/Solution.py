import numpy as np

def find_unique_elements(array):
    return np.unique(array)

# Example usage
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique_elements = find_unique_elements(array)
print(unique_elements)  # Output: [1 2 3 4 5]
