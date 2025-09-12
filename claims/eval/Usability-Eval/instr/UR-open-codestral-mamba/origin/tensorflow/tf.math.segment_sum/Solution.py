import tensorflow as tf

# Assume we have the following tensor 'x' and segment ids 's'
x = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=tf.float32)
s = tf.constant([0, 0, 1, 2, 2, 2, 3, 4, 5, 4], dtype=tf.int32)

# We first need to generate a segment sparse tensor out of x
_, indices, segments_sum = tf.raw_ops.UnsortedSegmentSum(x=x, segment_ids=s, num_segments=6)

with tf.Session() as sess:
    print(segments_sum.eval())
