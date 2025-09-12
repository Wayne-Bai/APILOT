import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=None):
    # Ensure weights are normalized
    weights = weights / np.sum(weights, axis=axis, keepdims=True)
    
    # Compute the weighted geometric mean
    weighted_data = data * weights
    return gmean(weighted_data, axis=axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

result = weighted_geometric_mean(data, weights, axis=1)
print(result)
