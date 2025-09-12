import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Get the pointer to the memory area of the array as a Python integer
pointer = arr.__array_interface__['data'][0]
print(pointer)
