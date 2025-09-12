import tensorflow as tf

class BaseExtensionType(tf.keras.Model):
    def __init__(self, **kwargs):
        super(BaseExtensionType, self).__init__(**kwargs)

    def build(self, input_shape):
        pass

    def call(self, inputs):
        pass

    def compute_output_shape(self, input_shape):
        pass
