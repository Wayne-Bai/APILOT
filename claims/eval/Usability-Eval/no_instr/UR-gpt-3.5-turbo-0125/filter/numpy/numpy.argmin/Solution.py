
import numpy as np

# Creating a 2D numpy array
arr = np.array([[3, 6, 9],
                [5, 2, 7],
                [8, 1, 4]])

# Finding the indices of the minimum values along axis 0 (column-wise)
indices = np.argmin(arr, axis=0)

print("Indices of minimum values along axis 0:", indices)
