import tensorflow as tf

class AdditiveAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(AdditiveAttention, self).__init__()
        self.Wa = self.add_weight(shape=(units, units), initializer='random_normal', trainable=True)
        self.Ua = self.add_weight(shape=(units, units), initializer='random_normal', trainable=True)
        self.Va = self.add_weight(shape=(units, 1), initializer='random_normal', trainable=True)

    def call(self, query, values):
        # query: shape (..., query_dim)
        # values: shape (..., seq_len, values_dim)
        
        # Expand query to match the shape of values
        query_with_time_axis = tf.expand_dims(query, 1)
        
        # Calculate the attention scores
        score = tf.nn.tanh(tf.matmul(query_with_time_axis, self.Wa) + tf.matmul(values, self.Ua))
        
        # Calculate the attention weights
        attention_weights = tf.nn.softmax(tf.matmul(score, self.Va), axis=1)

        # Calculate the context vector
        context_vector = attention_weights * values
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights
