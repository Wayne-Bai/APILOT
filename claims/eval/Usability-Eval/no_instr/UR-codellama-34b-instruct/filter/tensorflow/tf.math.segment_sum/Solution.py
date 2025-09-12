
import tensorflow as tf

# Input data
data = tf.constant([[1, 2], [3, 4]])

# Segment ids for each element in the input data
segment_ids = tf.constant([0, 0, 1, 1])

# Compute sum along segments
sess = tf.Session()
with sess.as_default():
    result = tf.math.unsorted_segment_sum(data=data, segment_ids=segment_ids)

print(result)
