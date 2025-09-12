import numpy as np

def indices_of_min_values(arr, axis=None):
    return np.argmin(arr, axis=axis)

# Example usage:
array = np.array([[1, 2], [3, 0]])
min_indices = indices_of_min_values(array, axis=1)
print("Indices of minimum values along axis 1:", min_indices)
