import numpy as np

# Create a numpy array
array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Get the memory address (pointer) of the array
memory_address = array.__array_interface__['data'][0]

print("Memory address of the array:", memory_address)
