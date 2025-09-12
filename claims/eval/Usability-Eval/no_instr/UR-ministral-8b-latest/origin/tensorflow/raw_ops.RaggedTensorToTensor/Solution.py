import tensorflow as tf

# Example ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5]])

# Convert ragged tensor to a dense tensor
dense_tensor = tf.ragged.constant(ragged_tensor).to_tensor(allowoutval=1)

print(dense_tensor)
