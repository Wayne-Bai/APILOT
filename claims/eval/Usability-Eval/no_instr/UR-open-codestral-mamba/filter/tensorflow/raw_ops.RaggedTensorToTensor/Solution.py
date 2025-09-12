import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Convert the ragged tensor to a dense tensor
dense_tensor = tf.ragged.constant_value(ragged_tensor)

print(dense_tensor)
