import tensorflow as tf
from tensorflow.keras import layers

class LuongAttentionLayer(layers.Layer):
    def __init__(self):
        super(LuongAttentionLayer, self).__init__()

    def build(self, input_shape):
        self.W = self.add_weight(name='attention_weight',
                                 shape=(input_shape[-1], 1),
                                 initializer='random_normal',
                                 trainable=True)

    def call(self, values, query):
        query_with_time_axis = tf.expand_dims(query, 1)
        score = tf.nn.softmax(tf.nn.tanh(tf.tensordot(values, query_with_time_axis, axes=(-1, -2))))
        context = tf.reduce_sum(score * values, axis=1)
        return context
