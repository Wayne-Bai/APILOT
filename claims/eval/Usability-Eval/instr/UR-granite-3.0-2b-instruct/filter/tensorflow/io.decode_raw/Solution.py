import tensorflow as tf

# Assuming input_tensor is your raw bytes tensor
input_tensor = tf.constant(raw_bytes, dtype=tf.string)

# Decode the bytes tensor to string tensor
decoded_tensor = tf.string_to_bytes(input_tensor)

# Convert the string tensor to numeric tensor (e.g., float or int)
numeric_tensor = tf.cast(decoded_tensor, tf.float32)  # or tf.int32
