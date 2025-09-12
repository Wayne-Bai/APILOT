import tensorflow as tf

# Assuming 'input_tensor' is your raw bytes tensor
input_tensor = tf.constant(b'raw_bytes')

# Convert raw bytes to numeric tensors
numeric_tensor = tf.io.decode_raw(input_tensor, tf.uint8)
