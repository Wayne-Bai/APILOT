import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super().__init__()
        self.units = units
        self.w_queries = tf.keras.layers.Dense(units)
        self.w_keys = tf.keras.layers.Dense(units)
        self.w_values = tf.keras.layers.Dense(units)

    def call(self, v, k, q, mask=None):
        # Query, key, value pairs are embedded, passed through the projected layers
        v_proj = self.w_values(v)
        k_proj = self.w_keys(k)
        q_proj = self.w_queries(q)

        # Compute dot product attention
        scores = tf.matmul(q_proj, k_proj, transpose_b=True)

        # Apply padding, to ignore it during attention computation
        if mask is not None:
            scores += (mask * -1e9)

        # Epsilon to stabilize the gradient
        scores = scores + tf.expand_dims(tf.random.uniform(tf.shape(scores),
                                                            minval=0.0, maxval=0.5, dtype=scores.dtype), -1)

        # Apply softmax to the scores
        scores /=  tf.cast(tf.sqrt(tf.shape(scores)[-1]), dtype=tf.float32)

        # We compute context vectors from the (oul out) scores
        context = tf.matmul(scores, v_proj)
        return context
