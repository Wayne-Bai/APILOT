
import numpy as np

def weighted_harmonic_mean(data, weights, axis=None):
    if axis is None:
        axis = 0
    weighted_sum = np.sum(weights, axis=axis)
    weights = np.expand_dims(weights, axis=axis)
    weighted_values_sum = np.sum(data / weights, axis=axis)
    return weighted_sum / weighted_values_sum

# Test the function
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.1, 0.2, 0.3])
result = weighted_harmonic_mean(data, weights, axis=1)
print(result)
