import numpy as np

# Create two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Stack arrays in sequence vertically (row wise)
stacked_array = np.concatenate((array1[:, np.newaxis], array2[:, np.newaxis], array3[:, np.newaxis]), axis=0)

print(stacked_array)
