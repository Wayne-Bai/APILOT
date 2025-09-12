
import tensorflow as tf

class DTensorLayout:
    def __init__(self, shape, dtype):
        self.shape = shape
        self.dtype = dtype

    def get_shape(self):
        return self.shape

    def get_dtype(self):
        return self.dtype

# Example usage
layout = DTensorLayout(shape=[3, 4], dtype=tf.float32)
print("Shape:", layout.get_shape())
print("Data type:", layout.get_dtype())
