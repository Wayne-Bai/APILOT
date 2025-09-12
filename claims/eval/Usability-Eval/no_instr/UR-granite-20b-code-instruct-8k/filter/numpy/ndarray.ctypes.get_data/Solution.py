import numpy as np
a = np.array([1, 2, 3], dtype=np.int32)
b = a.ctypes.data
print(b)
