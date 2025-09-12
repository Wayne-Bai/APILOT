import tensorflow as tf

# Create a sample RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5], [], [6]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_tensor())

# Verify the SparseTensor
print("SparseTensor indices:\n", sparse_tensor.indices.numpy())
print("SparseTensor values:\n", sparse_tensor.values.numpy())
print("SparseTensor dense_shape:\n", sparse_tensor.dense_shape.numpy())
