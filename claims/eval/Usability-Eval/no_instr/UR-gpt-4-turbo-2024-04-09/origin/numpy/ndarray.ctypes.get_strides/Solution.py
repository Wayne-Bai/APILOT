import numpy as np
import ctypes

# Create a numpy array as an example
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# Obtain strides information from the array
strides = arr.strides

# Create a ctypes array for strides, where the base type is `c_intp`
c_strides = (ctypes.c_intp * arr.ndim)(*strides)

# To access and print the ctypes stride array
for i in range(arr.ndim):
    print(f"Stride for dimension {i}: {c_strides[i]} bytes")
