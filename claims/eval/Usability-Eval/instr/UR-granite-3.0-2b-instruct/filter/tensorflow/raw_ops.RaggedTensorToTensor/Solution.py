import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.RaggedTensor.from_tensor([
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
])

# Create a dense tensor from the ragged tensor
dense_tensor = tf.sparse.to_dense(ragged_tensor)

# Print the dense tensor
print(dense_tensor)
