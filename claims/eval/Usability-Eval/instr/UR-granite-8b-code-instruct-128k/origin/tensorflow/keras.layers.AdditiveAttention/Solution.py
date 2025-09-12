
import tensorflow as tf
from tensorflow.keras.layers import Layer
class AdditiveAttention(Layer):
    def __init__(self, units):
        super(AdditiveAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, values):
        query_proj = self.W1(query)
        values_proj = self.W2(values)
        energy = tf.keras.activations.tanh(query_proj + values_proj)
        attention_weights = self.V(energy)
        attention_weights = tf.nn.softmax(attention_weights, axis=1)
        context_vector = tf.reduce_sum(attention_weights * values, axis=1)

        return context_vector
