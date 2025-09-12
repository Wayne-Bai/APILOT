import tensorflow as tf

def segment_sum(data, segment_ids):
    return tf.math.segment_sum(data, segment_ids)

# Example usage
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])

result = segment_sum(data, segment_ids)
print(result)  # Output will be [3, 7, 11] since it sums segments of the tensor based on segment_ids
