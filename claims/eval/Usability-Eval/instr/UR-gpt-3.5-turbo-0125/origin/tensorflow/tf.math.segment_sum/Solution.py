
import tensorflow as tf

# Create a tensor
input_tensor = tf.constant([[1, 2], [3, 4], [5, 6]])

# Define the segment ids
segment_ids = tf.constant([0, 0, 1])

# Compute the sum along segments
segment_sum = tf.math.segment_sum(input_tensor, segment_ids)

print(segment_sum)
