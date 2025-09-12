import numpy as np

# Here is a 5x5 numpy array for the demo
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]])

# Use numpy.argmin() to find the indices of the minimum values along an axis
min_indices = np.argmin(arr, axis=1)

print(min_indices)
