import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], [5, 3, 7, 9]])

# Convert ragged tensor to dense tensor
# Note: This will result in a tensor padded with zeros to match the largest row size
dense_tensor = tf.sparse.to_dense(tf.sparse.from_ragged(ragged_tensor))

# Print the dense tensor
print(dense_tensor)
