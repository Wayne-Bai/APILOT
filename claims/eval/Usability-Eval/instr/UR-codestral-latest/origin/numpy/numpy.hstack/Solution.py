# Import the numpy library
import numpy as np

# Define two example arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Use the numpy's hstack function to stack arrays in sequence horizontally (column wise)
stacked_array = np.hstack((array1, array2))

# Print the stacked array
print(stacked_array)
