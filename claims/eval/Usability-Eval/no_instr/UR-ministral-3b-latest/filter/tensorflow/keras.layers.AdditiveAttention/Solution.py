import tensorflow as tf

class BahdanauAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(BahdanauAttention, self).__init__()

    def build(self, input_shape):
        self.W = self.add_weight(name='W',
                                 shape=(input_shape[-1], input_shape[-1]),
                                 initializer='glorot_uniform',
                                 trainable=True)

        self.U = self.add_weight(name='U',
                                 shape=(input_shape[-1], input_shape[-1]),
                                 initializer='glorot_uniform',
                                 trainable=True)

        self.b = self.add_weight(name='b',
                                 shape=(input_shape[-1],),
                                 initializer='zeros',
                                 trainable=True)

    def call(self, query, values):
        attention_scores = tf.tensordot(query, self.W, axes=1)
        attention_scores = tf.tensordot(values, self.U, axes=1)
        attention_scores = tf.add(attention_scores, self.b)
        attention_weights = tf.nn.softmax(attention_scores, axis=-1)
        context_vector = tf.reduce_sum(
            tf.expand_dims(attention_weights, -1) * values, axis=1)
        return contextvector
