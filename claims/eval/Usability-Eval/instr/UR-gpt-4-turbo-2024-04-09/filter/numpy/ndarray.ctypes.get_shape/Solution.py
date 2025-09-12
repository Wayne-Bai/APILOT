import numpy as np
import ctypes

# Determine the appropriate ctypes integer type corresponding to numpy's intp
if np.dtype(np.intp) == np.dtype(np.int32):
    c_intp = ctypes.c_int
elif np.dtype(np.intp) == np.dtype(np.int64):
    c_intp = ctypes.c_longlong
else:
    c_intp = ctypes.c_long  # Defaulting to c_long if the platform specifics are unusual

# Define the ndim (number of dimensions)
ndim = 3  # Example dimensionality

# Example shape of the ndarray
shape = (10, 5, 2)

# Create a ctypes array of c_intp of length ndim containing the shape
ctypes_array = (c_intp * ndim)(*shape)

# The ctypes array now contains the dimensions of the ndarray
print(ctypes_array[:])  # Output to verify contents
