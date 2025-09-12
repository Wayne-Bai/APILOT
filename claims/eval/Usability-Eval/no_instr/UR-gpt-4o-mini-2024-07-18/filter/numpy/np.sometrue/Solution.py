import numpy as np

# Create a sample array
arr = np.array([[False, True, False],
                [False, False, False],
                [True, False, True]])

# Test if any element along a specific axis evaluates to True
result_axis0 = np.any(arr, axis=0)  # Check along columns
result_axis1 = np.any(arr, axis=1)  # Check along rows

print("Any True along axis 0:", result_axis0)
print("Any True along axis 1:", result_axis1)
