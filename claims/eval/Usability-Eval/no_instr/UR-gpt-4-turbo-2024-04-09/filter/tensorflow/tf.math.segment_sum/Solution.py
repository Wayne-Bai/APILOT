import tensorflow as tf

def segment_sum(data, segment_ids):
    return tf.math.segment_sum(data, segment_ids)

# Example usage
data = tf.constant([1, 2, 3, 4, 5, 6])
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])
result = segment_sum(data, segment_ids)
print(result)  # Output: tf.Tensor([ 3  7 11], shape=(3,), dtype=int32)
