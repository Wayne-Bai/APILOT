
import numpy as np

# Define a sample array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Try to access an element using an invalid axis
try:
    arr[0, :, :]
except AxisError as e:
    print(e)
