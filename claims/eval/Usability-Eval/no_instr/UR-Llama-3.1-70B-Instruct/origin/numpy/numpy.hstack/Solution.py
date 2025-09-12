import numpy as np

# Create two arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Use np.hstack() to stack arrays horizontally
stacked_array = np.hstack((array1, array2))

print(stacked_array)
