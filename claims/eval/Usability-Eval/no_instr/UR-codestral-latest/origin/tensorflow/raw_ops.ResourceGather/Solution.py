import tensorflow as tf

# Create a resource variable
resource = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

# Define indices for gather_nd
indices = tf.constant([[0, 0], [1, 1], [2, 2]])

# Use tf.gather_nd to gather slices from the resource variable
slices = tf.gather_nd(resource, indices)

# Print the gathered slices
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(slices))
