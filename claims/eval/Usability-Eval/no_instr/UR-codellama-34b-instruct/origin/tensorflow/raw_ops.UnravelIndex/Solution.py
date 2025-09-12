import tensorflow as tf

# Create a tensor with some arbitrary data
data = tf.constant([1, 2, 3, 4])

# Flatten the tensor into a 1D array of indices
indices = tf.range(data.shape[0], dtype=tf.int64)

# Convert the indices into a tuple of coordinate arrays
coords = tf.unravel_index(indices, data.shape)

print(coords)  # Output: (array([1, 2, 3, 4]), array([0, 0, 0, 0]))
