
import tensorflow as tf
from tensorflow import keras

class BahdanauAttention(keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super().__init__(**kwargs)
        self.W1 = tf.keras.layers.Dense(units, use_bias=False)
        self.W2 = tf.keras.layers.Dense(units, use_bias=False)
        self.V = tf.keras.layers.Dense(1, use_bias=False)
    
    def call(self, query, values):
        # Compute scores
        score = tf.matmul(tf.matmul(query, self.W1), self.W2, transpose_b=True)
        score = tf.squeeze(score, -1)
        
        # Compute weights
        weights = tf.nn.softmax(score, axis=1)
        
        # Compute output
        output = tf.matmul(weights, values)
        
        return output
