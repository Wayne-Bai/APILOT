
import numpy as np

# Create a random 2D array
arr = np.random.rand(3, 4)

# Find the indices of the maximum values along axis 0
max_indices_axis0 = np.argmax(arr, axis=0)
print("Indices of maximum values along axis 0:", max_indices_axis0)

# Find the indices of the maximum values along axis 1
max_indices_axis1 = np.argmax(arr, axis=1)
print("Indices of maximum values along axis 1:", max_indices_axis1)
