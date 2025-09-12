import numpy as np

# Example array
arr = np.array([[0, 1, 2], [0, 0, 0], [3, 0, 0]])

# Test whether any array element along a given axis evaluates to True
result_along_axis_0 = np.any(arr, axis=0)
result_along_axis_1 = np.any(arr, axis=1)

print("Any element true along axis 0:", result_along_axis_0)
print("Any element true along axis 1:", result_along_axis_1)
