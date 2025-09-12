# Import necessary modules from tensorflow
import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, Dropout, Attention

# Custom additive attention layer class
class AdditiveAttention(Layer):
    def __init__(self, units, dropout_rate=0.0):
        """
        Additive attention layer constructor.

        Args:
        units (int): The number of units in the dense layer.
        dropout_rate (float, optional): The dropout rate. Defaults to 0.0.
        """
        super(AdditiveAttention, self).__init__()
        self.units = units
        self.dropout_rate = dropout_rate
        self.W1 = Dense(units)
        self.W2 = Dense(units)
        self.dropout = Dropout(dropout_rate)
        self.V = tf.Variable(tf.random.normal([units]))


    def call(self, query, value):
        """
        Compute the additive attention mechanism.

        Args:
        query (tf.Tensor): The query tensor.
        value (tf.Tensor): The value tensor.

        Returns:
        tf.Tensor: The weighted sum of the value tensor based on the attention weights.
        """
        # Compute the attention scores
        score = tf.reduce_sum(
            self.V * tf.nn.tanh(self.W1(query) + self.W2(value)), 
            axis=-1
        )
        
        # Compute the attention weights
        weights = tf.nn.softmax(score)
        
        # Apply dropout
        weights = self.dropout(weights)
        
        # Compute the weighted sum
        context_vector = tf.reduce_sum(
            tf.expand_dims(weights, axis=-1) * value, 
            axis=1
        )
        
        return context_vector, weights

# Example usage
if __name__ == "__main__":
    # Sample query and value tensors
    query = tf.random.normal([32, 10, 128])
    value = tf.random.normal([32, 10, 128])

    # Create an instance of the AdditiveAttention layer
    attention_layer = AdditiveAttention(units=128)

    # Call the attention layer
    context_vector, weights = attention_layer(query, value)
    print("Context Vector Shape:", context_vector.shape)
    print("Weights Shape:", weights.shape)
