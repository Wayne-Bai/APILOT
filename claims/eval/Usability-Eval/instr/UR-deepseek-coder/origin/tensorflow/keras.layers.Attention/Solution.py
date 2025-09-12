import tensorflow as tf
from tensorflow.keras.layers import Layer

class LuongAttention(Layer):
    def __init__(self, units):
        super(LuongAttention, self).__init__()
        self.W = tf.keras.layers.Dense(units)

    def call(self, query, values):
        # query shape: (batch_size, query_depth)
        # values shape: (batch_size, seq_len, value_depth)
        
        # Transform query to have the same depth as values
        query_with_time_axis = tf.expand_dims(query, 1)
        
        # Compute scores
        scores = tf.matmul(query_with_time_axis, self.W(values), transpose_b=True)
        scores = tf.squeeze(scores, axis=1)
        
        # Compute attention weights
        attention_weights = tf.nn.softmax(scores, axis=1)
        
        # Compute context vector
        context_vector = tf.matmul(tf.expand_dims(attention_weights, 1), values)
        context_vector = tf.squeeze(context_vector, axis=1)
        
        return context_vector, attention_weights

# Example usage:
# query = tf.random.normal([32, 10])  # batch_size=32, query_depth=10
# values = tf.random.normal([32, 20, 15])  # batch_size=32, seq_len=20, value_depth=15
# attention_layer = LuongAttention(15)
# context_vector, attention_weights = attention_layer(query, values)
