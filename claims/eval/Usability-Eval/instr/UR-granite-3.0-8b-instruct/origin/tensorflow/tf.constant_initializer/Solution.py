import tensorflow as tf

class ConstantInitializer(tf.keras.initializers.Initializer):
    def __init__(self, value):
        self.value = value

    def __call__(self, shape, dtype=None):
        return tf.fill(shape, self.value)
