import numpy as np

# User inputs
array = np.array([1, 2, 3, 4, 5])
weights = np.array([1, 2, 3, 4, 5])
axis = 0

# Calculate weighted average
weighted_average = np.average(array, weights=weights, axis=axis)

# Output the result
print("The weighted average of the array is:", weighted_average)