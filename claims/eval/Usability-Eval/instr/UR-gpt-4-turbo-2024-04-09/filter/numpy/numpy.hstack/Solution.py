import numpy as np

# Example arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking arrays horizontally (column wise)
result = np.column_stack((a, b))
print(result)
