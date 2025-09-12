import tensorflow as tf

def sparse_bin_counting(sparse_input, num_bins, default_value=0):
    # Convert sparse tensor to dense tensor
    dense_input = tf.sparse.to_dense(sparse_input, default_value=default_value)
    
    # Perform bin counting
    bin_counts = tf.bincount(dense_input, minlength=num_bins, maxlength=num_bins)
    
    return bin_counts

# Example usage:
# Assuming `sparse_tensor` is your sparse tensor input
# sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 3], dense_shape=[3, 4])
# num_bins = 5
# result = sparse_bin_counting(sparse_tensor, num_bins)
# print(result)
