import tensorflow as tf

def bin_count_sparse(tensor):
    tensor_desc_dense = tf.raw_ops.SparseBinCount(
        values=tensor,
        num=self.num_quantized_bins,
        shape=self.shape,
        reduce_mean=False,
        number_dimensions=0)
    return tensor_desc_dense

# Example usage:
# Define your sparse tensor
sparse_tensor = tf.constant([[[0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 1]]],
                            dtype=tf.int32)
sparse_tensor_dense = tf.raw_ops.SparseBinCount(
    values=sparse_tensor,
    num=5,  # Number of bins
    shape=[2, 2],  # Example shape
    reduce_mean=False,
    number_dimensions=0
)
print(sparse_tensor_dense)
