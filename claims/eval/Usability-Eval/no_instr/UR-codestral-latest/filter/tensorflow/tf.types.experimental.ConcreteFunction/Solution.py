import tensorflow as tf

class CustomLayer(tf.keras.layers.Layer):
    def __init__(self):
        super(CustomLayer, self).__init__()

    def call(self, inputs):
        # You can define your differentiable graph function here
        return tf.square(inputs)

    def get_config(self):
        config = super().get_config().copy()
        return config
