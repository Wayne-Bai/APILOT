import numpy as np

def join_arrays_along_axis(arrays, axis):
    """
    Join a sequence of arrays along a new axis.

    Parameters:
    arrays (list of np.ndarray): List of arrays to join.
    axis (int): The axis along which to join the arrays.

    Returns:
    np.ndarray: The joined array.
    """
    return np.concatenate(arrays, axis=axis)
