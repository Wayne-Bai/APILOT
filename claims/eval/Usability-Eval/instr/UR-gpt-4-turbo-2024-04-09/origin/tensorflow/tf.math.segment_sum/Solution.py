import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    Computes the sum of elements in data tensor along segments specified by segment_ids.

    Args:
    data (tf.Tensor): Tensor containing data to be summed.
    segment_ids (tf.Tensor): An integer tensor of the same size as the data's 0th
                             dimension indicating the segments.

    Returns:
    tf.Tensor: A tensor resulting from segment-wise summation.
    """
    return tf.math.segment_sum(data, segment_ids)

# Example usage:
data = tf.constant([2, 5, 3, 7, 1, 4])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
result = segment_sum(data, segment_ids)
print(result.numpy())  # Output: [7, 10, 5]
