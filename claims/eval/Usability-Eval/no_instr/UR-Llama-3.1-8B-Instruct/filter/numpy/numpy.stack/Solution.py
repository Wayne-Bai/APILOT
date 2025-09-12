import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Create a new axis to join the arrays along it
axis = 0

# Use np.newaxis to add a new axis to each array
new_arr1 = arr1[:, np.newaxis]
new_arr2 = arr2[:, np.newaxis]

# Join the arrays along the new axis
joined_arr = np.concatenate((new_arr1, new_arr2), axis=axis)

print(joined_arr)
