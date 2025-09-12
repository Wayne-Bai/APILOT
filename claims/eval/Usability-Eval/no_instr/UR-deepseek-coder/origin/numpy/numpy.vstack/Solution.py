import numpy as np

# Example arrays to stack vertically
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Stack arrays vertically (row-wise)
stacked_array = np.vstack((array1, array2, array3))

print(stacked_array)
