import numpy as np

# Sample array
array = np.array([[True, True, False],
                  [True, True, True]])

# Testing if all elements along a given axis evaluate to True
result_axis0 = np.all(array, axis=0)  # Check along the rows
result_axis1 = np.all(array, axis=1)  # Check along the columns

print("Result along axis 0:", result_axis0)
print("Result along axis 1:", result_axis1)
