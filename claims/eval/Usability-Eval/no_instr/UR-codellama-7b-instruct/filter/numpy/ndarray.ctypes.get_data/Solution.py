
import numpy as np

# create an example array with unaligned data
arr = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
ptr = arr.ctypes.data_as(ctypes.c_void_p)
print(f"Pointer to array: {ptr}")
