import tensorflow as tf

# Function to compute the sum along segments
def segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Args:
    data: A tensor containing the data to be summed.
    segment_ids: A tensor of the same shape as 'data' specifying the segment index.

    Returns:
    A tensor with the same type as 'data' where the sum has been computed along the segments.
    """
    return tf.math.unsorted_segment_sum(data, segment_ids, num_segments=tf.reduce_max(segment_ids) + 1)

# Example usage
if __name__ == "__main__":
    # Create example data
    data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.float32)
    # Define segment IDs
    segment_ids = tf.constant([0, 1, 1, 2, 2, 2], dtype=tf.int32)
    # Compute the segment sum
    segment_sum_result = segment_sum(data, segment_ids)
    # Print the result
    tf.print("Segment Sum Result:", segment_sum_result)
