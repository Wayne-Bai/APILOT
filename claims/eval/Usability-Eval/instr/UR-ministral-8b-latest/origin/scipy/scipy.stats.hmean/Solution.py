import numpy as np
from scipy.stats import hmean

def weighted_harmonic_mean(data, weights, axis):
    # Calculate the weighted harmonic mean along the specified axis
    return hmean(data, axis=axis, weights=weights)

# Example usage:
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

weights = np.array([1, 2, 3])

axis = 0

result = weighted_harmonic_mean(data, weights, axis)
print("Weighted Harmonic Mean along axis:", result)
