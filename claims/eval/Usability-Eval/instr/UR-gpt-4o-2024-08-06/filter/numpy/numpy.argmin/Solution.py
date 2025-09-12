import numpy as np

# Example array
array = np.array([[4, 2, 9], [7, 1, 3], [5, 6, 8]])

# Find the indices of the minimum values along axis 0 (columns)
min_indices_axis0 = np.argmin(array, axis=0)

# Find the indices of the minimum values along axis 1 (rows)
min_indices_axis1 = np.argmin(array, axis=1)

print("Indices of minimum values along axis 0:", min_indices_axis0)
print("Indices of minimum values along axis 1:", min_indices_axis1)
