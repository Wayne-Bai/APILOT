import numpy as np

# Assume arr is the input numpy array
arr = np.array([[1, 2], [3, 4]])

# Calculate the cumulative product of elements along a given axis
# Here we are calculating the cumulative product along axis=0 (downwards)
result = np.cumprod(arr, axis=0)

# Print the result
print(result)
