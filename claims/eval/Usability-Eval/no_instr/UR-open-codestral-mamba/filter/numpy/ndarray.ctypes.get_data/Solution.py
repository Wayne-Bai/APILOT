import numpy as np

# create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# get the memory address
ptr = np.ctypeslib.as_ctypes(arr)

# Convert the memory address to a Python integer
int_ptr = int.from_bytes(ptr, byteorder=sys.byteorder)

print("Memory address:", int_ptr)
