
import tensorflow as tf

# Create a ragged tensor with shape (3, None) and type float32
ragged = tf.ragged.constant([[1.0, 2.0], [3.0], [4.0, 5.0]])

# Encode the ragged tensor into a variant tensor
variant_tensor = tf.ragged.encode(ragged)
