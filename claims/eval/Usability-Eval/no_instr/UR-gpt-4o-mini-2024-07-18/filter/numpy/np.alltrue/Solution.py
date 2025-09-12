import numpy as np

# Create a sample array
array = np.array([[True, False, True],
                  [True, True, True],
                  [False, True, True]])

# Test whether all elements along a specific axis evaluate to True
result_axis0 = np.all(array, axis=0)  # Checking along columns
result_axis1 = np.all(array, axis=1)  # Checking along rows

print("Result along axis 0:", result_axis0)
print("Result along axis 1:", result_axis1)
