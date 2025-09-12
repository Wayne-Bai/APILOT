import numpy as np

# Assuming 'arr' is your numpy array
arr = np.array([1, 2, 3, 4, 5])

# Get the memory address of the array
memory_address = arr.__array_interface__['data'][0]

print(memory_address)
