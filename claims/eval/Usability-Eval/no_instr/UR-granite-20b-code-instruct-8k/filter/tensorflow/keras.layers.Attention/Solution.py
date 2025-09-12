import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(DotProductAttention, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.W1 = self.add_weight(shape=(input_shape[-1], self.units),
                                  initializer='uniform',
                                  trainable=True)
        self.W2 = self.add_weight(shape=(input_shape[-1], self.units),
                                  initializer='uniform',
                                  trainable=True)
        self.b = self.add_weight(shape=(self.units,),
                                 initializer='uniform',
                                 trainable=True)

    def call(self, inputs):
        query, key = inputs
        score = tf.matmul(query, self.W1) + tf.matmul(key, self.W2) + self.b
        attention_weights = tf.nn.softmax(score, axis=-1)
        context_vector = tf.reduce_sum(key * tf.expand_dims(attention_weights, axis=-1), axis=1)
        return context_vector, attention_weights
