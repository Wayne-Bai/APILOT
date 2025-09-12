import tensorflow as tf

# Create sparse and dense tensors
sparse_tensor1 = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
sparse_tensor2 = tf.sparse.SparseTensor(indices=[[0, 1], [2, 3]], values=[3, 4], dense_shape=[3, 4])
dense_tensor = tf.constant([[5, 6], [7, 8], [9, 10]])

# Generate sparse cross
sparse_cross = tf.raw_ops.SparseCross(indices=[sparse_tensor1.indices, sparse_tensor2.indices],
                                       values=[sparse_tensor1.values, sparse_tensor2.values],
                                       dense_inputs=[dense_tensor],
                                       shape=[3, 4],
                                       axis=-1)

# Print the result
print(sparse_cross)
