import tensorflow as tf

def sparse_tensor_bincount(sparse_indices, sparse_values, dense_shape, size, weights=None):
    """
    Count the number of occurrences of each value in a sparse tensor with the option to use weights.

    :param sparse_indices: A 2-D Tensor of int64 representing the indices of the sparse tensor.
    :param sparse_values: A 1-D Tensor containing all the values corresponding to the indices in the sparse tensor.
    :param dense_shape: A 1-D Tensor of int64 representing the shape of the sparse tensor.
    :param size: The non-negative integer size of the output tensor (maximum value + 1).
    :param weights: A 1-D Tensor of weights, same shape as `sparse_values` (optional).
    :return: A 1-D Tensor of the same type as `sparse_values` which holds the bin counts.
    """
    sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=dense_shape)
    
    if weights is not None:
        return tf.raw_ops.SparseCountSparseOutput(indices=sparse_tensor.indices,
                                                  values=sparse_tensor.values,
                                                  dense_shape=sparse_tensor.dense_shape,
                                                  size=size,
                                                  weights=weights)
    else:
        return tf.raw_ops.SparseCountSparseOutput(indices=sparse_tensor.indices,
                                                  values=sparse_tensor.values,
                                                  dense_shape=sparse_tensor.dense_shape,
                                                  size=size)

# Example usage:
indices = tf.constant([[0, 0], [1, 2]])
values = tf.constant([1, 2])
dense_shape = tf.constant([3, 4])
size = 3

bin_counts = sparse_tensor_bincount(indices, values, dense_shape, size)
print(bin_counts)
