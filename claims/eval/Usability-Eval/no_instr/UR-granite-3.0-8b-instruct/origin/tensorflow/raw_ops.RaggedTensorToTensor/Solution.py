import tensorflow as tf

# Assuming ragged_tensor is your input ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5]])

# To create a dense tensor from a ragged tensor, you can use the `tf.ragged.to_dense` function
dense_tensor = tf.ragged.to_dense(ragged_tensor)

print(dense_tensor)
