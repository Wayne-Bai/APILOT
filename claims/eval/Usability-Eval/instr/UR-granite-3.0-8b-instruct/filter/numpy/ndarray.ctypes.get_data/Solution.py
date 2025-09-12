import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Get the memory address of the array
memory_address = arr.__array_interface__['data'][0]

print(memory_address)
