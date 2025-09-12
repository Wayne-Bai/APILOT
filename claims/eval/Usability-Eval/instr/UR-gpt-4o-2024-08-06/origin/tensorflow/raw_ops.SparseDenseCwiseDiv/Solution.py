import tensorflow as tf

# Define indices, values and dense_shape for the SparseTensor
indices = tf.constant([[0, 0], [1, 2]])
values = tf.constant([1.0, 2.0], dtype=tf.float32)
dense_shape = tf.constant([3, 4])

# Create the SparseTensor
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define a dense Tensor (it must have the same shape as the SparseTensor's dense_shape)
dense_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                            [5.0, 6.0, 7.0, 8.0],
                            [9.0, 10.0, 11.0, 12.0]], dtype=tf.float32)

# Convert the SparseTensor to a dense tensor with zero-fill
dense_from_sparse = tf.sparse.to_dense(sparse_tensor)

# Perform element-wise division
result = dense_from_sparse / dense_tensor

# You can also convert and divide without converting to dense if you want to keep it sparse
# Sparse element-wise division
sparse_result = tf.SparseTensor(indices=sparse_tensor.indices,
                                values=sparse_tensor.values / tf.gather_nd(dense_tensor, sparse_tensor.indices),
                                dense_shape=sparse_tensor.dense_shape)

with tf.Session() as sess:
    result_value = sess.run(result)
    sparse_result_value = sess.run(tf.sparse.to_dense(sparse_result))
    
    print("Dense result:")
    print(result_value)
    
    print("\nSparse result converted to dense for comparison:")
    print(sparse_result_value)
