import numpy as np
from scipy import stats

def weighted_harmonic_mean(data, weights, axis=None):
    """
    Calculate the weighted harmonic mean along the specified axis.
    
    Parameters:
    - data: array-like, input data
    - weights: array-like, weights for the harmonic mean
    - axis: int or None, axis along which the mean is computed. 
            If None, the mean is computed over the entire array.
    
    Returns:
    - Weighted harmonic mean along the specified axis.
    """
    if axis is None:
        data = np.ravel(data)
        weights = np.ravel(weights)
    else:
        data = np.moveaxis(data, axis, 0)
        weights = np.moveaxis(weights, axis, 0)

    weighted_values = weights / data
    weighted_harmonic_mean = np.sum(weights) / np.sum(weighted_values)
    
    return weighted_harmonic_mean

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[1, 1, 1], [1, 1, 1]])
result = weighted_harmonic_mean(data, weights, axis=0)
print(result)
