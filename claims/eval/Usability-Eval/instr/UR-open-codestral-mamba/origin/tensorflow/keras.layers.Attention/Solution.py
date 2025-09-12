import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(DotProductAttention, self).__init__()

    def call(self, q, k, v, mask):
        # Calculate the attention weights
        # using the dot product between "q" and "k".
        attn_weights = tf.matmul(q, k, transpose_b=True)

        # Softmax the attention weights
        # and apply the mask if provided
        if mask is not None:
            attn_weights += (mask * -1e9)
        attn_weights = tf.nn.softmax(attn_weights, axis=-1)

        # Calculate the final attention
        # output as the weighted sum of the values "v".
        output = tf.matmul(attn_weights, v)

        return output, attn_weights

# Example usage
q = tf.random.normal([10, 32, 64])
k = tf.random.normal([10, 32, 64])
v = tf.random.normal([10, 32, 64])
mask = tf.random.normal([10, 32, 32])

attn = DotProductAttention()
attn_output, attn_weights = attn(q, k, v, mask)
