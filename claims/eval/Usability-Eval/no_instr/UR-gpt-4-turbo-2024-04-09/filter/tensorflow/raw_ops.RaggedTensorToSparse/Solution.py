import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_tensor())

print("SparseTensor:")
print("Indices:\n", sparse_tensor.indices.numpy())
print("Values:\n", sparse_tensor.values.numpy())
print("Dense Shape:\n", sparse_tensor.dense_shape.numpy())
