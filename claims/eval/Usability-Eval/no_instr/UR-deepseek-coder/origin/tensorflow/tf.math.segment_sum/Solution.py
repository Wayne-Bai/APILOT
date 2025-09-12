import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.

    Args:
        data: A Tensor. Must be one of the following types: float32, float64, int32, uint8, int16, int8, int64, bfloat16, uint16, half, uint32, uint64.
        segment_ids: A Tensor. Must be one of the following types: int32, int64.
                     A 1-D tensor whose size is equal to the size of the first dimension of `data`.
                     Values should be sorted and can be repeated.

    Returns:
        A Tensor. Has the same type as `data`.
    """
    return tf.math.segment_sum(data, segment_ids)

# Example usage:
data = tf.constant([5, 1, 7, 2, 3, 4], dtype=tf.int32)
segment_ids = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)
result = segment_sum(data, segment_ids)
print(result.numpy())  # Output: [6 9 7]
