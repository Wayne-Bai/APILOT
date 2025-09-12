import tensorflow as tf

# Define a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define a segment ids tensor
segment_ids = tf.constant([0, 1, 2])

# Compute the sum along segments
segment_sum = tf.math.segment_sum(tensor, segment_ids)

with tf.Session() as sess:
    print(sess.run(segment_sum))
