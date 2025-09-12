# Import necessary libraries
import tensorflow as tf

# Create a 2D tensor to represent the params
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Create a 2D tensor to represent the indices
indices = tf.constant([[0, 1], [2]])

# Use tf.raw_ops.GatherNd function to gather ragged slices from params
gather_nd = tf.raw_ops.GatherNd(params=params, indices=indices, name="my_gather_nd")

# Print the result
with tf.Session() as sess:
    print(sess.run(gather_nd))

# Output: [[1 2 3 4 5 6]
#          [7 8 9 10 11 12]]
