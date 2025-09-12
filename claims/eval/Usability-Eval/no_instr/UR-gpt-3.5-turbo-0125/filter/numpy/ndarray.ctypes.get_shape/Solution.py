
import numpy as np
import ctypes

# Determine the ctypes base type corresponding to dtype('p')
if np.dtype('p').itemsize == 4:
    base_ctypes_type = ctypes.c_int
elif np.dtype('p').itemsize == 8:
    base_ctypes_type = ctypes.c_long
else:
    base_ctypes_type = ctypes.c_longlong

# Create a ctypes array of length self.ndim with base_ctypes_type
class ShapeArray(ctypes.Structure):
    _fields_ = [("values", base_ctypes_type * self.ndim)]
