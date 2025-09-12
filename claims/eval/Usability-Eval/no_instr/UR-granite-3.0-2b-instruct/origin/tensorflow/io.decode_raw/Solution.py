import tensorflow as tf

# Assuming input_tensor is the raw bytes tensor
input_tensor = tf.constant(raw_bytes, dtype=tf.uint8)

# Decode the bytes tensor into a string tensor
string_tensor = tf.string.decode(input_tensor, 'utf-8')

# Convert the string tensor into a numeric tensor
numeric_tensor = tf.string_to_numbers(string_tensor)
