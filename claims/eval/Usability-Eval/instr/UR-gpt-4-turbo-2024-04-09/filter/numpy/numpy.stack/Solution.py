import numpy as np

# Define a sequence of arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Join these arrays along a new axis
result = np.stack((array1, array2, array3), axis=0)

print(result)
