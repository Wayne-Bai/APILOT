import numpy as np

# Example array
arr = np.array([[True, False], [True, True]])

# Test whether all elements along axis 0 (columns) evaluate to True
result_axis_0 = np.all(arr, axis=0)

# Test whether all elements along axis 1 (rows) evaluate to True
result_axis_1 = np.all(arr, axis=1)

print("Result along axis 0 (columns):", result_axis_0)
print("Result along axis 1 (rows):", result_axis_1)
