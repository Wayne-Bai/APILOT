import numpy as np

# Create a sample array
arr = np.array([[1, 2], [3, 4]])

# Calculate the product of all elements along an axis
result = arr.prod(axis=0)
print(result)
