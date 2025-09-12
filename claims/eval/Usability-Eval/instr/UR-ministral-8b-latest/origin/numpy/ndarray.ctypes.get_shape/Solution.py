import numpy as np

class MyClass:
    def __init__(self, array, dtype):
        self.array = np.array(array, dtype=dtype)
        self.ndim = self.array.ndim
        self.shape = self._get_shape_ctypes()

    def _get_shape_ctypes(self):
        ctypes_size = self.array.ndim  # Length of the array shape ctypes array
        ctypes_shapes = [self.array.shape[i] for i in range(ctypes_size)]
        shape_ctypes_array = (ctypes.c_int * ctypes_size,)
        return np.array(ctypes_shapes, dtype=shape_ctypes_array).flatten()

# Usage
array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
my_instance = MyClass(array, dtype=np.int32)
print(my_instance.shape)
