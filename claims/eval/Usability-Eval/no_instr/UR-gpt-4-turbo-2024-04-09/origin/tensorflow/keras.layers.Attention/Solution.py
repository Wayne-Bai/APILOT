import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(DotProductAttention, self).__init__()

    def call(self, query, key, value, mask=None):
        """
        Calculate the attention weights and output.

        Args:
        query: Query `Tensor` of shape `[batch_size, query_depth]`.
        key: Key `Tensor` of shape `[batch_size, sequence_length, key_depth]`.
        value: Value `Tensor` of shape `[batch_size, sequence_length, value_depth]`.
        mask: Optional `Tensor` representing sequence mask of shape `[batch_size, sequence_length]`.

        Returns:
        context_vector: weighted sum of the values based on attention, `[batch_size, value_depth]`.
        attention_weights: attention weights, `[batch_size, sequence_length]`.
        """
        # Expand the query to match the dimensions of the key
        query_with_time_axis = tf.expand_dims(query, 1)

        # Calculate the dot product of the query and the key
        scores = tf.matmul(query_with_time_axis, key, transpose_b=True)

        # Optional mask for excluding zeros for padded positions
        if mask is not None:
            scores += (mask * -1e9)

        # Apply softmax to calculate attention weights
        attention_weights = tf.nn.softmax(scores, axis=-1)

        # Use attention weights to calculate the weighted sum of value
        context_vector = tf.matmul(attention_weights, value)
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights

# Example Usage:
# Assume batch_size=1, sequence_length=3, depth=5
query = tf.random.normal([1, 5])
key = tf.random.normal([1, 3, 5])
value = tf.random.normal([1, 3, 5])
attention_layer = DotProductAttention()
context_vector, attention_weights = attention_layer(query, key, value)
print("Context Vector:\n", context_vector)
print("Attention Weights:\n", attention_weights)
