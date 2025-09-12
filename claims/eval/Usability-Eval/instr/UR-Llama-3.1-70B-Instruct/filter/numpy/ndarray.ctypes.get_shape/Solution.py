
import numpy as np
import ctypes

# Create a sample numpy array
arr = np.array([[1, 2], [3, 4]])

# Get the shape of the numpy array
shape = arr.shape

# Determine the base type (c_int, c_long, or c_longlong) based on the platform
base_type = ctypes.c_int
if np.intp(1).itemsize == 8:  # Check for 64-bit platform
    base_type = ctypes.c_longlong
elif np.intp(1).itemsize == 4:  # Check for 32-bit platform
    base_type = ctypes.c_long

# Create a ctypes array to hold the shape of the numpy array
arr_shape = (base_type * arr.ndim)(*shape)

print("Shape of the numpy array:", arr_shape)

for i in range(arr.ndim):
    print("arr_shape[{}] = {}".format(i, arr_shape[i]))
