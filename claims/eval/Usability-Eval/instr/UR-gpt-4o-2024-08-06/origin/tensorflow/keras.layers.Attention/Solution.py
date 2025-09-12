import tensorflow as tf

class LuongAttention(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super(LuongAttention, self).__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        self.Wa = self.add_weight(shape=(input_shape[-1], self.units),
                                  initializer="random_normal",
                                  name="attention_weights")
        super(LuongAttention, self).build(input_shape)

    def call(self, query, values):
        # query: [batch_size, query_dim] or [batch_size, query_len, query_dim]
        # values: [batch_size, value_len, value_dim]

        # Calculate score
        # score = tf.matmul(query, values, transpose_b=True) if batched queries
        # else
        query = tf.expand_dims(query, 1)  # [batch_size, 1, query_dim]
        score = tf.matmul(query, self.Wa)  # [batch_size, 1, units]
        score = tf.matmul(score, values, transpose_b=True)  # [batch_size, 1, value_len]
        
        # Compute attention weights
        attention_weights = tf.nn.softmax(score, axis=-1)  # [batch_size, 1, value_len]
        
        # Compute context vector
        context_vector = tf.matmul(attention_weights, values)  # [batch_size, 1, value_dim]
        context_vector = tf.squeeze(context_vector, axis=1)  # [batch_size, value_dim]
        
        return context_vector, attention_weights

# Example usage:
# query_shape = (batch_size, query_dim)
# values_shape = (batch_size, value_len, value_dim)
# attention_layer = LuongAttention(units)
# context_vector, attention_weights = attention_layer(query, values)
