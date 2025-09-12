
import numpy as np

# Perform some operations with numpy arrays
# For example:
arr = np.array([[1, 2, 3], [4, 5, 6]])

try:
    result = np.sum(arr, axis=2)
except np.AxisError as e:
    print("Axis supplied was invalid:", e)
