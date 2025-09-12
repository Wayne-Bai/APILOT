import numpy as np

# Assuming we have a 2D np.array
arr = np.array([[1, 2, 3, 4],
                [5, 1, 2, 3],
                [6, 7, 1, 2],
                [8, 9, 10, 0]])

# Using np.argmin() to find indices of min values along axis=1
indices = np.argmin(arr, axis=1)

indices
