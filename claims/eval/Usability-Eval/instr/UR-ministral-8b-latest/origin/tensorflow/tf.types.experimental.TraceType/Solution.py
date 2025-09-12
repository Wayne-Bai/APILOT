import tensorflow as tf

# A custom Layer type
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=[input_shape[-1], self.units],
                                      initializer='glorot_uniform')

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)

# Example usage
inputs = tf.keras.Input(shape=(5,))
outputs = CustomLayer(3)(inputs)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Generate a model graph with tf.function tracing
@tf.function
def custom_function(inputs):
    outputs = CustomLayer(3)(inputs)
    return outputs

custom_function_result = custom_function(inputs)

print(custom_function_result)
