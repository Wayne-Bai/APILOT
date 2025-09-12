import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Attempt to access an invalid axis
try:
    print(arr[:, :3])
except np.AxisError as e:
    print(e)
