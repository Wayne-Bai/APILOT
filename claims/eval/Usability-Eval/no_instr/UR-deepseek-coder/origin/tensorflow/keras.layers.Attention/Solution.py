import tensorflow as tf
from tensorflow.keras.layers import Layer

class LuongAttention(Layer):
    def __init__(self, units):
        super(LuongAttention, self).__init__()
        self.units = units
        self.W = tf.keras.layers.Dense(units)

    def call(self, query, values):
        # query shape: (batch_size, hidden_size)
        # values shape: (batch_size, seq_len, hidden_size)

        # Transform query to have the same dimension as values
        query_with_time_axis = tf.expand_dims(query, 1)

        # score shape: (batch_size, seq_len, hidden_size)
        score = tf.matmul(query_with_time_axis, self.W(values), transpose_b=True)

        # attention_weights shape: (batch_size, seq_len, 1)
        attention_weights = tf.nn.softmax(score, axis=1)

        # context_vector shape: (batch_size, hidden_size)
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights

# Example usage:
# query = tf.random.normal([64, 128])  # Example query with batch size 64 and hidden size 128
# values = tf.random.normal([64, 20, 128])  # Example values with batch size 64, sequence length 20, and hidden size 128
# attention_layer = LuongAttention(128)
# context_vector, attention_weights = attention_layer(query, values)
# print(context_vector.shape)  # Should print (64, 128)
# print(attention_weights.shape)  # Should print (64, 20, 1)
