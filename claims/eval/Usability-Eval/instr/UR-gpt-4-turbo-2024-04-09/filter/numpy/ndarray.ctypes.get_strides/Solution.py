import numpy as np
import ctypes

# Create an example numpy array
array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# Get the strides of the array (bytes to jump to the next element in each dimension)
strides = array.strides

# Create a ctypes array of type c_intp (pointer-sized integer) with the same length as array.ndim
c_strides = (ctypes.c_intp * array.ndim)(*strides)

# Printing ctypes array with strides information
print(c_strides)
