import tensorflow as tf

def sparse_bin_count(sparse_tensor, num_bins):
    # Create a dense tensor from the sparse tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=0)
    
    # Use tf.math.bincount to count occurrences of each bin
    counts = tf.math.bincount(tf.reshape(dense_tensor, [-1]), minlength=num_bins)
    
    return counts

# Example usage
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 1], [1, 2], [2, 3]], values=[1, 2, 3], dense_shape=[3, 4])
num_bins = 5
bin_counts = sparse_bin_count(sparse_tensor, num_bins)

print(bin_counts)
