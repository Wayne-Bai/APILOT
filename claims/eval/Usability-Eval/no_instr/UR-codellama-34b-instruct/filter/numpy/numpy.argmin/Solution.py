import numpy as np

def get_min_indices(arr, axis=None):
    """
    Returns the indices of the minimum values along an axis.

    Parameters:
        arr (array-like): Input array or object that can be converted to an array.
        axis (int): Axis along which to operate. Default is None.

    Returns:
        min_indices (numpy.ndarray): Indices of the minimum values along the specified axis.

    Example:
        >>> import numpy as np
        >>> arr = np.random.rand(5, 3)
        >>> get_min_indices(arr, axis=0)
        array([[1, 2], [0, 2], [0, 0]])
    """
    if axis is None:
        min_val = np.min(arr)
        return np.where(arr == min_val)[0]
    else:
        min_vals = np.amin(arr, axis=axis)
        return np.argwhere(arr == min_vals).flatten()
