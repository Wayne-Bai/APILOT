import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(DotProductAttention, self).__init__()

    def call(self, query, key, value, mask=None):
        # Dot product between query and key
        scores = tf.matmul(query, key, transpose_b=True)

        # Optional masking of scores
        if mask is not None:
            scores += (mask * -1e9)

        # Apply softmax to get probabilities
        attention_weights = tf.nn.softmax(scores, axis=-1)

        # Weighted sum of value by attention weights
        output = tf.matmul(attention_weights, value)

        # Return output and the attention weights (often useful for visualization)
        return output, attention_weights

# Usage example:
# Assuming `query`, `key`, `value` tensors and an optional `mask`
# query = tf.random.normal(shape=(batch_size, num_queries, depth))
# key = tf.random.normal(shape=(batch_size, num_keys, depth))
# value = tf.random.normal(shape=(batch_size, num_keys, value_depth))
# output, attention_weights = DotProductAttention()(query, key, value)
