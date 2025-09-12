import scipy.stats as stats
import numpy as np

def weighted_harmonic_mean(data, weights, axis=0):
    if len(data) != len(weights):
        raise ValueError("The length of data and weights must be the same.")
    
    # Calculate the weighted harmonic mean using scipy stats.hmean
    # Scale data by weights for harmonic calculation
    scaled_data = 1 / (data * weights)
    hmean = 1 / np.sum(scaled_data, axis=axis) / np.sum(weights, axis=axis)
    
    return hmean

# Example usage
data = np.array([[2, 3], [4, 8]])
weights = np.array([[0.3, 0.7], [0.6, 0.4]])

result = weighted_harmonic_mean(data, weights, axis=0)
print("Weighted Harmonic Mean:", result)
