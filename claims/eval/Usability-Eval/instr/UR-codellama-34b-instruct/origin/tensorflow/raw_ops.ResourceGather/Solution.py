
import tensorflow as tf

# Create a placeholder for the variable we want to gather from
var = tf.placeholder(tf.float32, shape=[None])

# Create a tensor for the indices
indices = tf.constant([[0], [1], [2]])

# Use the `Gather` op to gather slices from the variable
slices = tf.raw_ops.Gather(var=var, indices=indices)

# Evaluate the `Gather` op using a session and print the results
with tf.Session() as sess:
  result = sess.run(slices)
  print(result)
