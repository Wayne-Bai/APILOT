import tensorflow as tf

class GraphFunction(tf.keras.layers.Layer):
    def __init__(self, units, activation='relu', **kwargs):
        super(GraphFunction, self).__init__(**kwargs)
        self.units = units
        self.activation = activation

    def build(self, input_shape):
        self.kernel = self.add_weight(shape=(input_shape[1], self.units),
                                      initializer='glorot_uniform',
                                      name='kernel')
        self.bias = self.add_weight(shape=(self.units,),
                                    initializer='zeros',
                                    name='bias')

    def call(self, inputs):
        output = tf.matmul(inputs, self.kernel)
        output = tf.nn.bias_add(output, self.bias)
        output = tf.nn.relu(output)
        return output
