import tensorflow as tf

def compute_segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Args:
        data (tf.Tensor): The input tensor.
        segment_ids (tf.Tensor): The segment IDs.

    Returns:
        tf.Tensor: The sum along segments of the input tensor.
    """
    # Use unsorted_segment_sum to compute the sum along segments
    num_segments = tf.math.reduce_max(segment_ids) + 1
    segment_sums = tf.math.unsorted_segment_sum(data, segment_ids, num_segments)
    
    return segment_sums

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])

segment_sums = compute_segment_sum(data, segment_ids)
print(segment_sums)
