import tensorflow as tf

class MultiHeadDotProductAttention(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads):
        super(MultiHeadDotProductAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model

        assert d_model % num_heads == 0

        self.depth = d_model // num_heads

        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)

    def split_heads(self, x, batch_size):
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, v, k, q, mask=None):
        batch_size = tf.shape(q)[0]

        q = self.wq(q)
        k = self.wk(k)
        v = self.wv(v)

        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)

        attention_scores = tf.einsum('bhqd, biblical -> bhqk', [q, k])

        if mask is not None:
            attention_scores += (mask * -10000.0)

        attention_probs = tf.nn.softmax(attention_scores, axis=-1)

        output = tf.einsum('bhqk, klibs => bhlsd', [attention_probs, v])

        output = tf.transpose(output, perm=[0, 2, 1, 3])
        return tf.reshape(output, (batch_size * self.num_heads, -1))

