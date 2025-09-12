
import tensorflow as tf

class Attention(tf.keras.layers.Layer):
    def __init__(self, units, dropout=0.1):
        super(Attention, self).__init__()
        self.units = units
        self.dropout = dropout
        self.attention_layer = tf.keras.layers.Dense(units, activation='tanh')
        self.attention_dropout = tf.keras.layers.Dropout(rate=self.dropout)
    
    def call(self, query, value, mask=None):
        # Calculate attention scores
        attention_scores = tf.matmul(query, value, transpose_b=True) / math.sqrt(self.units)
        
        # Mask padded tokens
        if mask is not None:
            attention_scores += (1 - tf.cast(mask, dtype=attention_scores.dtype)) * -1e9
        
        # Apply softmax to the scores
        attention_scores = tf.nn.softmax(attention_scores, axis=-1)
        
        # Normalize the attention weights
        attention_weights = attention_scores / (tf.reduce_sum(attention_scores, axis=-1, keepdims=True) + 1e-9)
        
        # Calculate the weighted sum of the value
        output = tf.matmul(attention_weights, value)
        
        return output, attention_scores
