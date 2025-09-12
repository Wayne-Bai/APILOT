import numpy as np

# Define a sample array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the indices of the maximum values along each row (axis=0)
max_indices_along_rows = np.argmax(array, axis=0)

# Get the indices of the maximum values along each column (axis=1)
max_indices_along_cols = np.argmax(array, axis=1)

print("Indices of maximum values along each row:", max_indices_along_rows)
print("Indices of maximum values along each column:", max_indices_along_cols)
