import numpy as np

# Create a sample 2D numpy array
array = np.array([[True, True, False],
                  [True, True, True],
                  [False, True, True]])

# Test whether all elements along the columns (axis 0) evaluate to True
all_true_axis_0 = np.all(array, axis=0)

# Test whether all elements along the rows (axis 1) evaluate to True
all_true_axis_1 = np.all(array, axis=1)

print("All true along axis 0:", all_true_axis_0)
print("All true along axis 1:", all_true_axis_1)
