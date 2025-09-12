import numpy as np
from scipy.stats.mstats import gmean

def weighted_geometric_mean(data, weights, axis=None):
    # Apply the weights by exponentiating the log of the data by the weights
    weighted_data = np.power(data, weights)
    # Compute the geometric mean of the weighted data
    return gmean(weighted_data, axis=axis)

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.5, 1.5])

# Compute the weighted geometric mean along axis 0
result = weighted_geometric_mean(data, weights, axis=0)
print("Weighted Geometric Mean along axis 0:", result)

# Compute the weighted geometric mean along axis 1
result = weighted_geometric_mean(data, weights, axis=1)
print("Weighted Geometric Mean along axis 1:", result)
