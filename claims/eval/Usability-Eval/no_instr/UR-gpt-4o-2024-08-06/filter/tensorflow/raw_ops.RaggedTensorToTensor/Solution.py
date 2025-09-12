import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Convert the ragged tensor into a dense tensor
dense_tensor = ragged_tensor.to_tensor()

# Print the dense tensor
print(dense_tensor)
