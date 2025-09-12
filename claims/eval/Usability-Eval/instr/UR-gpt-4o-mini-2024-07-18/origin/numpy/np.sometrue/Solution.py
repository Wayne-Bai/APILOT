import numpy as np

# Create a sample array
array = np.array([[False, False, True],
                  [False, False, False],
                  [True, False, False]])

# Test whether any array element along a given axis evaluates to True
result_axis_0 = np.any(array, axis=0)
result_axis_1 = np.any(array, axis=1)

# Print the results
print("Any element along axis 0:", result_axis_0)
print("Any element along axis 1:", result_axis_1)
