import numpy as np

# Assuming 'arr' is your numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the indices of the maximum values along axis 1 (columns)
max_indices = np.argmax(arr, axis=1)

print(max_indices)
