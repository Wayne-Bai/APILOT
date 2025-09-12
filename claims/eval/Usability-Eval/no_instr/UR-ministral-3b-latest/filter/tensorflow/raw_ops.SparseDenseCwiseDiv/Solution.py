import tensorflow as tf

# Function to divide a SparseTensor by a dense Tensor
def divide_sparse_by_dense(sparse_tensor, dense_tensor):
    result = tf.raw_ops.ComponentwiseDivideSparse(sparse_tensor, dense_tensor)
    return result

# Example Usage:
sparse_tensor = tf.sparse.Constant(tf.constant([[1., 2., 3.], [4., 5., 6.]]), tf.SparseTensor(shape=[2, 3], indices=[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]], values=[1, 4, 1, 4, 1, 4]))
dense_tensor = tf.constant([[1, 2, 3], [1, 2, 3]])

divided_tensor = divide_sparse_by_dense(sparse_tensor, dense_tensor)
print(divided_tensor)
