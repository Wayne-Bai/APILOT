import tensorflow as tf

# Define the data tensor and the segments
data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.int32)
segments = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)

# Compute the sum along the segments
segment_sums = tf.math.unsorted_segment_sum(data, segments, num_segments=3)

# Create a session to run the computation (if using TF 1.x; not needed in TF 2.x as eager execution is default)
# with tf.Session() as sess:
#     result = sess.run(segment_sums)
#     print(result)

# In TensorFlow 2.x, just execute the operations eagerly
print(segment_sums.numpy())  # Output: [3 7 11]
