import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Args:
    data (tf.Tensor): The input tensor.
    segment_ids (tf.Tensor): The segment IDs. Values should be in the range [0, num_segments).

    Returns:
    tf.Tensor: The sum along segments of the input tensor.
    """
    # Get the number of segments
    num_segments = tf.math.reduce_max(segment_ids) + 1

    # Compute the sum along segments
    segment_sum = tf.math.unsorted_segment_sum(data, segment_ids, num_segments)

    return segment_sum

# Example usage:
if __name__ == "__main__":
    # Create a sample tensor
    data = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=tf.float32)

    # Create sample segment IDs
    segment_ids = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)

    # Compute the sum along segments
    result = segment_sum(data, segment_ids)

    print(result)
