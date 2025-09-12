import numpy as np

def indices_of_max_values(arr, axis=None):
    return np.argmax(arr, axis=axis)

# Example usage:
array = np.array([[1, 2, 3], [4, 3, 2]])
max_indices = indices_of_max_values(array, axis=1)
print(max_indices)
