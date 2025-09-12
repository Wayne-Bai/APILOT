import tensorflow as tf

def segment_sum(data, segment_ids, num_segments):
    """
    Computes the sum along segments of a tensor.
    
    Parameters:
    data: A tensor containing data to be summed.
    segment_ids: A 1-D tensor containing the segment IDs for each entry. Length 
                 should be the same as the first dimension of data.
    num_segments: The desired number of segments.
    
    Returns:
    A tensor of the same type as data, reduced along the segment dimension.
    """
    return tf.math.unsorted_segment_sum(data, segment_ids, num_segments)

# Example usage:
data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.int32)
segment_ids = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)
num_segments = 3

result = segment_sum(data, segment_ids, num_segments)
print(result.numpy())  # Output: [3 7 11] since (1+2), (3+4), and (5+6)
