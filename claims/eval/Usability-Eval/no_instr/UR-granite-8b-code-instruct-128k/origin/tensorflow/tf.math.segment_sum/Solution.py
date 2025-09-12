import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6])

# Define the segments
segments = tf.constant([0, 0, 1, 1, 1, 2])

# Compute the sum along segments
result = tf.math.segment_sum(tensor, segments)

# Print the result
print(result)
