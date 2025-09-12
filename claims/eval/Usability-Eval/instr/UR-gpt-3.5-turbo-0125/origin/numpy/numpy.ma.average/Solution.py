
import numpy as np

# Create an array
arr = np.array([[1, 2], [3, 4]])

# Define the custom weights
weights = np.array([0.25, 0.75])

# Calculate the weighted average along axis 1
weighted_avg = np.average(arr, axis=1, weights=weights)

print(weighted_avg)
