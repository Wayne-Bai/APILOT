from scipy.stats import gmean
import numpy as np

# Sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Weights
weights = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])

# Compute weighted geometric mean along the specified axis
weighted_geometric_mean = gmean(data, axis=1, weights=weights)

print(weighted_geometric_mean)
