import tensorflow as tf

def segment_sum(data, segment_ids):
    """Computes the sum along segments of a tensor.

    Args:
        data (tf.Tensor): The input data to be summed along each segment.
        segment_ids (tf.Tensor): A 1-D tensor representing the segments.

    Returns:
        tf.Tensor: The sum along each segment of the input tensor.
    """
    num_segments = tf.size(segment_ids)
    data_shape = tf.shape(data)
    data = tf.reshape(data, [-1])
    result = tf.zeros([num_segments], dtype=tf.float32)
    for i in range(num_segments):
        segment_mask = tf.equal(segment_ids, i)
        segment_data = tf.boolean_mask(data, segment_mask)
        result[i] += tf.reduce_sum(segment_data)
    return tf.reshape(result, data_shape)
