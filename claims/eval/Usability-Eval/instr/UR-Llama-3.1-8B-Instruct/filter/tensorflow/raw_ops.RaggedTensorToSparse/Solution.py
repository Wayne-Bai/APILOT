import tensorflow as tf

# Create a random RaggedTensor
ragged_tensor = tf.RaggedTensor.from_row_lengths([1, 2, 3, 4, 0, 6, 7, 0], [2, 2, 1, 1, 2])

print("Initial RaggedTensor:")
print(ragged_tensor)

# Convert the RaggedTensor into a SparseTensor
sparse_tensor = tf.sparse.SparseTensor(censors=tf.zeros(ragged_tensor.shape[1], dtype=tf.int32),
                                       values=ragged_tensor.flat_values,
                                       dense_shape=ragged_tensor.shape)

# Convert the SparseTensor back into a dense Tensor, to make it easier to print
dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=0)

print("\nSparseTensor:")
print(dense_tensor)
