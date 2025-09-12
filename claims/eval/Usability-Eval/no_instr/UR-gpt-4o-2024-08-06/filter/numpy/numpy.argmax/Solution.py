import numpy as np

# Example array
array = np.array([[10, 12, 5], 
                  [15, 8, 9], 
                  [23, 1, 3]])

# Get the indices of maximum values along the specified axis
# axis=0 means maximum values in each column
max_indices_columns = np.argmax(array, axis=0)

# axis=1 means maximum values in each row
max_indices_rows = np.argmax(array, axis=1)

print("Indices of maximum values along columns:", max_indices_columns)
print("Indices of maximum values along rows:", max_indices_rows)
