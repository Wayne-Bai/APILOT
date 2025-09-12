import tensorflow as tf

# Define a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]], dtype=tf.int32)

# Create a dense tensor from a ragged tensor
dense_tensor = tf.expand_dims(ragged_tensor.to_tensor(), 1)

print(dense_tensor)
