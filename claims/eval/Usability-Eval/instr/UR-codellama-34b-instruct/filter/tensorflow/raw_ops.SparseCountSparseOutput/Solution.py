
import tensorflow as tf

# Define the shape and type of the input tensor
input_shape = [10, 5]
input_type = tf.int32

# Create a random sparse tensor with the specified shape and type
sparse_tensor = tf.SparseTensor(
    indices=tf.constant([[0], [4], [7]], dtype=tf.int64),
    values=tf.constant([1, 3, 5], dtype=input_type),
    dense_shape=tf.constant(input_shape)
)

# Define the bin edges for the output tensor
bin_edges = tf.range(0, 11, 2, dtype=tf.int32)

# Perform sparse-output bin counting using the `tf.raw_ops` module
sparse_counts = tf.raw_ops.SparseBinCount(
    indices=sparse_tensor.indices,
    values=sparse_tensor.values,
    dense_shape=sparse_tensor.dense_shape,
    bin_edges=bin_edges,
    dtype=tf.int64
)

# Convert the output tensor to a numpy array for display purposes
counts = sparse_counts.numpy()
