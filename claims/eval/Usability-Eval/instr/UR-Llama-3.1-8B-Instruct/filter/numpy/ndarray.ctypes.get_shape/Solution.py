import numpy as np
from ctypes import c_int
from ctypes import c_long
from ctypes import c_longlong

# Determine the base type based on the platform
if np.dtype('i').itemsize == 4:  # 32-bit platform
    c_intp = c_int
elif np.dtype('i').itemsize == 8:  # 64-bit platform
    c_intp = c_long
else:
    c_intp = c_longlong
