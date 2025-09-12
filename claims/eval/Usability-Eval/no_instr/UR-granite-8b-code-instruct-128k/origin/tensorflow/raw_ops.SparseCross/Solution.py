import tensorflow as tf

# Create a sparse tensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Create a dense tensor
dense_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Generate the sparse cross
sparse_cross = tf.raw_ops.SparseCross(inputs=[sparse_tensor, dense_tensor])

# Print the result
print(sparse_cross)
