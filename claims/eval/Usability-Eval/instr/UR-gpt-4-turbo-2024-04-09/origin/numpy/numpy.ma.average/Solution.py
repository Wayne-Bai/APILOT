import numpy as np

def weighted_average(arr, weights, axis=None):
    return np.average(arr, weights=weights, axis=axis)

# Example usage:
arr = np.array([1, 2, 3, 4])
weights = np.array([0.1, 0.2, 0.3, 0.4])

print(weighted_average(arr, weights))
