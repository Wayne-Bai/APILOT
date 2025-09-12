
import numpy as np

# Creating a sample 2D array
arr = np.array([[3, 7, 5],
                [1, 6, 8],
                [9, 2, 4]])

# Finding the indices of the minimum values along the first axis (axis=0)
min_indices_axis0 = arr.argmin(axis=0)

print("Indices of minimum values along axis 0:", min_indices_axis0)

# Finding the indices of the minimum values along the second axis (axis=1)
min_indices_axis1 = arr.argmin(axis=1)

print("Indices of minimum values along axis 1:", min_indices_axis1)
