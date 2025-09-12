import tensorflow as tf

# Let's create a sample tensor
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Convert the list to a tensor
data_tensor = tf.constant(data)

# Define the segments to compute sum along
segments = [0, 2]

# Compute the sum along the segments
sum_segments = tf.reduce_sum(data_tensor, axis=-1)

# Output the result
print(sum_segments.numpy())
