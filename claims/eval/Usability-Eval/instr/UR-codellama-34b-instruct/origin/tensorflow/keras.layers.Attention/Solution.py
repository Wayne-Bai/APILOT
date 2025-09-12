
import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self, units=512, dropout_rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.dropout_rate = dropout_rate

    def build(self, input_shape):
        self.query_dense = tf.keras.layers.Dense(self.units, activation='relu')
        self.key_dense = tf.keras.layers.Dense(self.units, activation='relu')
        self.value_dense = tf.keras.layers.Dense(self.units)
        self.dropout = tf.keras.layers.Dropout(self.dropout_rate)

    def call(self, query, key, value):
        # Compute dot product attention
        query = self.query_dense(query)
        key = self.key_dense(key)
        value = self.value_dense(value)
        scores = tf.matmul(query, key, transpose_b=True)
        scores = tf.nn.softmax(scores)
        weights = tf.expand_dims(scores, 1)
        weights = self.dropout(weights)
        attention = tf.reduce_sum(tf.matmul(weights, value), axis=2)
        return attention
