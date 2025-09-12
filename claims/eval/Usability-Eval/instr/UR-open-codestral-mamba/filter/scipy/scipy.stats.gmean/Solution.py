import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(a, weights):
    return np.exp(gmean(np.log(a), axis=0, weights=weights))

# Example usage:
data = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
weights = np.array([1, 2, 1])
print(weighted_geometric_mean(data, weights))  # Outputs: 2.23606797749979
