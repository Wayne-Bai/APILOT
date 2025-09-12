import tensorflow as tf

def unsorted_segment_sum(data, segment_ids, num_segments):
    """
    Computes the sum along segments of a tensor.

    Args:
        data: A Tensor with shape `[batch_size,...]`.
        segment_ids: A Tensor with shape `[batch_size]` and dtype int32 or int64.
        num_segments: A scalar.

    Returns:
        A Tensor with shape `[num_segments,...]`.
    """
    return tf.math.unsorted_segment_sum(data=data, segment_ids=segment_ids, num_segments=num_segments)

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
num_segments = 3

result = unsorted_segment_sum(data, segment_ids, num_segments)
print(result)  # Output: [3, 7, 11]
