import tensorflow as tf

# Define the input sparse tensor
indices = [[0, 0], [1, 2]]
values = [4.0, 5.0]
dense_shape = [2, 3]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_tensor.shape)

# Define the dense tensor
dense_tensor = tf.constant([[2.0, 3.0, 4.0], [1.0, 6.0, 2.0]], dtype=tf.float32)
sparse_tensor_out = tf.sparse.sparse_dense_div(sparse_tensor, dense_tensor)
print(sparse_tensor_out)
