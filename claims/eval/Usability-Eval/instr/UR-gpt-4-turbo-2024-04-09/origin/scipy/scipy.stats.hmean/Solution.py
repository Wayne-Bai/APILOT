import numpy as np
from scipy.stats import hmean

def weighted_harmonic_mean(values, weights, axis=None):
    if axis is not None and np.shape(values) != np.shape(weights):
        raise ValueError("values and weights must have the same shape when an axis is specified")
    # Compute element-wise multiplication of weights and values^-1
    weighted_values_inverse = weights / values
    # Sum over the specified axis
    sum_weighted_values_inverse = np.sum(weighted_values_inverse, axis=axis)
    sum_weights = np.sum(weights, axis=axis)
    # Compute the weighted harmonic mean
    return sum_weights / sum_weighted_values_inverse

# Example usage
values = np.array([[2, 3], [4, 6]])
weights = np.array([[1, 2], [2, 1]])

# Compute the weighted harmonic mean across the default axis
result = weighted_harmonic_mean(values, weights)
print("Weighted Harmonic Mean:", result)

# Compute the weighted harmonic mean along axis 0
result_axis_0 = weighted_harmonic_mean(values, weights, axis=0)
print("Weighted Harmonic Mean along axis 0:", result_axis_0)

# Compute the weighted harmonic mean along axis 1
result_axis_1 = weighted_harmonic_mean(values, weights, axis=1)
print("Weighted Harmonic Mean along axis 1:", result_axis_1)
