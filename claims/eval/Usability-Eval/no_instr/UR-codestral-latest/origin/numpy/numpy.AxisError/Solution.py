import numpy as np

# Creating a 2D array for demonstration
data = np.array([[1, 2, 3], [4, 5, 6]])

# Let's specify an invalid axis
invalid_axis = 3

try:
    result = np.sum(data, axis=invalid_axis)
    print(result)
except np.AxisError:
    print("Invalid axis specified. The axis parameter must be less than the number of the array dimensions.")
