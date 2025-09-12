
import tensorflow as tf

class BaseGraphFunction(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(BaseGraphFunction, self).__init__(**kwargs)
    
    def call(self, inputs):
        # Define the base graph function here
        raise NotImplementedError()
