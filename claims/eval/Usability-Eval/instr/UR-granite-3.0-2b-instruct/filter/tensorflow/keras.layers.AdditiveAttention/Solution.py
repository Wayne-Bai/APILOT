import tensorflow as tf

class AdditiveAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(AdditiveAttention, self).__init__()
        self.w1 = tf.keras.layers.Dense(units, activation='tanh')
        self.w2 = tf.keras.layers.Dense(units)

    def call(self, query, values):
        # query shape: (batch_size, seq_length, units)
        # values shape: (batch_size, seq_length, units)

        # query tanh
        query_tanh = self.w1(query)

        # scores shape: (batch_size, seq_length)
        scores = self.w2(query_tanh)

        # attention weights shape: (batch_size, seq_length)
        attention_weights = tf.nn.softmax(scores, axis=-1)

        # context vector shape: (batch_size, units)
        context_vector = tf.reduce_sum(values * attention_weights, axis=-1)

        return context_vector, attention_weights
