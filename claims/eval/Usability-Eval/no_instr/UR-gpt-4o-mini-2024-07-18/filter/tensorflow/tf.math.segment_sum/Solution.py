import tensorflow as tf

def segment_sum(data, segment_ids):
    return tf.math.unsorted_segment_sum(data, segment_ids, tf.reduce_max(segment_ids) + 1)

# Example usage
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 1, 2])

result = segment_sum(data, segment_ids)
print(result.numpy())
