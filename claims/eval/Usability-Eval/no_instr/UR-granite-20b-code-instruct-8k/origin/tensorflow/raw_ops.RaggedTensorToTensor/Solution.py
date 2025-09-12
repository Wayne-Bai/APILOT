import tensorflow as tf

# Define the input ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Create a dense tensor from the ragged tensor
dense_tensor = tf.ragged.to_tensor(ragged_tensor)

# Print the dense tensor
print(dense_tensor)
