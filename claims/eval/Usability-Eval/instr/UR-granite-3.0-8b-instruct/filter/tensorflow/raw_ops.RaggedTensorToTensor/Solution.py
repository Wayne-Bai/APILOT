import tensorflow as tf

# Assuming ragged_tensor is your input ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Use tf.raw_ops.RaggedToDense to create a dense tensor from the ragged tensor
dense_tensor = tf.raw_ops.RaggedToDense(ragged_tensor, default_value=0)

# Print the dense tensor
print(dense_tensor)
