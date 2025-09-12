import scipy as sp
import numpy as np

def weighted_harmonic_mean(data, weights, axis=0):
    """
    Calculate the weighted harmonic mean of a dataset.

    Parameters:
    data (numpy array): input data.
    weights (numpy array): weights of the data points.
    axis (int): axis along which to calculate the mean.

    Returns:
    weighted harmonic mean (numpy array).
    """
    data = np.asarray(data)
    weights = np.asarray(weights)

    if data.shape!= weights.shape:
        raise ValueError("Data and weights must have the same shape")

    # Check for zero weights or data points
    zero_weights = weights == 0
    zero_data = data == 0

    if np.any(zero_weights & zero_data):
        raise ValueError("Data point with zero weight has zero value")

    if np.any(zero_weights):
        raise ValueError("Zero weights not allowed")

    if np.any(zero_data):
        # replace 0 with a very small value, to avoid division by zero
        data[zero_data] = np.finfo(data.dtype).eps

    weighted_sum = np.sum(weights / data, axis=axis)
    sum_of_weights = np.sum(weights, axis=axis)

    return sum_of_weights / weighted_sum

# Example usage
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
weights = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])

print(weighted_harmonic_mean(data, weights, axis=0))
print(weighted_harmonic_mean(data, weights, axis=1))
