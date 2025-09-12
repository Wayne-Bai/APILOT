import tensorflow as tf

def bin_counting(sparse_tensor, count=True):
    """Perform bin counting for a sparse tensor.

    Args:
        sparse_tensor (tf.SparseTensor): The sparse tensor to perform bin counting on.
        count (bool, optional): Whether to return the count of non-zero elements in each bin. Defaults to True.

    Returns:
        list[tf.Tensor]: A list of tensors containing the bin counts or the count of non-zero elements in each bin.
    """
    # Calculate the number of bins based on the maximum value in the sparse tensor
    max_value = tf.reduce_max(sparse_tensor)
    num_bins = max_value + 1

    # Initialize a list to store the count for each bin
    bin_counts = [0] * num_bins

    # Iterate through each value in the sparse tensor and add it to its corresponding bin
    for v in tf.nest.flatten(sparse_tensor):
        i = tf.cast(v, tf.int64)
        if count:
            bin_counts[i] += 1
        else:
            bin_counts[i] = 1

    # Convert the list of counts to a tensor
    return tf.convert_to_tensor(bin_counts, dtype=tf.float32)
