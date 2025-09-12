import numpy as np

# Example array
arr = np.array([1, 2, 3, 4], dtype=np.int32)

# Get the pointer to the memory area of the array as a Python integer
memory_pointer = arr.ctypes.data

print(f"Memory pointer as Python integer: {memory_pointer}")
