import tensorflow as tf

def componentwise_divide(sparse_tensor, dense_tensor):
    """
    Component-wise divides a SparseTensor by a dense Tensor using tf.raw_ops.
    """
    # Convert the SparseTensor to a DenseTensor
    dense_sparse_tensor = tf.raw_ops.ConvertSparseToDense(sparse_tensor)

    # Perform the component-wise division
    result = dense_sparse_tensor / tf.convert_to_tensor(dense_tensor, dtype=sparse_tensor.dtype)

    return result

# Example Usage
sparse_input = tf.sparse.SparseTensor(indices=[[0, 1], [1, 0]], values=[1.0, 2.0], dense_shape=[2, 2])
dense_input = tf.constant([3.0, 4.0])
result = componentwise_divide(sparse_input, dense_input)

print(result.numpy())
