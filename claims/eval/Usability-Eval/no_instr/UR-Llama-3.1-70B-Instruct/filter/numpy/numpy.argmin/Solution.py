import numpy as np

# Define a 2D array
arr = np.array([[12, 45, 7, 23], [56, 67, 87, 98], [34, 54, 78, 34]])

# Apply the function to find the indices of the minimum values along the axis
# (0 for column, 1 for row)
column_index_min_values = np.argmin(arr, axis=0)
row_index_min_values = np.argmin(arr, axis=1)

print("Indices of minimum values along columns: ", column_index_min_values)
print("Indices of minimum values along rows: ", row_index_min_values)

# Explanation:
# argmin() function returns indices of the minimum values along the given axis.
# axis=0 for column, axis=1 for row
