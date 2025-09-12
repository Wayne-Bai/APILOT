import tensorflow as tf

# Assuming you have an input tensor of flat indices
flat_indices = tf.constant([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Use tf.unravel_index to convert flat indices to coordinate arrays
unraveled_indices = tf.unravel_index(flat_indices, shape=(3, 3))

# Print the result
print(unraveled_indices)
