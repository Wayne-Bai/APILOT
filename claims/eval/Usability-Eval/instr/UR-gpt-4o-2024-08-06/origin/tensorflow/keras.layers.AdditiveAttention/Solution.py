import tensorflow as tf

class BahdanauAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(BahdanauAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, query, values):
        # Expand the query to enable addition across the time steps
        query_with_time_axis = tf.expand_dims(query, 1)

        # Calculate score using additive attention mechanism
        score = tf.nn.tanh(self.W1(query_with_time_axis) + self.W2(values))

        # Calculate attention weights
        attention_weights = tf.nn.softmax(self.V(score), axis=1)

        # Context vector is the weighted sum of values
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights

# Example usage:
def example_usage():
    # Dummy inputs
    query = tf.random.normal(shape=(32, 64))  # Batch size x Query size
    values = tf.random.normal(shape=(32, 10, 64))  # Batch size x Time steps x Values size

    # Creating the attention layer instance
    attention_layer = BahdanauAttention(units=64)

    # Getting context vector and attention weights
    context_vector, attention_weights = attention_layer(query, values)
    
    print('Context Vector Shape:', context_vector.shape)
    print('Attention Weights Shape:', attention_weights.shape)

example_usage()
