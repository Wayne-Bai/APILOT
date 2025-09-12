import tensorflow as tf

# Example raw bytes input tensor
raw_bytes = tf.constant(b'\x01\x02\x03')

# Convert raw bytes to numeric tensor
numeric_tensor = tf.raw_tf.io.decode_raw(raw_bytes, "uint8")

print(numeric_tensor)
