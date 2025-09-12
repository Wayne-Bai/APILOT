import numpy as np

# Create a sample NumPy array
array = np.array([1, 2, 3, 4], dtype=np.int32)

# Get a pointer to the memory area of the array as a Python integer
pointer_to_memory = array.__array_interface__['data'][0]

# Print the pointer value
print("Pointer to memory area:", pointer_to_memory)
