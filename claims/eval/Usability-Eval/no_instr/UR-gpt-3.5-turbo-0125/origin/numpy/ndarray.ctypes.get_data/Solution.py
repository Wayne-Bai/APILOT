
import numpy as np

# Initialize a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Get a pointer to the memory area of the numpy array in the form of a Python integer
memory_area_pointer = arr.__array_interface__['data'][0]

print(memory_area_pointer)
