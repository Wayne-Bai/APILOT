import tensorflow as tf

# Let's assume we have the following data and segment indices
data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.float32)
segment_ids = tf.constant([0, 0, 1, 1, 2, 2])

# Compute the sum along segments
segment_sum = tf.math.unsorted_segment_sum(data, segment_ids, num_segments=3)

# Session to run the computation and print the result
with tf.Session() as sess:
    result = sess.run(segment_sum)
    print(result)
