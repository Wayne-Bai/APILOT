import tensorflow as tf

class DTensor(tf.keras.layers.Layer):
    def __init__(self, shape, **kwargs):
        super().__init__(**kwargs)
        self.shape = shape
    
    def build(self, input_shape):
        super().build(input_shape)
        self.weight = self.add_weight("w", shape=tf.TensorShape([1, 1]), initializer="ones")
        self.bias = self.add_weight("b", shape=tf.TensorShape([1, 1]), initializer="zeros")
    
    def call(self, inputs):
        outputs = tf.matmul(inputs, self.weight) + self.bias
        return outputs
