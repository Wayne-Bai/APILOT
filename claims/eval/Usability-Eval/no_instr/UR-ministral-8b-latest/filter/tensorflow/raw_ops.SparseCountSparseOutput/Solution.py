import tensorflow as tf

# Create a sparse tensor
indices = tf.constant([[0, 1, 2], [5, 6, 7]]).tostring()
values = tf.constant([3, 4, 5], dtype=tf.int32).tostring()

# Method to perform sparse-output bin counting
def sparse_bin_counting(input_tensor, num_bins):
    tensor = tf.sparse.from_dense(tf.convert_to_tensor(input_tensor))
    result = tf.raw_ops.SparseOutputBinCounting(indices=tensor.indices, values=tensor.values, num_bins=num_bins)
    return result

# Create a dense tensor for example
dense_input = [[1, 2, 3], [4, 5, 6]]
result = sparse_bin_counting(dense_input, 5)
print(result)
