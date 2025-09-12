
import tensorflow as tf

# Assume raw_bytes is the input tensor containing raw bytes
# Convert raw bytes into numeric tensors
numeric_tensors = tf.io.decode_raw(raw_bytes, out_type=tf.float32)

# Continue with further operations using numeric_tensors
