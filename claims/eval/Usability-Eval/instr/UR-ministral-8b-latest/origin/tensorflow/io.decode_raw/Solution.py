import tensorflow as tf

# Assume `raw_bytes_tensor` is your input tensor containing raw bytes
raw_bytes_tensor = tf.constant(b'hello world', dtype=tf.string)

# Convert raw bytes tensor to numeric tensor (i.e., characters)
numeric_tensor = raw_bytes_tensor

# Print the shape and content of the numeric tensor
print("Shape:", numeric_tensor.shape)
print("Content:", numeric_tensor.numpy().decode('utf-8'))
