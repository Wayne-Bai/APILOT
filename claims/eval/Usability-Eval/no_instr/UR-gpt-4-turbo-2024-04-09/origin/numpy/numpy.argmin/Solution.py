import numpy as np

def indices_of_min_values(arr, axis):
    return np.argmin(arr, axis=axis)

# Example usage:
array = np.array([[2, 3, 1], [6, 5, 4]])
min_indices = indices_of_min_values(array, axis=1)
print("Indices of minimum values:", min_indices)
