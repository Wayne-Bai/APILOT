import numpy as np

# Define the arrays to join
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Join the arrays along a new axis
result = np.concatenate((array1, array2), axis=0)

# Print the result
print(result)
