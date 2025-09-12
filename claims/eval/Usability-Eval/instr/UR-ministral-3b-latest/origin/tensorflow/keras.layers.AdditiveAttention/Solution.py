import tensorflow as tf

# Defining the Additive Attention Layer
class BahdanauAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(BahdanauAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.v = tf.keras.layers.Dense(1)

    def call(self, query, values):
        # Hidden with the same dimension as context. Need to reshape 3rd dimension (values_dim=len(word idx latest)
        hidden = self.W1(query)
        values = self.W2(values)
        energy = tf.reduce_sum(self.v(tf.tanh(hidden + values)) * values, axis=-2)

        attention_weights = tf.nn.softmax(energy, axis=1)
        context_vector = tf.reduce_sum(values * attention_weights[:, tf.newaxis, :], axis=1)

        return context_vector, attention_weights

# Example usage
units = 512
query = tf.keras.Input(shape=(1, units))
values = tf.keras.Input(shape=(None, units))

attention_layer = BahdanauAttention(units)
output, attention_weights = attention_layer(query, values)
print(output.shape)  # Should be same as input shape, confirming the correct attention: (1, output_dim)
