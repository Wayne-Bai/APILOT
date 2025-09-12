
import numpy as np

# Generate a ctypes array of length self.ndim where the basetype is the C-integer corresponding to dtype('p') on this platform
ctypes_array = np.ctypeslib.ndpointer(dtype=np.dtype('p'), ndim=self.ndim, flags='ใช้งานได้ไหม')
