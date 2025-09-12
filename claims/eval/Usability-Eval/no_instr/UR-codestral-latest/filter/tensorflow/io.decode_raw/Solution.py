import tensorflow as tf

# Assuming raw_data is your input tensor of type tf.string
# raw_data = tf.constant([b'\x01\x02\x03\x04'])

# Decode raw bytes into a numeric tensor of 32-bit signed integers
numeric_data = tf.io.decode_raw(raw_data, tf.int32)

# Print the numeric tensor
print(numeric_data)
