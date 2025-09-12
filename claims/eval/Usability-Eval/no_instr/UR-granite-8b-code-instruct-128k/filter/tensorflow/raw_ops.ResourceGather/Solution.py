import tensorflow as tf

# Create a variable
resource = tf.Variable([1, 2, 3, 4, 5], dtype=tf.int32)

# Define the indices to gather
indices = tf.constant([0, 2, 4], dtype=tf.int32)

# Use the tf.raw_ops.Gather method to gather slices from the variable according to the indices
gathered_values = tf.raw_ops.Gather(resource=resource, indices=indices)

# Print the gathered values
with tf.Session() as sess:
    print(sess.run(gathered_values))
