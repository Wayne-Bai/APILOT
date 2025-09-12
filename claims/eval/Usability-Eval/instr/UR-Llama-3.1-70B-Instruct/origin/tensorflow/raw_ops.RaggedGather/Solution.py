import tensorflow as tf

# Create a 2-D tensor
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Define the indices
indices = tf.constant([[0], [2]])

# Use tf.raw_ops.GatherNd to gather slices from params along axis 0 according to indices
gathered_slices = tf.raw_ops.GatherNd(params=params, indices=indices)

# Run the operation
with tf.Session() as sess:
    result = sess.run(gathered_slices)
    print(result)
