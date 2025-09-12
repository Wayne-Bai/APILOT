import tensorflow as tf

# Assuming a DTensor layout representation involves dimensions and dtype
class DTensorLayout:
    def __init__(self, shape, dtype):
        self.shape = shape
        self.dtype = dtype

    def __repr__(self):
        return f"DTensorLayout(shape={self.shape}, dtype={self.dtype})"

# Example usage
layout = DTensorLayout(shape=(2, 3, 4), dtype=tf.float32)
print(layout)
