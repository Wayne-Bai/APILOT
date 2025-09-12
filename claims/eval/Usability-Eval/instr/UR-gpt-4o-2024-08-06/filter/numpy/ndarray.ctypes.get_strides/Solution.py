import numpy as np
import ctypes

# Create a sample numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# Get the number of dimensions of the array
ndim = arr.ndim

# Get the strides of the array
strides = arr.strides

# Create a ctypes array of type np.ctypeslib.c_intp with length equal to the number of dimensions
c_intp_array = (ctypes.c_long * ndim)(*strides)

# Output the ctypes array containing the strides information
print("Ctypes strides array:", list(c_intp_array))
