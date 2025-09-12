import numpy as np

def weighted_average(array, weights, axis=None):
    weighted_sum = np.sum(array * weights, axis=axis)
    sum_of_weights = np.sum(weights, axis=axis)
    return weighted_sum / sum_of_weights

# Example usage:
array = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

result = weighted_average(array, weights, axis=1)
print(result)
