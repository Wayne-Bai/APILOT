import numpy as np

# Sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking arrays horizontally (column wise)
c = np.column_stack((a, b))

print(c)
