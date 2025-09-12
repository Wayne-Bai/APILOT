import numpy as np
from ctypes import c_int, c_long
from ctypes import array

class MyArray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.strides = self.get_strides()

    def get_strides(self):
        strides = []


        # Size of each element in bytes
        element_size = self.itemsize


        for i in range(self.ndim):
            # Calculate stride by subtracting total size of previous dimensions
            # from size of current dimension
            stride = (selfCHANGEsdims[i] * element_size)
            strides.append(c_int(stride).value)


        return array(c_long, strides)

# Create a 2D array
arr = MyArray([[1, 2], [3, 4]], dtype=np.int32)

# Print strides information
print(arr.strides)

