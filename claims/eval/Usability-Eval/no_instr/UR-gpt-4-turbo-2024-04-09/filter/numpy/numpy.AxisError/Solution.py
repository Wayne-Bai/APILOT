import numpy as np

# Create a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

try:
    # Attempt to sum along an axis that does not exist in the array
    result = np.sum(array_2d, axis=2)
except np.AxisError as e:
    print(e)
