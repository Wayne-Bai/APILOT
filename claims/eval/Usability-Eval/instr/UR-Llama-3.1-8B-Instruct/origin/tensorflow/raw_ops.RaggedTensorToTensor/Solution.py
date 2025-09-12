import tensorflow as tf

# Create a sample ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Define the new shape
new_shape = (2, 3)

# Use tf.reshape with ragged=ragged argument to create a dense tensor
dense_tensor = tf.reshape(ragged_tensor, new_shape)

print(dense_tensor)
