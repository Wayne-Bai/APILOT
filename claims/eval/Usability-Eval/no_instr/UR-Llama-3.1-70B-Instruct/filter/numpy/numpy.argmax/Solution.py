import numpy as np

# Create a 2D numpy array
arr = np.array([[4, 7, 2], [1, 3, 9], [6, 5, 8]])

# Get the indices of the maximum values along the specified axis
# 0 for rows, 1 for columns
max_indices_along_rows = np.argmax(arr, axis=0)
max_indices_along_cols = np.argmax(arr, axis=1)

print("Original array:")
print(arr)
print("\nMaximum values along rows at indices:", max_indices_along_rows)
print("Maximum values along columns at indices:", max_indices_along_cols)
