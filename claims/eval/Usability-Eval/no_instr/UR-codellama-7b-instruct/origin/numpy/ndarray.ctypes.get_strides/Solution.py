
import numpy as np

# function to create a ctypes array of length self.ndim where the basetype is the same as for the shape attribute
def create_strides_array(self):
    # create an empty ctypes array of length self.ndim
    strides = np.empty(shape=(self.ndim,), dtype=np.intp)
    
    # loop over each dimension and set the corresponding stride value
    for i in range(self.ndim):
        strides[i] = self.strides[i]
    
    return strides
