import tensorflow as tf

class ExtensionType(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def call(self, inputs):
        # Define custom logic for handling input data
        pass
