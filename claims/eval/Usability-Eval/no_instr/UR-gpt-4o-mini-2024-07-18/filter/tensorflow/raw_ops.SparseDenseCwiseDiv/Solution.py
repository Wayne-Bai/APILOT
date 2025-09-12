import tensorflow as tf

# Function to component-wise divide a SparseTensor by a dense Tensor
def sparse_tensor_divide_dense(sparse_tensor, dense_tensor):
    # Ensure the shapes are compatible for division
    sparse_shape = sparse_tensor.dense_shape
    dense_shape = tf.shape(dense_tensor)

    if not tf.reduce_all(tf.equal(sparse_shape, dense_shape)):
        raise ValueError("Shapes of SparseTensor and dense Tensor must be compatible for division.")

    # Perform the division using the tf.sparse.sparse_dense_matmul function
    result = tf.sparse.sparse_dense_matmul(sparse_tensor, tf.expand_dims(dense_tensor, axis=-1))

    return tf.squeeze(result)

# Example usage
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1.0, 2.0],
    dense_shape=[3, 4]
)

dense_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                            [5.0, 6.0, 7.0, 8.0],
                            [9.0, 10.0, 11.0, 12.0]])

divided_result = sparse_tensor_divide_dense(sparse_tensor, dense_tensor)
print(divided_result)
