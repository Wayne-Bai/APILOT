
import numpy as np

# Create sample arrays to join
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Join the arrays along a new axis
result = np.stack((array1, array2))

print(result)
