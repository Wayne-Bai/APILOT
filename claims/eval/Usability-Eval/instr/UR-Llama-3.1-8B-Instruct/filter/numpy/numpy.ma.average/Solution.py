import numpy as np

# Sample array with dimensions 3x4
array_3x4 = np.arange(12).reshape(3, 4)

# Define the weights for each axis
weights_axis_0 = np.array([0.2, 0.3, 0.5])  # weights for axis 0 (rows)
weights_axis_1 = np.array([0.8, 0.1, 0.05, 0.05])  # weights for axis 1 (columns)

# Calculate the weighted sum along axis 0 (rows)
weighted_average_rows = np.average(array_3x4, weights=weights_axis_0, axis=0)

# Calculate the weighted sum along axis 1 (columns)
weighted_average_columns = np.average(array_3x4, weights=weights_axis_1, axis=1)

print("Weighted average along rows (axis 0): ", weighted_average_rows)
print("Weighted average along columns (axis 1): ", weighted_average_columns)

# Calculate the weighted average over the entire array
weighted_average = np.average(array_3x4, weights=weights_axis_0* weights_axis_1)

print("Weighted average over the entire array: ", weighted_average)
