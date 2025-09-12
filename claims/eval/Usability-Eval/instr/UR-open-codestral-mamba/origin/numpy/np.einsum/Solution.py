import numpy as np

# create two 3D arrays
array1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
array2 = np.array([[[2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2]]])

# use numpy's einstein summation convention to add the two arrays
result = np.einsum('ijk,ijk->ij', array1, array2)

print(result)
