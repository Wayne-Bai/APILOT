import numpy as np
from scipy.stats import hmean

def weighted_harmonic_mean(data, weights, axis=None):
    # Ensure weights are non-negative
    if np.any(weights < 0):
        raise ValueError("Weights must be non-negative.")
    
    # Ensure data is non-negative
    if np.any(data <= 0):
        raise ValueError("Data must be strictly positive.")
    
    # Calculate the weighted harmonic mean
    weighted_data = weights / data
    sum_weights = np.sum(weights, axis=axis, keepdims=True)
    sum_weighted_data = np.sum(weighted_data, axis=axis, keepdims=True)
    
    return sum_weights / sum_weighted_data

# Example usage:
data = np.array([[1, 2, 4], [1, 3, 9]])
weights = np.array([[1, 2, 3], [1, 2, 3]])

# Calculate weighted harmonic mean along axis 1
result = weighted_harmonic_mean(data, weights, axis=1)
print(result)
