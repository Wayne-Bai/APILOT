
import numpy as np

# Create a sample array
arr = np.array([[1, 2], [3, 4]])

# Compute the product of array elements over a given axis
result = np.prod(arr, axis=1)

print(result)
