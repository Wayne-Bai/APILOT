import numpy as np

# Create two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Use np.vstack() to stack arrays in sequence vertically (row wise)
stacked_arr = np.vstack((arr1, arr2))

print(stacked_arr)
