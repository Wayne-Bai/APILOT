import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    def __init__(self):
        super(DotProductAttention, self).__init__()

    def call(self, decoder_outputs, encoder_outputs):
        # Calculate compatibility scores
        scores = tf.matmul(decoder_outputs, encoder_outputs, transpose_b=True)
        # Apply softmax to get attention weights
        attention_weights = tf.nn.softmax(scores, axis=-1)
        # Calculate context vector as the dot product of attention weights and encoder outputs
        context_vector = tf.matmul(attention_weights, encoder_outputs)
        return context_vector, attention_weights

# Example usage
# encoder_outputs shape: (batch_size, seq_length, hidden_dim)
# decoder_outputs shape: (batch_size, hidden_dim)

# Create random tensors for demonstration
batch_size = 2
seq_length = 5
hidden_dim = 3

encoder_outputs = tf.random.normal((batch_size, seq_length, hidden_dim))
decoder_outputs = tf.random.normal((batch_size, hidden_dim))

attention_layer = DotProductAttention()
context_vector, attention_weights = attention_layer(decoder_outputs, encoder_outputs)

print("Context Vector:", context_vector)
print("Attention Weights:", attention_weights)
