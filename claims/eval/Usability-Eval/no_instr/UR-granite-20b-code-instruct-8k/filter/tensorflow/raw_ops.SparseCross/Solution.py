import tensorflow as tf

# Define input sparse and dense tensors
sparse_tensors = [
    tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4]),
    tf.SparseTensor(indices=[[0, 0], [2, 3]], values=[3, 4], dense_shape=[3, 4])
]
dense_tensors = [
    tf.constant([[1.0], [2.0], [3.0]]),
    tf.constant([[4.0], [5.0], [6.0]])
]

# Call SparseCross op
sparse_cross_out = tf.raw_ops.SparseCross(
    indices=['concat'],
    values=['merge'],
    sparse_indices=[t.indices for t in sparse_tensors],
    sparse_values=[t.values for t in sparse_tensors],
    sparse_shapes=[t.dense_shape for t in sparse_tensors],
    dense_inputs=dense_tensors
)

# Print the output
print(sparse_cross_out)
