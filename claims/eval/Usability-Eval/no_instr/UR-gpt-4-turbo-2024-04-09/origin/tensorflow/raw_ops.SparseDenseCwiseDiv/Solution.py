import tensorflow as tf

def sparse_divide_dense(sparse_tensor, dense_tensor):
    if isinstance(sparse_tensor, tf.SparseTensor) and isinstance(dense_tensor, tf.Tensor):
        # Broadcasting the dense tensor to the shape of sparse tensor
        expanded_dense = tf.broadcast_to(dense_tensor, sparse_tensor.dense_shape)

        # Component-wise division of SparseTensor by the broadcasted Dense Tensor
        divided_values = tf.raw_ops.SparseDenseCwiseDiv(sp_a=sparse_tensor, b=expanded_dense)

        # Create a new SparseTensor with divided values
        result_sparse_tensor = tf.SparseTensor(indices=sparse_tensor.indices,
                                               values=divided_values,
                                               dense_shape=sparse_tensor.dense_shape)
        return result_sparse_tensor
    else:
        raise ValueError("Input must be a SparseTensor and a Tensor")

# Example usage
sparse_tensor_example = tf.SparseTensor(indices=[[0, 0], [1, 2]],
                                        values=[10.0, 30.0],
                                        dense_shape=[3, 4])

dense_tensor_example = tf.constant([[2.0, 3.0, 4.0, 5.0]])

result = sparse_divide_dense(sparse_tensor_example, dense_tensor_example)
tf.sparse.to_dense(result)
