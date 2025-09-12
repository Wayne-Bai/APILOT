import numpy as np
import ctypes

class ArrayShape:
    def __init__(self, array):
        self.array = array
        self.ndim = self.array.ndim
        self.shape_ctypes_array = self._create_ctypes_shape_array()

    def _create_ctypes_shape_array(self):
        # Determine the appropriate ctypes type for the platform
        c_intp_type = ctypes.c_long if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p) else ctypes.c_longlong
        # Create a ctypes array of length self.ndim
        shape_array = (c_intp_type * self.ndim)()
        # Populate the ctypes array with the shape of the underlying array
        for i in range(self.ndim):
            shape_array[i] = self.array.shape[i]
        return shape_array

# Example usage
array = np.array([[1, 2, 3], [4, 5, 6]])
array_shape = ArrayShape(array)
print(array_shape.shape_ctypes_array)
