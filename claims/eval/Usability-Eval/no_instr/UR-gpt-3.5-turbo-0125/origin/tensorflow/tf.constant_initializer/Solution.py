
import tensorflow as tf

class ConstantInitializer:
    def __init__(self, value):
        self.value = value

    def __call__(self, shape, dtype=None):
        return tf.fill(shape, self.value)

# Example usage
initializer = ConstantInitializer(5.0)
tensor = initializer((2, 3))
print(tensor)
