import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(DotProductAttention, self).__init__(**kwargs)

    def call(self, query, keys, values, mask=None):
        # Compute the dot products between the query and the keys
        score = tf.matmul(query, keys, transpose_b=True)

        # Optionally mask out the scores
        if mask is not None:
            score += (mask * -1e9)  # Using a large negative value to mask

        # Apply the softmax to get the attention weights
        attention_weights = tf.nn.softmax(score, axis=-1)

        # Compute the context vector as the weighted sum of the values
        context_vector = tf.matmul(attention_weights, values)

        return context_vector, attention_weights

# Example usage:
# Defining the attention layer
attention_layer = DotProductAttention()

# Dummy data to simulate some query, keys, and values
query = tf.random.normal(shape=(1, 10))   # E.g., shape [batch_size, query_dimension]
keys = tf.random.normal(shape=(5, 10))    # E.g., shape [timesteps, key_dimension]
values = tf.random.normal(shape=(5, 20))  # E.g., shape [timesteps, value_dimension]

# Compute attention
context_vector, attention_weights = attention_layer(query, keys, values)

print("Context Vector:", context_vector)
print("Attention Weights:", attention_weights)
