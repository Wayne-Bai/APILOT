import numpy as np

# Create some example arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[9, 10], [11, 12]])

# Use the np.stack() function to join the arrays along a new axis
result = np.stack([a, b, c])

print(result)
