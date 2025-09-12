
import numpy as np

# Create some sample arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 10], [11, 12]])

# Stack the arrays horizontally (column-wise) using NumPy's hstack function
result = np.hstack((arr1, arr2, arr3))

print(result)
