import tensorflow as tf

class AdditiveAttention(tf.keras.layers.Layer):
    """
    Bahdanau-style additive attention.
    
    Lordkipanidze, Baoluo, et al. "An attention attentive neural network for synthesis of a mnemonic by changing musical artifacts."
    
    Parameters:
    num_units (int): Number of hidden units.
    """
    
    def __init__(self, num_units):
        super(AdditiveAttention, self).__init__()
        self.W = tf.keras.layers.Embedding(input_dim=100, output_dim=num_units)
        self.V = tf.keras.layers.Embedding(input_dim=100, output_dim=num_units)
        self.U = tf.keras.layers.Dense(num_units)
        
    def call(self, query, context):
        """
        Apply attention mechanism on the `context` using the `query`.
        
        Parameters:
        query (tf.Tensor): The query tensor.
        context (tf.Tensor): The context tensor.
        
        Returns:
        tf.Tensor: The output tensor.
        """
        
        # Compute the scores
        scores = self.W(query) + tf.expand_dims(tf.reduce_sum(self.V(context), axis=1), axis=1) + self.U(context)
        
        # Apply softmax
        scores = tf.nn.softmax(scores)
        
        # Compute the context weighted by the scores
        output = tf.reduce_sum(context * tf.expand_dims(scores, axis=2), axis=1)
        
        return output

# Example usage:
query = tf.random.normal((1, 10))
context = tf.random.normal((1, 10, 10))
attention = AdditiveAttention(num_units=10)
output = attention(query, context)
print(output.shape)
