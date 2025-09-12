
import numpy as np

# Create sample arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Join the arrays along a new axis
result = np.stack((array1, array2))

print(result)
