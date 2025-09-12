import tensorflow as tf

class AdditiveAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(AdditiveAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, values):
        # query shape: (batch_size, query_size)
        # values shape: (batch_size, value_count, value_size)

        # Expand query to match the batch_size and number of values
        query_with_time_axis = tf.expand_dims(query, 1)

        # Score calculation (Bahdanau's score formula)
        score = self.V(tf.nn.tanh(self.W1(query_with_time_axis) + self.W2(values)))

        # Apply softmax to normalize
        attention_weights = tf.nn.softmax(score, axis=1)

        # Weighted sum of values (context vector)
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights

# Example of how you might use the AdditiveAttention layer
units = 10  # Number of units for the Dense layers in the attention mechanism
attention_layer = AdditiveAttention(units)

query = tf.random.normal(shape=(32, 64))  # Example query with shape (batch_size, query_size)
values = tf.random.normal(shape=(32, 50, 64))  # Example values with shape (batch_size, value_count, value_size)

context_vector, attention_weights = attention_layer(query, values)

print("Context Vector Shape:", context_vector.shape)
print("Attention Weights Shape:", attention_weights.shape)
