
import numpy as np

# Create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the product of array elements over axis 1
result = np.prod(arr, axis=1)

print(result)
