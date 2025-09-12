
import numpy as np

def create_strides_array(self):
    # Create a ctypes array of length self.ndim where the basetype is the same as for the shape attribute
    strides = (c_intp * self.ndim)()

    # Fill the strides array with the appropriate values based on the shape and dtype of the underlying array
    for i in range(self.ndim):
        strides[i] = self.shape[i] * np.dtype(self.dtype).itemsize

    return strides
