import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(DotProductAttention, self).__init__()

    def call(self, query, key, value):
        # Calculate the dot products between the query and keys
        scores = tf.matmul(query, key, transpose_b=True)

        # Scale the scores
        d_k = tf.cast(tf.shape(key)[-1], tf.float32)
        scaled_scores = scores / tf.sqrt(d_k)

        # Calculate the weights using softmax
        attention_weights = tf.nn.softmax(scaled_scores, axis=-1)

        # Apply the attention weights to the values
        output = tf.matmul(attention_weights, value)

        return output, attention_weights

# Example usage
# query is of shape (batch_size, 1, depth)
# key and value are of shape (batch_size, num_key_value_pairs, depth)

# Creating dummy data
batch_size = 2
depth = 4
num_key_value_pairs = 3

query = tf.random.uniform((batch_size, 1, depth))
key = tf.random.uniform((batch_size, num_key_value_pairs, depth))
value = tf.random.uniform((batch_size, num_key_value_pairs, depth))

attention_layer = DotProductAttention()
output, attention_weights = attention_layer(query, key, value)

print("Output:", output)
print("Attention Weights:", attention_weights)
