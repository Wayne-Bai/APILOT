import numpy as np

# Example array
arr = np.array([1, 2, 3])

# Trying to sum along an invalid axis
try:
    result = np.sum(arr, axis=1)
except np.AxisError as e:
    print("AxisError:", e)
