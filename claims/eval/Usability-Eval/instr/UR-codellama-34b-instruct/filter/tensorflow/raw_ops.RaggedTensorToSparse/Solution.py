
import tensorflow as tf

# Create a sample RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4], [5]])

# Convert the RaggedTensor into a SparseTensor
sparse_tensor = tf.SparseTensor(indices=ragged_tensor.flat_values, values=ragged_tensor.flat_row_splits, dense_shape=ragged_tensor.dense_shape)

# Print the resulting SparseTensor
print(sparse_tensor)
