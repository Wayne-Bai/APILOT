import numpy as np

def find_min_indices(arr, axis=None):
    if axis is None:
        axis = 0
    min_indices = np.unravel_index(np.argmin(arr, axis=axis), arr.shape)
    return min_indices

# Example usage
arr = np.array([[3, 1, 2], [4, 2, 1]])
print(find_min_indices(arr))  # Assuming default axis 0
print(find_min_indices(arr, axis=1))  # Specifying axis 1

arr2D = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

print(find_min_indices(arr2D, axis=1))  # Columns
print(find_min_indices(arr2D, axis=0))  # Rows
