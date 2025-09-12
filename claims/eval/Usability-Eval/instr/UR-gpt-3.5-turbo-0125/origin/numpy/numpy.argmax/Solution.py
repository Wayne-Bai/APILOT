
import numpy as np

# Create a sample 2D array
arr = np.array([[1, 3, 2],
                [4, 2, 6],
                [0, 1, 5]])

# Find the indices of maximum values along axis 0
max_indices_axis0 = np.argmax(arr, axis=0)

# Find the indices of maximum values along axis 1
max_indices_axis1 = np.argmax(arr, axis=1)

print("Indices of maximum values along axis 0: ", max_indices_axis0)
print("Indices of maximum values along axis 1: ", max_indices_axis1)
