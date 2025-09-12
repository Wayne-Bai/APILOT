
import scipy

def weighted_harmonic_mean(data, weights, axis=None):
    """
    Calculate the weighted harmonic mean along the specified axis.

    Args:
        data (array_like): Input array.
        weights (array_like): Weights for each element in the data.
        axis (int, optional): Axis along which to compute the weighted harmonic mean. Default is None.

    Returns:
        harmonic_mean (float): Weighted harmonic mean of the input data along the specified axis.

    """
    return scipy.stats.hmean(data, weights=weights, axis=axis)
