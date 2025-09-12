import numpy as np
import ctypes

class CustomArray:
    def __init__(self, shape, dtype):
        self.data = np.array(shape, dtype=dtype)
        self.ndim = len(shape)

    @property
    def strides(self):
        # Create a ctypes array of length self.ndim where the basetype is the same as for the shape attribute
        strides_array = (ctypes.c_int * self.ndim)()

        # Fill in the strides information
        strides_array[:] = self.data.strides

        return strides_array


# Create a custom array with shape (3, 4, 5) and dtype int
custom_array = CustomArray((3, 4, 5), np.int32)

# Get the strides information
strides_info = custom_array.strides

# Print the strides information
print("Strides information (in bytes):", strides_info[:])
