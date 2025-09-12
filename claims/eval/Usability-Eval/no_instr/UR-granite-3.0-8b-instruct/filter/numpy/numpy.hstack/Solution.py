import numpy as np

# Assuming you have two 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Stack arrays in sequence horizontally (column wise)
result = np.hstack((array1, array2))

print(result)
