import numpy as np

# Example array
arr = np.array([1, 2, 3, 4], dtype=np.int32)

# Get the memory address of the array as a Python integer
memory_address = arr.ctypes.data

print(f"Memory address of the array: {memory_address}")
