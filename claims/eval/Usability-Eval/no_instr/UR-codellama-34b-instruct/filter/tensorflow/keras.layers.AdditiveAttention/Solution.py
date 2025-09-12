import tensorflow as tf

class Attention(tf.keras.layers.Layer):
    def __init__(self, units, num_heads=1):
        super().__init__()
        self.units = units
        self.num_heads = num_heads
        self.WQ = tf.keras.layers.Dense(units)
        self.WK = tf.keras.layers.Dense(units)
        self.WV = tf.keras.layers.Dense(units)
        self.dropout = tf.keras.layers.Dropout(0.1)

    def call(self, query, key, value):
        # Calculate attention scores
        Q = self.WQ(query)  # (batch_size, seq_len, units)
        K = self.WK(key)  # (batch_size, seq_len, units)
        V = self.WV(value)  # (batch_size, seq_len, units)
        scores = tf.matmul(Q, K, transpose_b=True) / tf.math.sqrt(tf.cast(self.units, tf.float32))  # (batch_size, seq_len, num_heads)
        
        # Normalize attention scores
        scores = self.dropout(scores)  # (batch_size, seq_len, num_heads)
        scores = tf.nn.softmax(scores, axis=1)  # (batch_size, seq_len, num_heads)
        
        # Apply attention weights
        outputs = tf.matmul(scores, V)  # (batch_size, seq_len, units)
        outputs = self.dropout(outputs)  # (batch_size, seq_len, units)
        
        return outputs
