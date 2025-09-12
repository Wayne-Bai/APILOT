import numpy as np

def find_min_indices(array, axis=None):
    if axis is None:
        min_indices = np.indices(array.shape)
        return min_indices

    if axis < 0:
        axis += array.ndim

    min_vals = np.min(array, axis=axis)
    min_indices = np.unravel_index(np.argmin(array, axis=axis), array.shape)

    return min_indices

# Example usage
array = np.array([[3, 1, 4], [5, 2, 6], [7, 8, 9]])
print(find_min_indices(array, axis=1))
print(find_min_indices(array, axis=-1))
