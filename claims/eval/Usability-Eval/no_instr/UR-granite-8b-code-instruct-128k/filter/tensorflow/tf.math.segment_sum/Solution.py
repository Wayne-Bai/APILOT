
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=(6,))

# Define the segment ids
segment_ids = tf.constant([0, 0, 1, 1, 2, 2], shape=(6,))

# Compute the segment sum using tf.math.segment_sum()
output_tensor = tf.math.segment_sum(input_tensor, segment_ids)

# Print the output tensor
print(output_tensor)
