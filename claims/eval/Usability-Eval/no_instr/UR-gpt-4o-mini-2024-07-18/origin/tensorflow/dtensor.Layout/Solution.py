import tensorflow as tf

# Creating a simple DTensor layout representation
class DTensorLayout:
    def __init__(self, shape, dtype=tf.float32):
        self.shape = shape
        self.dtype = dtype

    def __repr__(self):
        return f"DTensorLayout(shape={self.shape}, dtype={self.dtype})"

# Example usage
layout = DTensorLayout(shape=(2, 3, 4), dtype=tf.float32)
print(layout)
