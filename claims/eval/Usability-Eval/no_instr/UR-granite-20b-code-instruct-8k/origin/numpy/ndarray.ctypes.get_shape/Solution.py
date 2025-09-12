import numpy as np

class YourClass:
    def __init__(self, ndim):
        self.ndim = ndim
        self.c_intp = self.get_c_integer_type()

    def get_c_integer_type(self):
        import ctypes
        if ctypes.sizeof(ctypes.c_voidp) == 4:
            return ctypes.c_int
        elif ctypes.sizeof(ctypes.c_voidp) == 8:
            return ctypes.c_longlong
        else:
            raise Exception("Unsupported platform")

    def generate_code(self):
        c_ddr_p = np.ctypeslib.as_ctypes(np.empty(self.ndim, dtype=np.dtype('p')))
        return c_ddr_p
