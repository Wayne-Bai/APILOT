# Import the numpy library
import numpy as np

# Define three 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Join the arrays along a new axis
joined_arrays = np.column_stack((array1, array2, array3))

print(joined_arrays)
