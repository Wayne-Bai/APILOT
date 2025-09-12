import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=None):
    # Convert data and weights to numpy arrays
    data = np.array(data)
    weights = np.array(weights)
    
    # Ensure data and weights have the same shape
    if data.shape != weights.shape:
        raise ValueError("data and weights must be the same shape")
    
    # Apply weights
    weighted_data = data ** weights
    
    # Compute geometric mean of the weighted data using scipy's gmean function
    result = gmean(weighted_data, axis=axis)
    
    return result

# Example usage:
data = [[1, 2, 3], [4, 5, 6]]
weights = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
axis = 1

print(weighted_geometric_mean(data, weights, axis))
