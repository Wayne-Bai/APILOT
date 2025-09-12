import numpy as np

# Sample array
arr = np.array([[0, 1, 0], [0, 0, 0]])

# Test if any element along a given axis evaluates to True
result_axis0 = np.any(arr, axis=0)
result_axis1 = np.any(arr, axis=1)

print("Any true along axis 0:", result_axis0)
print("Any true along axis 1:", result_axis1)
