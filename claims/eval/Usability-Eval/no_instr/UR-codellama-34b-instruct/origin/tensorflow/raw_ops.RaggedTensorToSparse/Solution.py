
import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [], [4]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.raw_ops.RaggedToSparse(
    values=ragged_tensor.flat_values,
    indices=ragged_tensor.row_splits,
    dense_shape=ragged_tensor.dense_shape)
