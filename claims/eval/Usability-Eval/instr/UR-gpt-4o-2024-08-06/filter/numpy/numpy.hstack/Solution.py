import numpy as np

# Example arrays to be stacked
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stack arrays horizontally (column-wise)
stacked_arrays = np.concatenate((array1, array2), axis=1)

print(stacked_arrays)
