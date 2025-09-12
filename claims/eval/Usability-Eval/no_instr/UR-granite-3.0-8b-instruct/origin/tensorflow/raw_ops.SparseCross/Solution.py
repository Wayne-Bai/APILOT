import tensorflow as tf

# Define a list of sparse and dense tensors
sparse_tensors = [tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[2, 3]),
                  tf.SparseTensor(indices=[[0, 1], [2, 0]], values=[3, 4], dense_shape=[3, 3])]
dense_tensor = tf.constant([[5, 6, 7], [8, 9, 10], [11, 12, 13]])

# Generate sparse cross using tf.raw_ops.SparseCross
sparse_cross = tf.raw_ops.SparseCross(sparse_tensors, dense_tensor)

# Print the result
print(sparse_cross)
