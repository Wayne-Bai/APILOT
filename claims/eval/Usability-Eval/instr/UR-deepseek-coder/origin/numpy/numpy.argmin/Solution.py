import numpy as np

def argmin_axis(arr, axis=None):
    if axis is None:
        return np.unravel_index(np.argmin(arr, axis=None), arr.shape)
    else:
        return np.argmin(arr, axis=axis)

# Example usage:
# arr = np.array([[3, 2, 1], [6, 5, 4]])
# print(argmin_axis(arr, axis=1))  # Output: [2 2]
