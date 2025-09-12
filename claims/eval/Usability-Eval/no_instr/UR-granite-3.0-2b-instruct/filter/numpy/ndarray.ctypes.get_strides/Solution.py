import numpy as np

class MyArray(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.info = getattr(obj, 'info', None)

    @property
    def strides(self):
        return np.Lib.stride_numbers.strides(self.info)
