import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6]])

# Convert RaggedTensor into a SparseTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_tensor())

# Print the SparseTensor
print(sparse_tensor)
