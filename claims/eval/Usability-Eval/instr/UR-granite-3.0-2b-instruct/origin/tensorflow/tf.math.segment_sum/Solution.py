import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Define the segment ids
segment_ids = tf.constant([[0, 0, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]])

# Compute the sum along segments
segment_sums = tf.segment_sum(tensor, segment_ids)

# Print the result
print(segment_sums)
