import tensorflow as tf

# Assuming you have an input tensor of raw bytes
input_bytes = tf.constant([b'hello', b'world'])

# Convert raw bytes into numeric tensors
input_numeric = tf.strings.to_number(input_bytes, tf.int32)

# Print the output
print(input_numeric)
