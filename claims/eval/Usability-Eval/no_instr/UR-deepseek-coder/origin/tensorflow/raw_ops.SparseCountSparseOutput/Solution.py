import tensorflow as tf

def sparse_bin_count(sparse_indices, sparse_values, sparse_shape, num_bins, weights=None):
    # Create a dense tensor from the sparse tensor
    dense_tensor = tf.sparse.to_dense(tf.SparseTensor(sparse_indices, sparse_values, sparse_shape))
    
    # Flatten the dense tensor to a 1D tensor
    flat_tensor = tf.reshape(dense_tensor, [-1])
    
    # If weights are provided, apply them to the values
    if weights is not None:
        flat_tensor = flat_tensor * weights
    
    # Perform bin counting
    bin_counts = tf.math.bincount(flat_tensor, minlength=num_bins, maxlength=num_bins)
    
    return bin_counts

# Example usage:
# sparse_indices = tf.constant([[0, 0], [1, 2], [2, 3]])
# sparse_values = tf.constant([1, 2, 3])
# sparse_shape = tf.constant([3, 4])
# num_bins = 4
# weights = tf.constant([0.5, 1.0, 1.5])

# bin_counts = sparse_bin_count(sparse_indices, sparse_values, sparse_shape, num_bins, weights)
# print(bin_counts.numpy())
