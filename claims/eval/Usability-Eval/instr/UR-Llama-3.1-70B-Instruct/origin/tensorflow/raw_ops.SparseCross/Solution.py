import tensorflow as tf

# Define sparse and dense tensors
sparse_tensor1 = tf.sparse.SparseTensor(indices=[[0, 0], [0, 1], [1, 2]], values=[1, 2, 3], dense_shape=[2, 3])
sparse_tensor2 = tf.sparse.SparseTensor(indices=[[1, 0], [1, 2], [2, 1]], values=[4, 5, 6], dense_shape=[3, 3])
dense_tensor1 = tf.constant([[7, 8, 9], [10, 11, 12]])
dense_tensor2 = tf.constant([[13, 14, 15], [16, 17, 18]])

# Use tf.raw_ops.SparseCross to generate sparse cross
sparse_cross = tf.raw_ops.SparseCross(
    sparse_indices=[sparse_tensor1.indices, sparse_tensor2.indices],
    dense_inputs=[dense_tensor1, dense_tensor2],
    num_sparse=[1, 1],
    num_dense=[1, 1],
    output_index_dtype=tf.dtypes.int64
)

# Print the sparse_cross
print(sparse_cross)
