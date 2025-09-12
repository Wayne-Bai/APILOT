import tensorflow as tf

# Define a constant initializer
class ConstantInitializer(tf.keras.initializers.Initializer):
    def __init__(self, value):
        self.value = value

    def __call__(self, shape, dtype=None):
        return tf.constant(self.value, dtype=dtype, shape=shape)

# Example of using the ConstantInitializer
initializer = ConstantInitializer(value=5.0)
tensor = initializer(shape=(2, 3))

print(tensor)
