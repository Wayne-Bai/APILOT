import numpy as np

# Assuming 'arr' is your numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# To find the indices of the minimum values along the axis 0
min_indices_axis0 = np.argmin(arr, axis=0)
print("Indices of minimum values along axis 0:", min_indices_axis0)

# To find the indices of the minimum values along the axis 1
min_indices_axis1 = np.argmin(arr, axis=1)
print("Indices of minimum values along axis 1:", min_indices_axis1)
