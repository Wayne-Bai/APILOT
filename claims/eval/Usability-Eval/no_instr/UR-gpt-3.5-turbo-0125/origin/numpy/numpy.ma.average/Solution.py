
import numpy as np

def weighted_average(arr, weights, axis=None):
    return np.average(arr, weights=weights, axis=axis)

# Example of using the function
arr = np.array([[1, 2], [3, 4]])
weights = np.array([0.1, 0.9])
result = weighted_average(arr, weights, axis=0)
print(result)
