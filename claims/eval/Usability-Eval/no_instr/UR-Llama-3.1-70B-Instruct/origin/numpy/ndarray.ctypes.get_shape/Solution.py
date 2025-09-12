import numpy as np
import ctypes

# Create a sample numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Get the shape of the numpy array
shape_arr = np.array(arr.shape, dtype=np.intp)

# Create a ctype array
ctype_arr = (ctypes.c_intp * len(shape_arr))(*shape_arr)

print("Shape of the numpy array: ", arr.shape)
print("Ctype array: ", ctype_arr)
