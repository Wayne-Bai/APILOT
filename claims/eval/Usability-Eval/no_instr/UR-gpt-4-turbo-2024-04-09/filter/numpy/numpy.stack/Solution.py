import numpy as np

# Sample arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Joining arrays along a new axis
result_array = np.stack((array1, array2, array3), axis=0)

print(result_array)
