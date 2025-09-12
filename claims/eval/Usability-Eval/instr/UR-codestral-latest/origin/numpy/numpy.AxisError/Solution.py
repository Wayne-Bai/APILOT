import numpy as np

try:
    # Your numpy code that might raise AxisError
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    result = np.mean(arr, axis=2)
except IndexError as e:
    # Handle the error
    print("Axis supplied was invalid. Error message: ", str(e))
