import numpy as np

# Example array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Check if all elements along an axis evaluate to True
result_axis0 = np.all(array, axis=0)
result_axis1 = np.all(array, axis=1)

print("Result along axis 0:", result_axis0)
print("Result along axis 1:", result_axis1)
