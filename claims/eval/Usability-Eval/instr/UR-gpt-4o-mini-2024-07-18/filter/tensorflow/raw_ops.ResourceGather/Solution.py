import tensorflow as tf

# Example variables and indices
resource = tf.Variable(tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
indices = tf.constant([0, 2])  # Row indices to gather

# Using tf.gather to gather slices from the variable
gathered_slices = tf.gather(resource, indices)

# If you want to execute the operation in a session (for TensorFlow 1.x)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     result = sess.run(gathered_slices)
#     print(result)

# For TensorFlow 2.x, you can directly evaluate it.
print(gathered_slices.numpy())
