
import tensorflow as tf

# Create a tensor to work with
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the segment ids
segment_ids = tf.constant([0, 0, 1])

# Compute the sum along segments of the tensor
segment_sum = tf.math.segment_sum(input_tensor, segment_ids)

print(segment_sum)
