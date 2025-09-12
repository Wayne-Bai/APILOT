import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, Input
from tensorflow.keras.init import RandomNormal

class BahdanauAttention(Layer):
    def __init__(self, units):
        super(BahdanauAttention, self).__init__()
        self.W1 = Dense(units)
        self.W2 = Dense(units)
        self.V = Dense(1)

    def call(self, query, values):
        query_with_time_axis = tf.expand_dims(query, 1)
        score = tf.nn.tanh(self.W1(query_with_time_axis) + self.W2(values))
        attention_weights = tf.nn.softmax(self.V(score), axis=1)
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)
        return context_vector, attention_weights

# Example usage:
query = tf.constant([[-0.5, -0.5], [0.5, 0.5], [-0.2, -0.2]])
context = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
attention_layer = BahdanauAttention(units=2)

output, weights = attention_layer(query, context)
print(output.numpy())
print(weights.numpy())
