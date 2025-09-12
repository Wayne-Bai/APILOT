import tensorflow as tf

def sparse_dense_divide(sparse_tensor, dense_tensor):
    """
    Component-wise divides a SparseTensor by a dense Tensor.

    Parameters:
    sparse_tensor (tf.SparseTensor): The sparse tensor to be divided.
    dense_tensor (tf.Tensor): The dense tensor to divide by.

    Returns:
    tf.SparseTensor: A new SparseTensor resulting from the division.
    """
    # Ensure the dense tensor is compatible with the sparse tensor's shape
    if sparse_tensor.dense_shape[0] != dense_tensor.shape[0]:
        raise ValueError("Shapes of SparseTensor and dense Tensor must match.")

    # Create a SparseTensor to hold the result
    division_result = tf.raw_ops.SparseSparseCwiseDiv(
        x=sparse_tensor,
        y=tf.SparseTensor(indices=dense_tensor.indices, values=dense_tensor.values, dense_shape=dense_tensor.dense_shape)
    )
    
    return division_result

# Example usage:
# Create a SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Create a dense Tensor
dense_tensor = tf.constant([[2, 4, 6, 8], [10, 20, 30, 40], [50, 60, 70, 80]], dtype=tf.float32)

# Perform the division
result = sparse_dense_divide(sparse_tensor, dense_tensor)
