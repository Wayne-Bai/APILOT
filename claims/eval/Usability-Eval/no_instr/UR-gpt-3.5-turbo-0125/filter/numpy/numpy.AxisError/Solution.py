
import numpy as np

# Example array
arr = np.array([[1, 2, 3], [4, 5, 6]])

try:
    # Specify an invalid axis
    result = np.sum(arr, axis=2)
except np.AxisError as e:
    print("Axis supplied was invalid:", e)
