
import numpy as np

def weighted_harmonic_mean(data, weights, axis=0):
    # Calculate the weighted harmonic mean along the specified axis
    weights_sum = np.sum(weights, axis=axis)
    weighted_means = np.sum(weights/data, axis=axis)
    
    return weights_sum / weighted_means

# Example usage
data = np.array([[1, 2], [3, 4]])
weights = np.array([[1, 2], [3, 4]])
result = weighted_harmonic_mean(data, weights, axis=0)
print(result)
