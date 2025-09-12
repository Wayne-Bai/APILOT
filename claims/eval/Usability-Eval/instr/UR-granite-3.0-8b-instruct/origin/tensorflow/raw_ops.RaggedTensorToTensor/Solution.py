import tensorflow as tf

# Assuming ragged_tensor is your input ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Create a dense tensor from the ragged tensor
dense_tensor = tf.RaggedTensorToDense(ragged_tensor, default_value=0)

print(dense_tensor)
