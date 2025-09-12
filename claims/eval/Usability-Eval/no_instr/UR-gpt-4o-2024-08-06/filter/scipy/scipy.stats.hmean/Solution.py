import numpy as np
from scipy import stats

def weighted_harmonic_mean(data, weights, axis=0):
    """
    Calculate the weighted harmonic mean along the specified axis.

    :param data: ndarray
        Data for which the weighted harmonic mean is to be calculated.
    :param weights: ndarray
        Weights for the data elements.
    :param axis: int, optional
        Axis along which to compute the harmonic mean. Default is 0.
    :return: Weighted harmonic mean
    """
    data = np.asarray(data)
    weights = np.asarray(weights)
    
    if data.shape != weights.shape:
        raise ValueError("Data and weights must be the same shape")
    
    # Use the formula for weighted harmonic mean
    weighted_harm_mean = np.sum(weights, axis=axis) / np.sum(weights / data, axis=axis)
    
    return weighted_harm_mean

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.5, 0.2, 0.3], [0.8, 0.1, 0.1]])
axis = 0

whm = weighted_harmonic_mean(data, weights, axis=axis)
print("Weighted Harmonic Mean:", whm)
