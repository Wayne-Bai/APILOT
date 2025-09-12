import numpy as np

def get_max_indices(arr, axis):
    """
    Returns the indices of the maximum values along an axis.

    Parameters:
    arr (numpy array): Input array
    axis (int): Axis along which to find the max values

    Returns:
    numpy array: Indices of the maximum values
    """
    max_values = np.argmax(arr, axis=axis)
    return max_values

# Example usage:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Get the indices of the max values along the first axis (rows)
idx = get_max_indices(arr, 0)
print("Indices of max values along first axis:", idx)

# Get the indices of the max values along the second axis (columns)
idx = get_max_indices(arr, 1)
print("Indices of max values along second axis:", idx)
