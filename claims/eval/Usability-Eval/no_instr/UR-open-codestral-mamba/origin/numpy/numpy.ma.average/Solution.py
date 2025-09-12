import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Give respective weights for array elements
weights = np.array([1, 2, 3, 4, 5])

# Use numpy's average function to get weighted average
# 'aweights' are the array containing the weights for elements
# 'axis' is the axis along which to calculate weighted average
weighted_avg = np.average(arr, weights=weights, axis=None)

print(f'The weighted average of array is: {weighted_avg}')
