import tensorflow as tf

def sparse_output_bin_counting(sparse_indices, sparse_values, sparse_shape, bins, type):
    """
    Performs sparse-output bin counting for a sparse tensor.

    Args:
    sparse_indices: A 2D Tensor of type int64. Indices of the sparse tensor.
    sparse_values: A 1D Tensor. Values of the sparse tensor.
    sparse_shape: A 1D Tensor of type int64. Shape of the sparse tensor.
    bins: A 1D Tensor. Defines the bins for counting.
    type: Data type for the output tensor.

    Returns:
    A Tensor of the defined type representing bin counts.
    """
    # Creating the SparseTensor
    sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=sparse_shape)
    
    # Using bincount over the sparse tensor
    result = tf.sparse.bincount(sp_input=sparse_tensor, size=bins.shape[0]+1, weights=None, binary_output=False)
    
    # Cast result to desired output type
    result_cast = tf.cast(result, dtype=type)
    
    return result_cast

# Example usage
sparse_indices = tf.constant([[0, 0], [1, 2]])
sparse_values = tf.constant([1, 2])
sparse_shape = tf.constant([3, 4])
bins = tf.constant([0, 1, 2, 3])

# Call function
bin_counts = sparse_output_bin_counting(sparse_indices, sparse_values, sparse_shape, bins, tf.int32)
print(bin_counts)
