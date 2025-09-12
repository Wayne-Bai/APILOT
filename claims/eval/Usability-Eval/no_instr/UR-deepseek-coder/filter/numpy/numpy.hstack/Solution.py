import numpy as np

# Example arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Stack arrays horizontally (column-wise)
result = np.column_stack((array1, array2))

print(result)
