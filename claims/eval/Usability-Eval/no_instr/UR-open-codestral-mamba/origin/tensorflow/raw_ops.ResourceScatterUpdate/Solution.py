import tensorflow as tf

# Define the tensor and sparse update indices and values
dense_shape = [3, 3]
sparse_indices = [[0, 0], [1, 2], [2, 1]]
sparse_values = [1, 2, 3]

# Convert the sparse tensor to a dense tensor
sparse_tensor = tf.SparseTensor(sparse_indices, sparse_values, dense_shape)
dense_tensor = tf.sparse.to_dense(sparse_tensor)

# Print the dense tensor
with tf.Session() as sess:
    result = sess.run(dense_tensor)
    print(result)
