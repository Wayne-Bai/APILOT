import numpy as np

# Assuming you have the following arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = np.array([[9, 10], [11, 12]])

# Join the arrays along a new axis (axis=0)
joined_array = np.vstack((array1, array2, array3))

print(joined_array)
