import numpy as np

def get_min_indices(arr, axis):
    return np.unravel_index(np.argmin(arr, axis=axis), arr.shape)

# Example usage:
arr = np.array([[3, 5, 2], [7, 1, 4]])
indices = get_min_indices(arr, axis=0)
print("Indices of min values along axis 0:", indices)

indices = get_min_indices(arr, axis=1)
print("Indices of min values along axis 1:", indices)
