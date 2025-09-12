import numpy as np

# Creating two 2D arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

array2 = np.array([[10, 11, 12],
                   [13, 14, 15],
                   [16, 17, 18]])

# Stacking arrays horizontally (column wise)
stacked_array = np.hstack((array1, array2))

print(stacked_array)
