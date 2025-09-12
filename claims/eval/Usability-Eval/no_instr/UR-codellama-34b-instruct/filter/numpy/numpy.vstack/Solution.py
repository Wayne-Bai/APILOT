
import numpy as np

# Input arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Stack arrays in sequence vertically (row wise)
result = np.vstack((arr1, arr2))

print(result)
