import numpy as np

# Create a random 2D array
arr = np.random.rand(3, 3)

# Try to access a non-existing axis
try:
    result = arr[0, 3, :]
except IndexError as e:
    print("Axis supplied was invalid: ", str(e))
