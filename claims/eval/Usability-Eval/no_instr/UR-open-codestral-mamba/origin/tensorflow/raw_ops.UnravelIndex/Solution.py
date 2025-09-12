import tensorflow as tf

# Converts an array of flat indices into a tuple of coordinate arrays
tensor_shape = tf.constant([3, 3])  # Shape of the tensor
flat_indices = tf.constant([2, 5])  # Flat indices
output = tf.unravel_index(flat_indices, tensor_shape)

print(output)
