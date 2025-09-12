import numpy as np
import ctypes

# Assuming self is an instance of numpy array
# Creating a ctypes array with the strides information
strides = np.array(self.strides)
c_strides = (ctypes.c_intp * len(self.shape))(*strides)
