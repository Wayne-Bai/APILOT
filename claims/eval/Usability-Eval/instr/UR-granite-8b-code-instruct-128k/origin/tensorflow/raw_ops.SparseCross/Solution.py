import tensorflow as tf

# Create sparse and dense tensors
sparse_tensor_1 = tf.sparse.SparseTensor(indices=[[0, 0]], values=[1], dense_shape=[1, 1])
sparse_tensor_2 = tf.sparse.SparseTensor(indices=[[0, 1]], values=[2], dense_shape=[1, 1])
dense_tensor = tf.constant([[3]])

# Generate sparse cross
sparse_cross = tf.raw_ops.SparseCross(inputs=[sparse_tensor_1, sparse_tensor_2, dense_tensor], num_sparse=2, sparse_inputs=[0, 1])

# Print the sparse cross
print(sparse_cross)
