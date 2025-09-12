import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the segment IDs
segment_ids = tf.constant([0, 1, 0])

# Compute the sum along segments
output_tensor = tf.math.segment_sum(input_tensor, segment_ids)

# Print the output
print(output_tensor)
