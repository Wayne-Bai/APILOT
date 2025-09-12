import numpy as np

def find_unique_elements(array):
    unique_elements = np.unique(array)
    return unique_elements

# Example usage:
array = np.array([1, 2, 2, 3, 4, 4, 5])
unique_sorted_elements = find_unique_elements(array)
print(unique_sorted_elements)
