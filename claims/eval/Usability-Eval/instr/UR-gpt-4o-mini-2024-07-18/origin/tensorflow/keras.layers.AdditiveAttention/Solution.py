import tensorflow as tf
from tensorflow.keras.layers import Layer

class AdditiveAttentionLayer(Layer):
    def __init__(self, output_dim, **kwargs):
        super(AdditiveAttentionLayer, self).__init__(**kwargs)
        self.output_dim = output_dim
        self.Wa = self.add_weight(shape=(output_dim, output_dim), initializer='random_normal', trainable=True)
        self.Ua = self.add_weight(shape=(output_dim, output_dim), initializer='random_normal', trainable=True)
        self.Va = self.add_weight(shape=(output_dim, 1), initializer='random_normal', trainable=True)

    def call(self, inputs):
        # inputs are the decoder hidden states and encoder outputs
        decoder_hidden_state, encoder_outputs = inputs
        
        # Expand dimensions for broadcasting
        decoder_hidden_state = tf.expand_dims(decoder_hidden_state, axis=1)
        
        # Score calculation
        score = tf.nn.tanh(tf.matmul(decoder_hidden_state, self.Wa) + tf.matmul(encoder_outputs, self.Ua))
        attention_weights = tf.nn.softmax(tf.matmul(score, self.Va), axis=1)
        
        # Context vector calculation
        context_vector = tf.reduce_sum(attention_weights * encoder_outputs, axis=1)
        
        return context_vector, attention_weights
