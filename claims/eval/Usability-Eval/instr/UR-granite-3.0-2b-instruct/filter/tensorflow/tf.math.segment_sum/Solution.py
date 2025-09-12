import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the segment ids
segment_ids = tf.constant([[0, 0, 1], [1, 1, 1], [2, 2, 2]])

# Compute the sum along segments
sum_along_segments = tf.reduce_sum(tf.gather_nd(tensor, tf.argsort(segment_ids, batch_dims=1)))

# Print the result
print(sum_along_segments)
