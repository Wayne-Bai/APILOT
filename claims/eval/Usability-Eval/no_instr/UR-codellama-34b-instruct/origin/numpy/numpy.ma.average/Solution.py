
import numpy as np

def weighted_average(array, weights, axis=None):
    """
    Calculate the weighted average of an array over a given axis.

    Parameters:
    ----------
        array : numpy.ndarray
            The input array to calculate the weighted average for.
        weights : numpy.ndarray
            The weights for each element in the array. Must be the same shape as `array`.
        axis : int, optional
            The axis over which to calculate the weighted average. If None, the average is calculated over the entire array. Default is None.

    Returns:
    -------
        numpy.ndarray
            The weighted average of the input array along the given axis.
    """
    # Check that `weights` and `array` have the same shape
    if weights.shape != array.shape:
        raise ValueError("Weights and array must have the same shape.")

    # Calculate the weighted sum along the given axis
    weighted_sum = np.einsum("i,ij->j", weights, array)

    # Normalize by the sum of the weights
    norm = np.sum(weights, axis=axis)
    return weighted_sum / norm
