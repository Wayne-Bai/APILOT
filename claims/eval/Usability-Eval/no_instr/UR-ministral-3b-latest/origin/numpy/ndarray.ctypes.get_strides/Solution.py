import numpy as np
import ctypes

# Example usage
array_shape = np.array([2, 3], dtype=np.intc)
strides = np.array(array_shape, dtype=np.intc).ctypes.data_as(ctypes.POINTER(ctypes.c_int))

# Print strides for demonstration
for strd in strides :
    print(strd)
