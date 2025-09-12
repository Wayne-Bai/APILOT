import numpy as np

def find_min_indices(arr, axis):
    """
    Returns the indices of the minimum values along an axis.

    Parameters:
    arr (numpy.ndarray): The input array.
    axis (int): The axis along which to find the minimum indices.

    Returns:
    indices (numpy.ndarray): The indices of the minimum values along the specified axis.
    """
    if axis < 0:
        axis += arr.ndim
    if axis >= arr.ndim or axis < 0:
        raise np.AxisError(axis, arr.ndim)

    # Use np.argmin replacement with np.unravel_index
    indices = np.unravel_index(np.minimum.reduceat(arr, np.arange(0, arr.size, arr.shape[axis-1])).argmin(), arr.shape)[axis-1]
    return indices

# Example usage:
arr = np.array([[12, 6, 7], [4, 10, 9], [8, 13, 11]])
axis = 0  # Find minimum along rows (axis=0) or columns (axis=1)

min_indices = find_min_indices(arr, axis)
print(min_indices)
