import tensorflow as tf

class LuongAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(LuongAttention, self).__init__()
        self.W = tf.keras.layers.Dense(units)
        self.U = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, value):
        # query: (batch_size, time_steps, units)
        # value: (batch_size, time_steps, units)
        query_with_time_axis = tf.expand_dims(query, 1)
        # query_with_time_axis: (batch_size, 1, time_steps, units)
        weights = self.V(tf.nn.tanh(
            self.W(query_with_time_axis) + self.U(value)))
        # weights: (batch_size, time_steps, time_steps, 1)
        weights = tf.nn.softmax(weights, axis=2)
        # weights: (batch_size, time_steps, time_steps, 1)
        context_vector = weights * value
        context_vector = tf.reduce_sum(context_vector, axis=2)
        return context_vector, weights

# Example usage
if __name__ == "__main__":
    attention = LuongAttention(128)
    query = tf.random.normal([32, 10, 128])  # batch_size=32, time_steps=10, units=128
    value = tf.random.normal([32, 10, 128])  # batch_size=32, time_steps=10, units=128
    context_vector, weights = attention(query, value)
    print(context_vector.shape)  # Output: (32, 10, 128)
    print(weights.shape)  # Output: (32, 10, 10, 1)
