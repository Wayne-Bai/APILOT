import numpy as np

# Example arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Stacking arrays horizontally
result = np.hstack((array1, array2))

print(result)
