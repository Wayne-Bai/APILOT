import numpy as np

class MyArray(np.ndarray):
    def __init__(self, shape, dtype):
        super().__init__(shape, dtype)
        self.strides = np.lib.stride_tricks.strided. StridedArray(self.shape, self.strides)

    def __str__(self):
        return f"MyArray with shape {self.shape} and strides {self.strides}"
