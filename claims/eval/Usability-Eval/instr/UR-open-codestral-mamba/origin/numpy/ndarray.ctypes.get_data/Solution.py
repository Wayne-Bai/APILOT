import numpy as np

# Create a numpy array with aligned memory
arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)

# Get the pointer to the memory area of the array
ptr = arr.ctypes.data

print("Pointer to the memory area of the array:", ptr)
