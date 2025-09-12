import tensorflow as tf

def reshape_sparse_tensor(sparse_tensor, new_dense_shape):
    """
    Reshapes a SparseTensor to represent values in a new dense shape.

    Args:
    sparse_tensor (tf.SparseTensor): The input SparseTensor to be reshaped.
    new_dense_shape (tf.Tensor): A 1-D tensor representing the new dense shape.

    Returns:
    tf.SparseTensor: The reshaped SparseTensor.
    """
    # Check if the input is a SparseTensor
    assert isinstance(sparse_tensor, tf.SparseTensor)

    # Check if the new_dense_shape is a 1-D tensor
    assert tf.rank(new_dense_shape) == 1

    # Compute the number of non-zero values in the reshaped SparseTensor
    num_nonzeros = tf.reduce_prod(new_dense_shape)

    # Create a new SparseTensor with the reshaped shape
    reshaped_sparse_tensor = tf.sparse.from_dense(
        tf.sparse.to_dense(sparse_tensor),
        new_dense_shape,
        num_nonzeros,
        sparse_tensor.dense_shape
    )

    return reshaped_sparse_tensor
