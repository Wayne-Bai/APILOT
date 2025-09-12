import tensorflow as tf

def sparse_reshape(sparse_tensor, new_shape):
    """
    Reshapes a SparseTensor to represent values in a new dense shape.

    Args:
        sparse_tensor: A SparseTensor to be reshaped.
        new_shape: The new dense shape for the SparseTensor.

    Returns:
        A SparseTensor with new dense shape.
    """
    
    # Convert the sparse tensor to a SparseTensorValue
    sparse_tensor_value = tf.SparseTensorValue(indices=sparse_tensor.indices, values=sparse_tensor.values, dense_shape=sparse_tensor.dense_shape)
    
    # Reshape the sparse tensor
    reshaped_sparse_tensor = tf.raw_ops.SparseReshape(sparse_indices=sparse_tensor_value.indices, output_shape=new_shape, input_values=sparse_tensor.values)
    
    return reshaped_sparse_tensor

# Create a sparse tensor
sparse_tensor = tf.sparse.from_dense([[1, 0, 0], [0, 2, 0]])

# Reshape the sparse tensor
new_shape = [3, 2]
reshaped_sparse_tensor = sparse_reshape(sparse_tensor, new_shape)

# Print the reshaped sparse tensor
print(reshaped_sparse_tensor)
