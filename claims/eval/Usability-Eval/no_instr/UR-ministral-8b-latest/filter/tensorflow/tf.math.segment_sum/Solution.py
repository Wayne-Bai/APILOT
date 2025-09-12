import tensorflow as tf

def compute_segment_sums(tensor, segment_indices):
    """
    Compute the sum along segments of a tensor.

    :param tensor: A TensorFlow tensor of shape (N, M).
    :param segment_indices: A TensorFlow tensor of shape (K,), containing the indices of segment starting points.
    :return: A TensorFlow tensor of shape (K,), containing the sums for each segment.
    """
    segment_sums = []
    for i in range(len(segment_indices) - 1):
        start = segment_indices[i]
        end = segment_indices[i + 1]
        segment = tensor[start:end]
        segment_sum = segment.reduce_sum()
        segment_sums.append(segment_sum)

    # Handle the last segment separately
    last_segment = tensor[segment_indices[-1]:]
    last_segment_sum = last_segment.reduce_sum()
    segment_sums.append(last_segment_sum)

    return tf.constant(segment_sums)

# Example usage:
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
segment_indices = tf.constant([0, 2, 3], dtype=tf.int32)
result = compute_segment_sums(tensor, segment_indices)
print(result.numpy())
