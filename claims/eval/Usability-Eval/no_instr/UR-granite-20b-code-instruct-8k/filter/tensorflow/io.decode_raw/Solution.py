import tensorflow as tf

# Assuming raw_bytes is the input tensor containing raw bytes data
# Convert raw bytes from input tensor into numeric tensors
numeric_tensors = tf.io.decode_raw(raw_bytes, out_type=tf.float32)
