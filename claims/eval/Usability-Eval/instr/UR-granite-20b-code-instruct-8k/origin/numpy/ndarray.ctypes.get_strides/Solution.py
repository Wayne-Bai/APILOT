import numpy as np

c_dtypes = np.dtype('int')
self.ndim = 10

c_strides = np.ctypeslib.as_ctypes(np.zeros(self.ndim, dtype=c_dtypes))
print(c_strides)
