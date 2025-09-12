import numpy as np

def find_unique_elements(array):
    unique_elements = np.unique(array)
    return np.sort(unique_elements)

# Example usage
my_array = np.array([1, 2, 3, 1, 2, 3, 4, 5, 5, 6, 7, 7])
result = find_unique_elements(my_array)
print(result)
