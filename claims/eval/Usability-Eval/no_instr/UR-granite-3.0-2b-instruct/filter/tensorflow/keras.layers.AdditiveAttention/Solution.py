import tensorflow as tf

# Define the Additive Attention layer
class AdditiveAttention(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super(AdditiveAttention, self).__init__(**kwargs)
        self.w1 = tf.keras.layers.Dense(units, activation='relu')
        self.w2 = tf.keras.layers.Dense(units)

    def call(self, query, values, mask=None):
        query_lengths = tf.reduce_sum(mask, axis=1, keepdims=True)
        query = self.w1(query)
        query = tf.nn.tanh(query)
        query *= tf.math.sqrt(query_lengths)
        query = self.w2(query)
        attention_weights = tf.nn.softmax(query, axis=-1)
        context_vector = tf.reduce_sum(values * attention_weights, axis=1)
        return context_vector, attention_weights

# Create an instance of the Additive Attention layer
attention = AdditiveAttention(units=128)

# Define a sample input
query = tf.random.normal([10, 10])
values = tf.random.normal([10, 10, 10])

# Apply the Additive Attention layer
context_vector, attention_weights = attention(query, values)
