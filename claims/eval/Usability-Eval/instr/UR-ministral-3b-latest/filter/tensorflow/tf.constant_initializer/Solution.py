import tensorflow as tf

# Define an initialization method
def constant_initializer(constant_value):
    def initializer(shape, dtype=None):
        return tf.constant(constant_value, shape=shape, dtype=dtype)

    return initializer
