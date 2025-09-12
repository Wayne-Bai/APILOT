
import tensorflow as tf
from tensorflow import keras

class DotProductAttention(keras.layers.Layer):
    def __init__(self, **kwargs):
        super(DotProductAttention, self).__init__(**kwargs)
        
    def call(self, query, key, value):
        # Calculate the dot product attention score
        attention_scores = tf.matmul(query, key, transpose_b=True)
        attention_scores /= math.sqrt(key.shape[-1].value)
        
        # Normalize the attention scores
        attention_weights = tf.nn.softmax(attention_scores, axis=-1)
        
        # Calculate the weighted sum of values using attention weights
        context_vector = tf.matmul(attention_weights, value)
        
        return context_vector, attention_weights
