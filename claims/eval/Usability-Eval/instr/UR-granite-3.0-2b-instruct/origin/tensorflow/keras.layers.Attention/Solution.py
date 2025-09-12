import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self, multiplier=1.0):
        super(DotProductAttention, self).__init__()
        self.multiplier = multiplier

    def call(self, q, k, v, mask=None):
        # Calculate attention scores
        attention_scores = tf.matmul(q, k, transpose_b=True) * self.multiplier

        # Apply mask if provided
        if mask is not None:
            attention_scores += (mask * -1e9)

        # Softmax to get attention weights
        attention_weights = tf.nn.softmax(attention_scores, axis=-1)

        # Multiply with value to get context vector
        context_vector = tf.matmul(attention_weights, v)

        return context_vector
