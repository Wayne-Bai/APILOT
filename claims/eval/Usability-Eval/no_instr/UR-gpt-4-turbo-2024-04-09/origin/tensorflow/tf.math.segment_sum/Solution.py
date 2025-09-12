import tensorflow as tf

# Create a tensor (for example, a list of values)
tensor = tf.constant([5, 1, 7, 2, 3, 8])

# Define segment ids for each tensor element (indicating which segment they belong to)
segments = tf.constant([0, 0, 1, 1, 2, 2])

# Compute the sum along segments
segmented_sum = tf.math.segment_sum(tensor, segments)

# Print the result
print(segmented_sum.numpy())
