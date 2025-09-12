import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    This function computes the sum along segments of a tensor.

    Args:
    data: A Tensor with data that will be segmented.
    segment_ids: A Tensor with the same shape as data's first dimension.

    Returns:
    A Tensor of the same type as data, containing the sum of elements in data belonging to each segment.
    """
    # Create an unsorted segment sum op
    segment_sum_op = tf.math.unsorted_segment_sum(data, segment_ids, num_segments=tf.reduce_max(segment_ids) + 1)

    # Execute with a session
    with tf.Session() as sess:
        result = sess.run(segment_sum_op)

    return result
