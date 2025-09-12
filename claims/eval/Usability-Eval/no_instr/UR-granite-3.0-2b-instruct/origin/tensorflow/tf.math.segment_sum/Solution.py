import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define segment ids
segment_ids = tf.constant([[0, 0, 0], [1, 1, 1], [2, 2, 2]])

# Compute the sum along segments
sum_along_segments = tf.segment_sum(tensor, segment_ids)

# Print the result
print(sum_along_segments.numpy())
