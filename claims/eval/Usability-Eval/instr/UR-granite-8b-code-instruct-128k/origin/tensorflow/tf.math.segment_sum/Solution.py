import tensorflow as tf

# Create a tensor of shape [4, 2]
tensor = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])

# Define the segment indices
segment_ids = tf.constant([0, 0, 1, 1])

# Compute the sum along segments
result = tf.math.segment_sum(tensor, segment_ids)

# Print the result
print(result)
