import numpy as np
import ctypes

# Define a numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Determine the correct ctypes integer type for the platform
c_intp_type = np.ctypeslib.ctypes.c_intp

# Create a ctypes array of the shape of the numpy array
ctypes_shape_array = (c_intp_type * array.ndim)(*array.shape)

# Output the result
print(ctypes_shape_array)
