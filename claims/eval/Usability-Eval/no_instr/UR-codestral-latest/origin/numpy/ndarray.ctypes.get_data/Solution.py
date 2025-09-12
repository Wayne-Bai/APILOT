import numpy as np

# Create a numpy array
a = np.array([1, 2, 3, 4, 5])

# Get the memory address of the numpy array
memory_address = a.ctypes.data

# Convert the memory address to a Python integer
memory_integer = int(memory_address)

print(memory_integer)
