import numpy as np

# Creating sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking arrays in sequence vertically (row wise)
c = np.vstack((a, b))
print(c)
