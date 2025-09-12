
import tensorflow as tf

class SumLayer(tf.keras.layers.Layer):
    def __init__(self, input_shape):
        super().__init__()
        self.input_shape = input_shape

    def call(self, inputs):
        return tf.add(inputs)
