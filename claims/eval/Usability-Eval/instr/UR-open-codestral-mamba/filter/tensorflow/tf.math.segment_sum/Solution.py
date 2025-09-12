import tensorflow as tf

def segment_sum(tensor, segment_ids):
    unique_segments, _ = tf.unique(segment_ids)
    result = tf.reduce_sum(tensor * tf.one_hot(segment_ids, tf.shape(unique_segments)[0]), axis=0)
    return result

# Usage
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.float32)
segment_ids = tf.constant([0, 1, 1, 0, 2, 1])

print(segment_sum(tensor, segment_ids))
