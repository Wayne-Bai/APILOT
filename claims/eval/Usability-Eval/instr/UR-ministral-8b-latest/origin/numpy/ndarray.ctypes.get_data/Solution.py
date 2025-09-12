import numpy as np

# Create an example array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Use numpy.ndarray.ctypes to generate the C pointer
ptr = arr.ctypes.data

# Display the C pointer
print(f"C Pointer: {ptr}")
