import tensorflow as tf

class DTensorLayout:
    def __init__(self, shape, dtype, device):
        self.shape = shape
        self.dtype = dtype
        self.device = device

    def __str__(self):
        return f"DTensorLayout(shape={self.shape}, dtype={self.dtype}, device={self.device})"
