import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6, 7, 8]])

# Create a dense tensor from the ragged tensor
dense_tensor = tf.ragged.to_tensor(ragged_tensor)

#ALTER the shape of the dense tensor
reshaped_tensor = tf.reshape(dense_tensor, [4, -1])

print(reshaped_tensor)
