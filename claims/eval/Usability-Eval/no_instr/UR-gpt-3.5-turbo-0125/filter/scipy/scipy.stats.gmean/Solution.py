
import numpy as np

def weighted_geometric_mean(data, weights, axis):
    return np.prod(data ** weights, axis=axis) ** (1 / np.sum(weights))

# Test the function with sample data
data = np.array([[2, 3, 4], [5, 6, 7]])
weights = np.array([0.25, 0.5, 0.25])
result = weighted_geometric_mean(data, weights, axis=1)
print(result)
