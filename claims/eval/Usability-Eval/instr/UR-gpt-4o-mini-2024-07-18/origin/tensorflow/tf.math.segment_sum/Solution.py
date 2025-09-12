import tensorflow as tf

def segment_sum(data, segment_ids):
    # Use tf.unsorted_segment_sum to compute the sum along segments
    return tf.unsorted_segment_sum(data, segment_ids, num_segments=tf.reduce_max(segment_ids) + 1)

# Example usage
data = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
segment_ids = tf.constant([0, 1, 0])

result = segment_sum(data, segment_ids)
print(result.numpy())
