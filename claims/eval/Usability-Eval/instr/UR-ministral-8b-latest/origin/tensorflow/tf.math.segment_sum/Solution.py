import tensorflow as tf

def sum_segments(tensor, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Parameters:
        tensor (tf.Tensor): The input tensor along which to sum.
        segment_ids (tf.Tensor): The segment IDs.

    Returns:
        tf.Tensor: The tensor with the sum along the segments.
    """
    # Reshape segment_ids to match the shape of tensor
    # For this purpose, assume segment_ids is a 1D tensor with the same length as the input tensor's batch dimension
    segment_ids = tf.reshape(segment_ids, [-1])

    # Create a one-hot encoding of the segment IDs
    ones = tf.ones(tf.shape(tensor))
    one_hot_segments = tf.one_hot(segment_ids, depth=tf.math.reduce_max(segment_ids) + 1)
    BroadcastingOneHot = tf.broadcast(ones, one_hot_segments, axes=[])

    # Sum up values in each segment
    sum_segments = tf.reduce_sum(tensor * BroadcastingOneHot, axis=0)

    return sum_segments

# Example usage:
tensor_example = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
segment_ids_example = tf.constant([0, 0, 1, 1, 2, 2, 0, 0, 1, 1])

segment_sums = sum_segments(tensor_example, segment_ids_example)
print(segment_sums.numpy())
