import tensorflow as tf

# Example tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the segments in which to sum
segments = [
    [0, 0, 1, 1],
    [1, 1, 2, 2]
]

# Compute the sum along segments
sum_along_segments = [tf.reduce_sum(tf.gather_nd(tensor, segment.reshape(-1, 1))) for segment in segments]

# Output the results
print(sum_along_segments)
