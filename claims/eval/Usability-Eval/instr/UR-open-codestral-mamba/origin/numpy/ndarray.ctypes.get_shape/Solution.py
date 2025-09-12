import numpy as np
import ctypes

# Get the appropriate c_intp based on the platform
if np.dtype('p').itemsize == 4:
    c_intp = ctypes.c_int
elif np.dtype('p').itemsize == 8:
    c_intp = ctypes.c_longlong
else:
    raise RuntimeError("Unable to determine appropriate c_intp type on this platform")

# Create the ctypes array of length self.ndim
shape_array = (c_intp * self.ndim)()
