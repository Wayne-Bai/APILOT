
import tensorflow as tf

# Define sparse tensor
indices = tf.constant([[0, 0], [1, 2]], tf.int64)
values = tf.constant([3.0, 4.0], tf.float32)
dense_shape = tf.constant([3, 4], tf.int64)
sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define dense tensor
dense_tensor = tf.constant([[2.0, 0.0, 1.0, 3.0], [1.0, 2.0, 3.0, 4.0], [0.0, 0.0, 0.0, 0.0]], tf.float32)

# Element-wise division of sparse tensor by dense tensor
result = tf.sparse.sparse_dense_cwise_div(sparse_tensor, dense_tensor)

print(result)
