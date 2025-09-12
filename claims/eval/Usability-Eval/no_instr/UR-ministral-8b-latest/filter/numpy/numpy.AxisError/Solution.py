import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Try to reshape an array with an invalid axis
try:
    invalid_array = array.reshape((-1, 30))
except AxisError as e:
    print(f"Axis supplied was invalid: {e}")
