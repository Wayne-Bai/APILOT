import tensorflow as tf

# Assuming input_tensor is your raw bytes tensor
input_tensor = tf.constant(b'your_raw_bytes_here')

# Convert bytes to numeric tensors
numeric_tensor = tf.cast(input_tensor, tf.int32)

# Print the numeric tensor
print(numeric_tensor)
