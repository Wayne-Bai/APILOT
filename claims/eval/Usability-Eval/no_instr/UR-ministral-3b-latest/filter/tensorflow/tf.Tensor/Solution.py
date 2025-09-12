import tensorflow as tf

# Create a one-dimensional constant tensor
constant_tensor = tf.constant([1, 2, 3, 4], dtype=tf.int32)

# Add an additional dimension
constant_tensor_nd = tf.expand_dims(constant_tensor, axis=0)

print(constant_tensor_nd)
