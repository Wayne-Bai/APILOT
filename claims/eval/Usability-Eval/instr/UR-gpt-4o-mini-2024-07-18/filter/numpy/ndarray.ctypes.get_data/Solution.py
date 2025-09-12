import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Get a pointer to the memory area of the array as a Python integer
memory_pointer = array.__array_interface__['data'][0]

print(f"Memory pointer of the array: {memory_pointer}")
