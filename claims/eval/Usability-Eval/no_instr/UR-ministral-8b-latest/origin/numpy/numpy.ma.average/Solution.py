import numpy as np

def weighted_average(array, weights=None, axis=None):
    if weights is None:
        weights = np.ones_like(array, dtype=float) / array.shape[axis]

    weighted_array = np.multiply(array, weights)
    sum_weights = np.sum(weights, axis=axis)
    return np.sum(weighted_array, axis=axis) / sum_weights

# Example usage:
array = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.2, 0.3, 0.5])
result = weighted_average(array, weights, axis=1)
print(result)
