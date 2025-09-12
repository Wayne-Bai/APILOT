import numpy as np

# Define a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Define the weights
weights = np.array([0.3, 0.7])

# Define the axis
axis = 0  # 0 for rows, 1 for columns

# Calculate the weighted average along the axis
weighted_average = np.average(array, axis=axis, weights=weights)

print(weighted_average)
