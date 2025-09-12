import numpy as np
from scipy import stats

def weighted_harmonic_mean(data, weights, axis=0):
    """
    Calculate the weighted harmonic mean along the specified axis.

    Parameters:
    - data: array-like, the data over which to calculate the harmonic mean.
    - weights: array-like, the weights for each element in the data.
    - axis: int, axis along which to calculate the harmonic mean.

    Returns:
    - Weighted harmonic mean along the specified axis.
    """
    data = np.array(data)
    weights = np.array(weights)
    
    if axis is None or axis >= data.ndim:
        raise ValueError("Invalid axis. Axis should be between 0 and data.ndim - 1.")

    weighted_reciprocal = weights / np.clip(data, np.finfo(float).eps, None)
    sum_weights = np.sum(weights, axis=axis)
    
    weighted_harmonic_mean_value = sum_weights / np.sum(weighted_reciprocal, axis=axis)
    
    return weighted_harmonic_mean_value

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
result = weighted_harmonic_mean(data, weights, axis=1)
print("Weighted Harmonic Mean:", result)
