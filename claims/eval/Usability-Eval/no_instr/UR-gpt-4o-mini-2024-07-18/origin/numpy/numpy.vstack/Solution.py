import numpy as np

# Example arrays to stack
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stacking arrays vertically
stacked_array = np.vstack((array1, array2))

print(stacked_array)
