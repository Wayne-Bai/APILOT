
import numpy as np

# Create two numpy arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stack the arrays horizontally (column wise)
result = np.hstack((arr1, arr2))

print(result)
