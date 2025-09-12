
import ctypes

# Determine the C integer type corresponding to dtype('p')
if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_int):
    c_intp_type = ctypes.c_int
elif ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_long):
    c_intp_type = ctypes.c_long
else:
    c_intp_type = ctypes.c_longlong

# Create a ctypes array of length self.ndim with the determined base type
class ShapeArray(ctypes.Structure):
    _fields_ = [("shape", c_intp_type * self.ndim)]

# Use ShapeArray to access the ctypes array containing the shape
