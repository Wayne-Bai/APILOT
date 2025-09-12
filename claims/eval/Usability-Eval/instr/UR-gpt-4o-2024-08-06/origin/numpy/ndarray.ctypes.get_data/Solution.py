import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Get the pointer to the memory area of the array
pointer_to_memory = arr.ctypes.data

# Output the memory pointer address
print(f"Memory address of the array: {pointer_to_memory}")
