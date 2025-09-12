import tensorflow as tf

def segment_sum(data, segment_ids):
    """
    Computes the sum along segments of a tensor.
    
    Parameters:
    data (tf.Tensor): The input tensor.
    segment_ids (tf.Tensor): A 1-D tensor containing the segment IDs for each element in data.

    Returns:
    tf.Tensor: A tensor where each value is the sum of the input tensor elements 
                corresponding to each segment ID.
    """
    return tf.math.unsorted_segment_sum(data, segment_ids, num_segments=tf.reduce_max(segment_ids) + 1)

# Example usage
data = tf.constant([1, 2, 3, 4, 5])
segment_ids = tf.constant([0, 0, 1, 1, 1])
result = segment_sum(data, segment_ids)
print(result.numpy())
