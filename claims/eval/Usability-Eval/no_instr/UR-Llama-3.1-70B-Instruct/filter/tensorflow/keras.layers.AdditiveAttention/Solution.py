import tensorflow as tf

class AdditiveAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(AdditiveAttention, self).__init__()
        self.units = units
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, values):
        score = tf.nn.tanh(
            self.W1(query) + self.W2(values)
        )
        weights = self.V(score)
        weights = tf.nn.softmax(weights, axis=-1)
        context_vector = weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, weights

# Test the layer
if __name__ == "__main__":
    # Creating the layer with units of 64
    attention = AdditiveAttention(64)

    # Creating test input
    query = tf.random.uniform((1, 64))  # (batch, features)
    values = tf.random.uniform((1, 10, 64))  # (batch, time_steps, features)

    # Using the layer
    context_vector, weights = attention(query, values)

    print("Context Vector Shape:", context_vector.shape)
    print("Weights Shape:", weights.shape)
