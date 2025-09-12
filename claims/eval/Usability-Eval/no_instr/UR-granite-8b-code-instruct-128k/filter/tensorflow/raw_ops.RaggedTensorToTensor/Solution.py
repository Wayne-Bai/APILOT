
import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Generate a dense tensor from the ragged tensor
dense_tensor = tf.sparse_tensor_to_dense(ragged_tensor)

# Print the dense tensor
print(dense_tensor)
