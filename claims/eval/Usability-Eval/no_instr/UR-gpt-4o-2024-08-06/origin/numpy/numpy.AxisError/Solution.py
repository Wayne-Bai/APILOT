import numpy as np

# Attempt to access an invalid axis in a numpy array
try:
    array = np.array([[1, 2, 3], [4, 5, 6]])
    # Here trying to sum over axis 2, which does not exist in a 2D array
    result = np.sum(array, axis=2)
except np.AxisError as e:
    print(f"AxisError: {e}")
