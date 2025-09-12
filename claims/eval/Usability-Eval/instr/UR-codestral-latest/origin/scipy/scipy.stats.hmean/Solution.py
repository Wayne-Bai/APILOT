import numpy as np

def weighted_harmonic_mean(data, weights, axis=0):
    """
    Calculate the weighted harmonic mean along specified axis.

    Parameters:
    data : np.ndarray
        The input data.
    weights : np.ndarray
        The weights for each data point.
    axis : int, optional
        The axis along which to calculate the weighted harmonic mean. Default is 0.

    Returns:
    np.ndarray
        The weighted harmonic mean of the data.
    """
    # Check if weights are all positive
    if np.any(weights <= 0):
        raise ValueError("All weights must be positive.")

    # Calculate the weighted harmonic mean
    return (np.sum(weights / data, axis=axis) / np.sum(weights, axis=axis)) ** -1
