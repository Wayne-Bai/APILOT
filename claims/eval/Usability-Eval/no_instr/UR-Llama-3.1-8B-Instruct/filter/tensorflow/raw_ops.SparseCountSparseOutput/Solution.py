import tensorflow as tf

def sparse_bin_counting(input_tensor, boundaries):
    """
    Performs sparse-output bin counting for a sparse tensor input.

    Args:
        input_tensor: A sparse tensor where each sparse tensor represents a single sample in the population.
        boundaries: A 1-D tensor of sorted and unique `boundaries` values. bucketize values into corresponding intervals.

    Returns:
        A dense tensor containing the count of elements in each bin of the corresponding sparse tensor in the input.
    """
    # Reshape the boundaries to match the required shape for tf.histogram_fixed_width_bins
    boundaries = tf.cast(boundaries, tf.float32)
    assert tf.math.reduce_all(boundaries[:-1] < boundaries[1:])

    # Use tf.scatter_nd to perform sparse bin counting
    result = tf.scatter_nd(tf.transpose(input_tensor.indices), 
                           tf.ones(tf.shape(input_tensor.values)), 
                           [input_tensor.dense_shape[0]] + boundaries.shape.as_list())

    # Perform histogram bin counts
    bin_counts = tf.histogram_fixed_width_bins(feature=input_tensor.values, 
                                                value_range=(boundaries[0], boundaries[-1]), 
                                                num_balance=boundaries.shape[-1],
                                                dtype=tf.float32)
    
    # Add and cast bin counts to result tensor
    result += bin_counts
    
    return result

# Example usage:
# Create a sparse tensor with values  [5, 10, 15, 6, 12, 18]
input_tensor = tf.sparse.SparseTensor(indices=[[0], [1], [1], [2], [2], [2]], 
                                       values=[5, 10, 10, 6, 12, 18], 
                                       dense_shape=[3, 6])

# Create boundaries
boundaries = tf.constant([-2, 5, 10, 15, 20], dtype=tf.float32)

# Perform sparse bin counting
result = sparse_bin_counting(input_tensor, boundaries)
print(result)
