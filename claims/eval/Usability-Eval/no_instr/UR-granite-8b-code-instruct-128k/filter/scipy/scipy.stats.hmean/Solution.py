
import numpy as np
from scipy.stats import rankdata

def calculate_weighted_harmonic_mean(data, weights, axis=None):
    ranks = rankdata(data, method='min')
    return np.average(weights / data, axis=axis, weights=ranks)

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
weights = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
weighted_harmonic_mean = calculate_weighted_harmonic_mean(data, weights)
print(weighted_harmonic_mean)
