import numpy as np

# Create a sample numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define a condition
condition = lambda x: x > 5

# Use numpy's apply_along_axis function to apply the condition along axis=1 (columns)
result = np.apply_along_axis(condition, 1, arr)

# Print the result
print(result)
