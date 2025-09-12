import numpy as np

# Initialize a simple 2x2 array (represented as a list)
array = np.array([[1, 2], [3, 4]])

# Horizontal stacking of arrays in sequence
stacked_array = np.column_stack((array, array))

print(stacked_array)
