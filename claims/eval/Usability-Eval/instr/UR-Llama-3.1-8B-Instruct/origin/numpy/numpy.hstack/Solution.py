import numpy as np

# Define the arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Stack arrays in sequence horizontally (column wise)
stacked_array = np.hstack((array1, array2))

print(stacked_array)
