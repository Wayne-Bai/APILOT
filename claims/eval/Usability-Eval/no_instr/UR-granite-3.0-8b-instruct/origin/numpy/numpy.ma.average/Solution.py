import numpy as np

def weighted_average(array, weights, axis=None):
    """
    Calculate the weighted average of an array over the given axis.

    Parameters:
    array (numpy.ndarray): The input array.
    weights (numpy.ndarray): The weights for each element in the array.
    axis (int, optional): The axis along which to compute the weighted average. Default is None.

    Returns:
    numpy.ndarray: The weighted average along the specified axis.
    """
    if array.shape != weights.shape:
        raise ValueError("The array and weights must have the same shape.")

    if axis is None:
        return np.average(array, weights=weights)
    else:
        return np.average(array, axis=axis, weights=weights)
