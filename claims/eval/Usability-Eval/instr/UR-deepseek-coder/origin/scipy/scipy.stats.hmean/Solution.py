import numpy as np
from scipy.stats import hmean

def weighted_harmonic_mean(data, weights, axis=None):
    # Ensure weights are positive
    if np.any(weights <= 0):
        raise ValueError("Weights must be positive.")
    
    # Calculate the weighted harmonic mean
    weighted_data = data * weights
    sum_weights = np.sum(weights, axis=axis, keepdims=True)
    sum_weighted_data = np.sum(weighted_data, axis=axis, keepdims=True)
    
    # Avoid division by zero
    if np.any(sum_weighted_data == 0):
        raise ValueError("Sum of weighted data is zero, cannot compute harmonic mean.")
    
    harmonic_mean = sum_weights / np.sum(weights / data, axis=axis, keepdims=True)
    
    return np.squeeze(harmonic_mean)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[1, 2, 3], [4, 5, 6]])

result = weighted_harmonic_mean(data, weights, axis=1)
print(result)
