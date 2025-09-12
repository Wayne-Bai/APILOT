import numpy as np
from ctypes import c_int, c_long, c_longlong

def get_c_intp_array(shape):
    # Determine the base type based on the platform
    if sys.maxsize > 2**32:
        c_intp = c_longlong
    elif sys.maxsize > 2**16:
        c_intp = c_long
    else:
        c_intp = c_int

    # Create a ctypes array with the given shape
    c_intp_array = (c_intp * len(shape))(*shape)

    return c_intp_array
