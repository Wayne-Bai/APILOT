import tensorflow as tf

# Create a variable to update
resource = tf.Variable(initial_value=[[1, 2], [3, 4]], trainable=True)

# Create a placeholder for the updated values
updated_values = tf.placeholder(dtype=tf.float32, shape=[None])

# Use the sparse_update op to update the variable with the new values
sparse_update = tf.raw_ops.SparseUpdate(resource=resource, indices=[[0, 1], [1, 0]], values=updated_values)

# Execute the session and display the updated values
with tf.Session() as sess:
  result = sess.run(sparse_update, feed_dict={updated_values: [[5, 6]]})
  print(result)
