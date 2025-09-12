import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Args:
    data (tf.Tensor): The input tensor.
    segment_ids (tf.Tensor): A 1-D tensor. Values should be sorted and can be repeated.

    Returns:
    tf.Tensor: Has same shape as data, except for dimension 0 which has size `tf.math.reduce_max(segment_ids) + 1`.
    """
    # Get the number of segments
    num_segments = tf.math.reduce_max(segment_ids) + 1

    # Initialize the output tensor with zeros
    output = tf.zeros((num_segments, tf.shape(data)[1]))

    # Use tf.math.unsorted_segment_sum to compute the sum along segments
    output = tf.math.unsorted_segment_sum(data, segment_ids, num_segments)

    return output


# Example usage:
if __name__ == "__main__":
    # Input data
    data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

    # Segment IDs
    segment_ids = tf.constant([0, 0, 1, 1])

    # Compute segment sum
    segment_sum_value = segment_sum(data, segment_ids)

    print("Segment Sum:")
    print(segment_sum_value)
